def generator_chunks(iterator,recordSizeLimit):
    for index in range(0,len(iterator),recordSizeLimit):
       print(iterator[index:index+recordSizeLimit])
        
if __name__ == "__main__":
    list1=[f"check{index}" for index in range(100)] 
    generator_chunks(list1,3)