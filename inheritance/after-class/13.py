import random
class Arrays():
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_row(array):
        print(",".join(map(str, array)))
    @staticmethod
    def createIndenticalArr(numOfElements, value):
        newArr = []
        for i in range(numOfElements):
            newArr.append(value)
        return newArr
    @staticmethod    
    def createRandomArr(numOfElements, beginning, ending):
        newArr = []
        for i in range(numOfElements):
            newArr.append(random.randint(beginning, ending))
        return newArr
    @staticmethod    
    def calcInRange(array, beginning, ending):
        counter = 0
        for num in array:
            if num in range(beginning, ending+1):
                counter += 1
        return counter
    

            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.print_in_row(my_array)

tenElArray = Arrays.createIndenticalArr(10, 4)
twentyElArray = Arrays.createRandomArr(20, 7,8)
Arrays.print_in_row(tenElArray)
Arrays.print_in_row(twentyElArray)
print(Arrays.calcInRange(twentyElArray, 1, 1))