import re
from sklearn.externals import joblib
import numpy as np

#获取文本内容转变为向量
# import Doc222Vector
# import TextclfModel

#抽取文章特征现在主要用的是正则匹配
class Content(object):

    #获取被告人姓名
    def getbgr_name(self,text):
        pattern = re.compile('被告人(\w*)')
        result = re.search(pattern, text)
        return result.group(1)

    # 案件类型：主要分为1.伪造信用卡或使用虚假身份;2.冒用他人信用卡;3.恶意透支
    def judge_ajlx(self,text):
        pattern1 = re.compile('伪造\w*信用卡|虚假\w*身份证明')
        pattern2 = re.compile('冒用\w*信用卡|拾得\w*信用卡')
        pattern3 = re.compile('恶意透支')
        result = re.search(pattern1, text)
        if result != None:
            return 2
        else:
            result = re.search(pattern2, text)
            if result != None:
                return 1
            else:
                return 0

    # 判定是否坦白，减刑用
    def judge_tb(self,text):
        pattern = re.compile('坦白|如实供述\w*|悔罪|自愿认罪')
        result = re.search(pattern, text)
        if result != None:
            return 1
        else:
            return 0

    # 自首情节,我们认为在本类案件中，自首的人一定坦白，因此此函数返回两个值，是否自首与是否坦白
    # todo：更智能的判断，可以根据语境判断；现在做的是根据正则去匹配，
    def judge_zs(self,text):
        pattern = re.compile('自首')
        result = re.search(pattern, text)
        if result != None:
            tb = 1
            zs = 1
        else:
            zs = 0
            tb = self.judge_tb(text)
        return zs, tb

    #处理金额格式
    def formatre(self,result):
        result = result / 10000
        result = round(result, 2)
        return result

    # 获得被告人犯罪金额
    def getfzjine(self,text):
        pattern = re.compile('共计\w*?(\d+\.\d+)元')
        result = re.search(pattern, text)
        if result != None:
            # print("123456")
            result = float(result.group(1))
            print(result)
            result = self.formatre(result)
        else:
            pattern = re.compile('透支\w*?(\d+\.\d+)元|人民币(\d+\.\d+)元|人民币(\d+)元')
            result = re.search(pattern, text)
            if type(result) == type(None):
                # print(result)
                return 0
            # print(type(None))
            if result.group(1) != None:
                result = float(result.group(1))
                result = self.formatre(result)
            elif result.group(2) != None:
                result = float(result.group(2))
                result = self.formatre(result)
            elif result.group(3) != None:
                result = float(result.group(3))
                result = self.formatre(result)
            else:
                result = 0
        return result

    # 判断是否是未成年
    def judge_lf(self,text):
        pattern = re.compile('累犯')
        result = re.search(pattern, text)
        if result != None:
            return 1
        else:
            return 0

    #通过正则匹配是否偿还欠款
    def judge_pcbyre(self,text):
        patten=re.compile('未归还欠款|尚未归还欠款|仍有欠款未追缴')
        result=re.search(patten,text)
        if result!=None:
            return 0
        else:
            return 1

    # 判断是否是未成年
    def judge_teenager(self,text):
        pattern = re.compile('未成年')
        result = re.search(pattern, text)
        if result != None:
            return 1
        else:
            return 0

    # 是否是怀孕
    def judge_pregnant(self,text):
        pattern = re.compile('怀孕')
        result = re.search(pattern, text)
        if result != None:
            return 1
        else:
            return 0

    #是否是老年人
    def judge_old(self,text):
        pattern = re.compile('老年人|老人')
        result = re.search(pattern, text)
        if result != None:
            return 1
        else:
            return 0

    # 通过正则表达式匹配案件号
    def get_id(text):
        # pattern = re.compile('刑事判决书(.+?)公诉| (（)')
        pattern = re.compile('（.+?号|\(.+?号|〔.+?号')
        result = re.search(pattern, text)
        if result != None:
            return result.group()
        else:
            return None

    # 有期徒刑时间
    def get_yqtx(text):
        pattern = re.compile('拘役|有期徒刑(\w*)')
        result = re.search(pattern, text)
        return (result.group(1))

    # 缓刑
    def get_hx(text):
        pattern = re.compile('缓刑(\w*)')
        result = re.search(pattern, text)
        return (result.group(1))

    # def get_pengch.ang(path):
    #     d=Doc222Vector()
    #     vec, textc = dvec_predict.get_vec(path)
    #     # pattern=re.compile('继续追缴')
    #     # result=re.search(pattern,textc)
    #     # if result!=None:
    #     #     return [0],textc
    #     clfmodel=TextclfModel()
    #     clf=clfmodel.loadclf('./model/clfmodel.m')
    #     vec = clfmodel.get_prodata(vec)
    #     vec = np.array(vec).reshape(-1, 100)
    #     y = clf.predict(vec)
    #     return y, textc

    def get_inputv(self,path):
        pc_label, textc = self.get_pengchang(path)
        id=self.get_id()

        pc_label = pc_label[0]
        name = self.getbgr_name(textc)
        fzlx = self.judge_ajlx(textc)
        zs, tb = self.judge_zs(textc)
        jine = self.getfzjine(textc)
        lf = self.judge_lf(textc)
        teenager = self.judge_teenager(textc)
        pregnant = self.judge_pregnant(textc)
        old = self.judge_old(textc)
        print(name, fzlx, zs, jine, pc_label, tb, lf, teenager, pregnant, old)
        v = np.array([id,name,fzlx, zs, jine, pc_label, tb, lf, teenager, pregnant, old])
        v=v.reshape(1,-1)
        return v