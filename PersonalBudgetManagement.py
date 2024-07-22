# Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., 
# ensuring that budget details remain private and are accessed or modified through public methods.

class BudgetCategory:
    def __init__(self, categoryName, allocatedBudget):
        self.__categoryName = categoryName
        self.__allocatedBudget = allocatedBudget
        self.__remainingBudget = allocatedBudget

    def getCategoryName(self):
        return self.__categoryName

    def setCategoryName(self, newName):
        self.__categoryName = newName

    def getAllocatedBudget(self):
        return self.__allocatedBudget

    def setAllocatedBudget(self, newBudget):
        if newBudget >= 0:
            self.__allocatedBudget = newBudget
        else:
            print("Budget should be  positive.")

    def addExpense(self, amount):
        if amount >= 0:
            if amount <= self.__remainingBudget:
                self.__remainingBudget -= amount
                print(f"${amount} expense added to {self.__categoryName} category.")
            else:
                print("Expense exceeds remaining budget.")
        else:
            print("Expense should be a positive number.")

    def displayCategorySummary(self):
        print("Category:", self.__categoryName)
        print("Allocated Budget: $", self.__allocatedBudget)
        print("Remaining Budget: $", self.__remainingBudget)


if __name__ == "__main__":
    foodCategory = BudgetCategory("Food", 500)
    foodCategory.addExpense(100)
    foodCategory.displayCategorySummary()
