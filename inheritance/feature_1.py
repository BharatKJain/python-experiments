class A:
    def __init__(self):
        self.sampleData=10
        print("check")
    def tearDown(self):
        print(f"{self.sampleData}")

class B:
    def __init__(self):
        self.sampleData=2
    def setUp_B(self):
        self.sampleData=2
        print("check")
    def tearDown_B(self):
        print("kkkk")

class C(A):
    # def __init__(self):
    #     super().__init__()
    def check(self):
        print("hello")
        self.sampleData+=1
        self.tearDown()
        # print(self.sampleData)
        # self.tearDown()
        # print(self.sample/Data)
objectMain=C()
objectMain.check()