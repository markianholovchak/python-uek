class Statistics():
    def __init__(self):
        self.set = []
        self.max = None
        self.max = None
        self.arithmMean = None
        self.median = None
    def displaySet(self):
        print(", ".join(map(str, self.set)))
    def addToSet(self):
        self.set.append(int(input("Enter the num to be added to the set: ")))
    def calcMax(self):
        self.max = max(self.set)
    def calcMin(self):
        self.min = min(self.set)
    def calcArithmeticMean(self):
        self.arithmMean = round(sum(self.set) / len(self.set), 2)
    def calcMediam(self):
        sortedArr = sorted(self.set)
        if len(self.set) % 2 == 0:
            self.median = (sortedArr[len(sortedArr) // 2] + sortedArr[len(sortedArr) // 2 + 1]) / 2
        else:
            self.median = sortedArr[len(sortedArr) // 2]

    def displayValues(self):
        print(f"Min: {self.min} Max: {self.max} Arithm Mean: {self.arithmMean}, Median: {self.median}")

newStat = Statistics()
newStat.addToSet()
newStat.addToSet()
newStat.addToSet()
newStat.displaySet()
newStat.calcMax()
newStat.calcMin()
newStat.calcArithmeticMean()
newStat.calcMediam()
newStat.displayValues()