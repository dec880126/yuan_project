class SimulateSaving():
    def __init__(self, totalCost = 1000000, portionDownPayment = 0.25, interestRate = 0.04, annualSalary = 120000,):
        """
        type totalCost: int
        type portionDownPayment: float
        type interestRate: float
        type annualSalary: int
        """   
        self.totalCost = int(totalCost)
        self.portionDownPayment = float(portionDownPayment)
        self.interestRate = float(interestRate)
        self.annualSalary = int(annualSalary)
    
    def simulate(self, portionSavings = 0.1) -> int:
        """
        type portionSavings: float
        rtype: int
        """
        monthToSave = 0
        currentSavings = 0.0
        monthlySalary = self.annualSalary/12
        fisrtCost = self.totalCost * self.portionDownPayment
        while currentSavings < fisrtCost:
            currentSavings *= 1 + self.interestRate/12              # interest of the money
            currentSavings += monthlySalary * portionSavings        # save money by parameter: portionSavings
            monthToSave += 1
        return monthToSave

class SearchSavingsRate(SimulateSaving):        
    def binarySearch(self, monthsToSave = 36):
        """
        type monthsToSave: int
        rtype: float
        """
        portionSavings = 0.0005                                     
        # portionSavings starts with 0.0005, because the question said that the
        # accuracy is allowed to 3 digits after decimal points
        month = 0
        while month != monthsToSave:                                # keep trying until the number of month has been tried equal to parameter: monthsToSave
            month = super().simulate(portionSavings)                # super(): use the function that defined in mother's class
            portionSavings += 0.0005                                # increase the portionSavings by 0.0005
        return portionSavings

class SearchSavingsRateWRaise(SearchSavingsRate):
    def simulate(self, portionSavings = 0.1) -> int:
        """
        type portionSavings: float
        rtype: int
        """
        semiAnnualRaise = 0.1
        raisePeriod = 6

        monthToSave = 0
        currentSavings = 0.0
        monthlySalary = self.annualSalary/12
        fisrtCost = self.totalCost * self.portionDownPayment
        print(f"{monthlySalary=:1.0f}")
        while currentSavings < fisrtCost:
            print(f"今は第{monthToSave}月                           預金は{currentSavings:.1f}円")
            if (monthToSave%raisePeriod) == 0 and monthToSave != 0:
                monthlySalary *= 1 + semiAnnualRaise
                print(f"    昇給！ -> 今の月収は{monthlySalary:1.0f}") 
            currentSavings *= 1 + self.interestRate/12              # interest of the money
            currentSavings += monthlySalary * portionSavings        # save money by parameter: portionSavings
            monthToSave += 1
        return monthToSave
        
        
#publish object
search = SearchSavingsRateWRaise()

#Parameter
# monthsToSave = 36

#Simulating
output = search.simulate()

#Monitor
# print(f"在{monthsToSave}個月存到頭期款所需的存款比率為{search.binarySearch(): 1.4f}")

print(output)