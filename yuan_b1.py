class SimulateSaving():
    def __init__(self, totalCost = 1000000, portionDownPayment = 0.25, interestRate = 0.04, annualSalary = 120000) -> None:
        self.fisrtCost = float(totalCost) * float(portionDownPayment)
        self.interestRate = float(interestRate)
        self.annualSalary = float(annualSalary)
        self.currentSavings = float(0)
        self.monthlySalary = float(self.annualSalary/12)
    
    def simulate(self, portionSavings = 0.1) -> int:
        monthToSave = 0
        while self.currentSavings < self.fisrtCost:
            self.currentSavings *= 1 + self.interestRate/12
            self.currentSavings += self.monthlySalary * portionSavings            
            monthToSave += 1
        return monthToSave

totalCost_ = input("totalCost:")
annualSalary_ = input("annualSalary:")
portionSavings_ = float(input("portionSavings:"))
interestRate_ = input("interestRate:")

me = SimulateSaving(totalCost = totalCost_, interestRate = interestRate_, annualSalary = annualSalary_)
print(me.simulate(portionSavings_))