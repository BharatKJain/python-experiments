import pandas

def testingFunction(inputStr:pandas.DataFrame)-> list:
    return inputStr.split(",")

def testingFunction2(inputStr:int)-> list:
    return inputStr.split(",")

if __name__=="__main__":
    # reponse=testingFunction2("check,help")

    response=testingFunction("check,help")

    print(response)