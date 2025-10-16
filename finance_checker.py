"""
Finance Checker - A simple tool to track budgets and validate expenses.
"""


class FinanceChecker:
    """A class to manage budget tracking and expense validation."""
    
    def __init__(self, monthly_budget=0):
        """
        Initialize the Finance Checker.
        
        Args:
            monthly_budget (float): The total monthly budget
        """
        self.monthly_budget = monthly_budget
        self.expenses = []
        self.categories = {}
    
    def set_budget(self, amount):
        """
        Set the monthly budget.
        
        Args:
            amount (float): The budget amount
        """
        if amount < 0:
            raise ValueError("Budget cannot be negative")
        self.monthly_budget = amount
    
    def add_expense(self, description, amount, category="General"):
        """
        Add an expense to the tracker.
        
        Args:
            description (str): Description of the expense
            amount (float): Amount spent
            category (str): Category of the expense
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative")
        
        expense = {
            "description": description,
            "amount": amount,
            "category": category
        }
        self.expenses.append(expense)
        
        # Update category totals
        if category not in self.categories:
            self.categories[category] = 0
        self.categories[category] += amount
    
    def get_total_expenses(self):
        """
        Calculate total expenses.
        
        Returns:
            float: Total amount of all expenses
        """
        return sum(expense["amount"] for expense in self.expenses)
    
    def get_remaining_budget(self):
        """
        Calculate remaining budget.
        
        Returns:
            float: Remaining budget after expenses
        """
        return self.monthly_budget - self.get_total_expenses()
    
    def is_over_budget(self):
        """
        Check if expenses exceed the budget.
        
        Returns:
            bool: True if over budget, False otherwise
        """
        return self.get_total_expenses() > self.monthly_budget
    
    def get_category_breakdown(self):
        """
        Get spending breakdown by category.
        
        Returns:
            dict: Dictionary of categories and their total spending
        """
        return self.categories.copy()
    
    def get_budget_status(self):
        """
        Get a detailed budget status report.
        
        Returns:
            dict: Dictionary containing budget status information
        """
        total_expenses = self.get_total_expenses()
        remaining = self.get_remaining_budget()
        percentage_used = ((total_expenses / self.monthly_budget) * 100) if self.monthly_budget > 0 else 0
        
        return {
            "monthly_budget": self.monthly_budget,
            "total_expenses": total_expenses,
            "remaining_budget": remaining,
            "percentage_used": round(percentage_used, 2),
            "over_budget": self.is_over_budget(),
            "number_of_expenses": len(self.expenses),
            "category_breakdown": self.get_category_breakdown()
        }
    
    def clear_expenses(self):
        """Clear all expenses and reset categories."""
        self.expenses = []
        self.categories = {}


def main():
    """Example usage of the Finance Checker."""
    print("Finance Checker - Budget Tracking Tool\n")
    
    # Create a finance checker with a $2000 monthly budget
    checker = FinanceChecker(monthly_budget=2000)
    
    # Add some expenses
    checker.add_expense("Groceries", 150, "Food")
    checker.add_expense("Rent", 800, "Housing")
    checker.add_expense("Electric bill", 75, "Utilities")
    checker.add_expense("Internet", 60, "Utilities")
    checker.add_expense("Restaurant", 45, "Food")
    checker.add_expense("Gas", 50, "Transportation")
    
    # Get budget status
    status = checker.get_budget_status()
    
    print(f"Monthly Budget: ${status['monthly_budget']:.2f}")
    print(f"Total Expenses: ${status['total_expenses']:.2f}")
    print(f"Remaining Budget: ${status['remaining_budget']:.2f}")
    print(f"Budget Used: {status['percentage_used']:.2f}%")
    print(f"Over Budget: {status['over_budget']}")
    print(f"\nExpense Breakdown by Category:")
    for category, amount in status['category_breakdown'].items():
        print(f"  {category}: ${amount:.2f}")


if __name__ == "__main__":
    main()
