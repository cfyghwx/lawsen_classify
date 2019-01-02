import gensim
import numpy as np


def get_model():
    model = gensim.models.Word2Vec.load('D:\\pycharm\\wordvec\\zh.bin')
    return model

 # 返回一个词 的向量：
if __name__=='__main__':
    model=get_model()
    a=model['我']
    b=model['吃饭']
    a=np.array(a).reshape(1,300)
    b=np.array(b)
    c=a+b
    print(c.shape)