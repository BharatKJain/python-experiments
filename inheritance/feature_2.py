from feature_1 import B,A

class C(A,B):
    # def __init__(self):
    #     super().__init__()
    def check(self):
        print("hello")
        self.sampleData+=1
        print(self.sampleData)
        # self.tearDown()
        # print(self.sample/Data)
objectMain=C()
objectMain.check()