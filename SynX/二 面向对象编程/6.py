#一定要可迭代的对象才可以调用迭代器，所以在定义类的时候要加可迭代的方法
class BatchDataLoader:
    def __init__(self,data,batch_size):
        self.data = data[:]#[]的目的是？
        # 功能是“复制”，不是“列表特色”；写成  list(data)  也能达到同样效果，只是  [:]  更短。
        self.batch_size = batch_size#是为了说明每切一次，每组内要有一定数量的元素
        self.index =0#准备从第0号元素读起

    def __iter__(self):
        self.index = 0#因为这里要迭代，所以要计数，要对自己内部进行初始化
        return self

    def __next__(self):#有次序，所以开始要有index(读到第几个的计数器)
        if self.index >= len(self.data):
            raise StopIteration#叠甲，防止死循环
        batch = self.data[self.index:self.index + self.batch_size]#限定每次输出几个数字
        #!!!记得体现循环，把数往后推进
        self.index += self.batch_size
        return batch
#这里return的作用是明确下次再进__next__函数继续（没想到！！！）
data = list(range(1,21))
for batch in BatchDataLoader(data,6):
    print(batch)