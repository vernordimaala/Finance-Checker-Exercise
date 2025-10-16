# Finance-Checker-Exercise

A simple Python-based budget tracking and expense validation tool to help manage personal finances.

## Features

- **Budget Management**: Set and track monthly budgets
- **Expense Tracking**: Add and categorize expenses
- **Budget Analysis**: Check if you're over budget
- **Category Breakdown**: View spending by category
- **Detailed Reports**: Get comprehensive budget status reports

## Installation

No external dependencies required! This tool uses only Python standard library.

Requirements:
- Python 3.6 or higher

## Usage

### Quick Start

Run the example demo:
```bash
python finance_checker.py
```

### Using in Your Code

```python
from finance_checker import FinanceChecker

# Create a finance checker with a $2000 monthly budget
checker = FinanceChecker(monthly_budget=2000)

# Add expenses
checker.add_expense("Groceries", 150, "Food")
checker.add_expense("Rent", 800, "Housing")
checker.add_expense("Electric bill", 75, "Utilities")

# Check total expenses
total = checker.get_total_expenses()
print(f"Total expenses: ${total:.2f}")

# Check remaining budget
remaining = checker.get_remaining_budget()
print(f"Remaining budget: ${remaining:.2f}")

# Check if over budget
if checker.is_over_budget():
    print("Warning: You are over budget!")

# Get detailed status report
status = checker.get_budget_status()
print(f"Budget used: {status['percentage_used']:.2f}%")
```

## API Reference

### FinanceChecker Class

#### `__init__(monthly_budget=0)`
Initialize the Finance Checker with an optional monthly budget.

#### `set_budget(amount)`
Set the monthly budget amount.

#### `add_expense(description, amount, category="General")`
Add an expense with a description, amount, and optional category.

#### `get_total_expenses()`
Returns the total amount of all expenses.

#### `get_remaining_budget()`
Returns the remaining budget after expenses.

#### `is_over_budget()`
Returns True if expenses exceed the budget, False otherwise.

#### `get_category_breakdown()`
Returns a dictionary of spending by category.

#### `get_budget_status()`
Returns a comprehensive dictionary with budget status including:
- monthly_budget
- total_expenses
- remaining_budget
- percentage_used
- over_budget
- number_of_expenses
- category_breakdown

#### `clear_expenses()`
Clears all expenses and resets categories.

## Running Tests

Run the test suite:
```bash
python -m unittest test_finance_checker.py -v
```

All tests should pass, validating:
- Budget setting and validation
- Expense adding and tracking
- Budget calculations
- Category management
- Error handling for negative values

## Example Output

```
Finance Checker - Budget Tracking Tool

Monthly Budget: $2000.00
Total Expenses: $1180.00
Remaining Budget: $820.00
Budget Used: 59.00%
Over Budget: False

Expense Breakdown by Category:
  Food: $195.00
  Housing: $800.00
  Utilities: $135.00
  Transportation: $50.00
```

## License

This is an exercise project for testing GitHub Copilot capabilities.