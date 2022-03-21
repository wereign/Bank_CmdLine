class handler:
    def writer(obj,file):
        import pickle
        op = open(file,'wb')
        pickle.dump(obj,op)
        op.close()
    def reader(file):
        import  pickle
        re = open(file,'rb')
        data = pickle.load(re)
        re.close()
        return data