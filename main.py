from  deal_doc import DealtextUtil
from  w2vec import w2vec
from StatisticsUtil import StatisticsUtil
if __name__=='__main__':
    ##获取词向量
    dtu=DealtextUtil()
    path='D:\\南京大学\\天津方面事务\\自动文本分类\\数据记录\\newdata\\退款\\pc_0.docx'
    # res=dtu.readdoc(path)
    # for i in res:
    #     print(i)
    # for i in res:
    #     if len(i)==0:
    #         res.remove(i)
    w=w2vec()
    a=w.pa2vec(path)
    # matrix=w.w2v(res)
    # print(matrix.shape)

    #统计句子长度
    # pathlist=['D:\\南京大学\\天津方面事务\\自动文本分类\\数据记录\\newdata\\退款','D:\\南京大学\\天津方面事务\\自动文本分类\\数据记录\\newdata\\未退款']
    # su=StatisticsUtil()
    # # su.get_longsentence(pathlist)
    # su.statistics_word(pathlist)

    # #统计自首率：
    # pathlist=['D:\\南京大学\\天津方面事务\\自动文本分类\\数据记录\\自首or非自首\\自首','D:\\南京大学\\天津方面事务\\自动文本分类\\数据记录\\自首or非自首\\非自首']
    # su=StatisticsUtil()
    # su.zishou_rate(pathlist)

    #统计赔偿准确率
    # pathlist = ['D:\\南京大学\\天津方面事务\\自动文本分类\\数据记录\\newdata\\退款', 'D:\\南京大学\\天津方面事务\\自动文本分类\\数据记录\\newdata\\未退款']
    # su=StatisticsUtil()
    # su.pc_auc(pathlist)
