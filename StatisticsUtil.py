import os
from deal_doc import DealtextUtil
from ContenExtraction import Content


#做一些基础性统计
class StatisticsUtil(object):

    #统计文章长度
    def get_longsentence(self,pathlist):
        maxlength=0
        maxlength_name=''
        sentences_count=0
        minlength=float('INF')
        minlength_name=''
        dtu = DealtextUtil()
        doc_count=0
        for path in pathlist:
            files=os.listdir(path)
            doc_count+=len(files)
            for file in files:
                filepath=os.path.join(path,file)
                res=dtu.readdoc(filepath)
                for i in res:
                    if len(i) == 0:
                        res.remove(i)
                length=len(res)
                sentences_count+=length
                if maxlength<length:
                    maxlength=length
                    maxlength_name=file
                if minlength>length:
                    minlength=length
                    minlength_name=file
        print('most sentences',maxlength_name,maxlength)
        print('min sentences',minlength_name,minlength)
        print('aver senteces',sentences_count/doc_count)

    #统计句子长度
    def statistics_word(self, pathlist):
        maxlength = 0
        maxlength_name = ''
        sentences_count = 0
        minlength = float('INF')
        minlength_name = ''
        dtu = DealtextUtil()
        doc_count = 0
        for path in pathlist:
            files = os.listdir(path)
            for file in files:
                filepath = os.path.join(path, file)
                res = dtu.readdoc(filepath)
                doc_count += len(res)
                for i in res:
                    sentences_count += len(i)
                    if len(i) == 0:
                        res.remove(i)
                    else:
                        maxlength = max(len(i), maxlength)
                        if len(i)==481:
                            print(i)
                        minlength = min(len(i), minlength)
                        if len(i)==1:
                            print(i)
        print('longest', maxlength_name, maxlength)
        print('shortest', minlength_name, minlength)
        print('aver length', sentences_count / doc_count)

    #统计正则匹配的准确率
    def zishou_auc(self,pathlist):
        dtu=DealtextUtil()
        cextract=Content()
        filecount=0
        flag=1
        tptn=0
        for path in pathlist:
            files = os.listdir(path)
            filecount+=len(files)

            for file in files:
                filepath = os.path.join(path, file)
                text=dtu.readtext(filepath)
                zs,tb=cextract.judge_zs(text)
                if zs==flag:
                    tptn+=1
            flag -= 1
        print('auc',(tptn/filecount))


    #统计是否还清欠款正则匹配的准确率
    def pc_auc(self,pathlist):
        dtu=DealtextUtil()
        cextract=Content()
        filecount=0
        flag=1
        tptn=0
        for path in pathlist:
            files = os.listdir(path)
            filecount+=len(files)

            for file in files:
                filepath = os.path.join(path, file)
                text=dtu.readtext(filepath)
                pc=cextract.judge_pcbyre(text)
                if pc==flag:
                    tptn+=1
            flag -= 1
        print('auc',(tptn/filecount))