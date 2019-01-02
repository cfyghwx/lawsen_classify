from deal_doc import DealtextUtil
from get_model import get_model
import numpy as np

#将文本转化为向量，
class w2vec(object):
    #一句转化为一个向量
    def w2v(self,array):
        vecmatrix=[]
        model=get_model()
        for i in array:
            vec=np.zeros((1,300))
            for j in i:
                try:
                    vec_j=model[j]
                except:
                    # vec_j=np.zeros((1,300))
                    vec_j=np.random.uniform(-0.25,0.25,300)
                vec_j=np.array(vec_j)
                vec+=vec_j
            vec=vec/len(i)
            vecmatrix.append(vec)
        vecmatrix=np.array(vecmatrix).reshape(-1,300)
        docvec=np.zeros((1,300))
        for i in vecmatrix:
            docvec+=i
        docvec=docvec/len(vecmatrix)
        # return vecmatrix
        return docvec

    def pa2vec(self,path):
        dtu = DealtextUtil()
        array=dtu.readdoc_word(path)
        matrix=[]
        model = get_model()
        for i in array:
            try:
                vec=model[i]
            except:
                vec = np.random.uniform(-0.1, 0.1, 300)
            matrix.append(vec)
        matrix=np.array(matrix)
        print(matrix.shape)
        return matrix


