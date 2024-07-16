
# Question Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget.
class BudgetCategory:
    def __init__(self,category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
    def get_category_name(self):
        return self.__category_name
    def set_category_name(self, category_name):
        self.__category_name = category_name
    def get_allocated_budget(self):
        return self.__allocated_budget
    def set_allocated_budget(self, allocated_budget):
        self.__allocated_budget = allocated_budget
if __name__ == "__main__":
   
   food_category = BudgetCategory("Food", 400 )
   print(f"Category: {food_category.get_category_name()}, Budget: {food_category.get_allocated_budget()}")
   food_category.set_allocated_budget(500)
   print(f"Updated Budget: {food_category.get_allocated_budget()}")

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. 
class BudgetCategory:
    def __init__(self,category_name, allocated_budget):
     self._category_name = category_name
     self._allocated_budget = allocated_budget
    @property
    def category_name(self):
            return self._category_name
    @category_name.setter
    def category_name(self,value):
        if not value:
            raise ValueError("Category name cannot be empty.")
        self._category_name = value
    @property
    def allocated_budget(self):
        return self._allocated_budget
    @allocated_budget.setter
    def allocated_budget(self,value):
        if value <= 0:
            raise ValueError("Allocated budget must be a positive number.")
        self.__allocated_budget = value
try:
    budget = BudgetCategory("Groceries", 400)
    print(budget.category_name)
    print(budget.allocated_budget)

    budget.category_name = "Utilities"
    budget.allocated_budget = 230
    print(budget.category_name)
    print(budget.allocated_budget)
    budget.allocated_budget = -200
except ValueError as e:
    print(e)

# Task 3: Add Budget Functionality.
class Budget:
    def __init__(self, total_budget):
        self.total_budget = total_budget
        self.categories = {}

    def add_category(self, category_name, category_budget):
        if category_name in self.categories:
            print(f"Category '{category_name}' already exists.")
        else:
            self.categories[category_name] = {
                'budget': category_budget,
                'expenses': 0
            }
            print(f"Category '{category_name}' added with a budget of {category_budget}.")

    def add_expense(self, category_name, expense_amount):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist.")
            return

        if expense_amount <= 0:
            print("Expense amount must be greater than zero.")
            return

        category = self.categories[category_name]
        if expense_amount > (category['budget'] - category['expenses']):
            print(f"Not enough budget in category '{category_name}' to cover this expense.")
        else:
            category['expenses'] += expense_amount
            print(f"Added expense of {expense_amount} to category '{category_name}'.")

    def get_remaining_budget(self, category_name):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist.")
            return None

        category = self.categories[category_name]
        remaining_budget = category['budget'] - category['expenses']
        return remaining_budget

    def get_total_remaining_budget(self):
        total_expenses = sum(category['expenses'] for category in self.categories.values())
        return self.total_budget - total_expenses
    
budget = Budget(1000)
budget.add_category("Food", 300)
budget.add_category("Entertainment", 200)
budget.add_expense("Food", 50)
budget.add_expense("Entertainment", 100)

print(f"Remaining budget for Food: {budget.get_remaining_budget('Food')}")
print(f"Remaining budget for Entertainment: {budget.get_remaining_budget('Entertainment')}")
print(f"Total remaining budget: {budget.get_total_remaining_budget()}")

# Task 4:Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.name = name
        self.allocated_budget = allocated_budget
        self.expenses = 0

    def add_expense(self, amount):
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.expenses += amount

    def remaining_budget(self):
        return self.allocated_budget - self.expenses
    
    def display_details(self):
        print(f"Budget Category: {self.name}")
        print(f"Allocated budget: ${self.allocated_budget:.2f}")
        print(f"Expenses: ${self.expenses:.2f}")
        print(f"Remaining Budget: ${self.remaining_budget():.2f}")

food_budget = BudgetCategory("Food", 600)
food_budget.add_expense(400)
food_budget.add_expense(250)
food_budget.display_details()
    

    
    





