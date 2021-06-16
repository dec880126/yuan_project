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
        
#publish object
search = SearchSavingsRate()

#Parameter
monthsToSave = 36

#Simulating
search.binarySearch(monthsToSave)

#Monitor
print(f"在{monthsToSave}個月存到頭期款所需的存款比率為{search.binarySearch(): 1.4f}")