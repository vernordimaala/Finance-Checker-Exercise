"""
Tests for the Finance Checker module.
"""

import unittest
from finance_checker import FinanceChecker


class TestFinanceChecker(unittest.TestCase):
    """Test cases for the FinanceChecker class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.checker = FinanceChecker(monthly_budget=1000)
    
    def test_initialization(self):
        """Test that FinanceChecker initializes correctly."""
        self.assertEqual(self.checker.monthly_budget, 1000)
        self.assertEqual(len(self.checker.expenses), 0)
        self.assertEqual(len(self.checker.categories), 0)
    
    def test_set_budget(self):
        """Test setting the budget."""
        self.checker.set_budget(1500)
        self.assertEqual(self.checker.monthly_budget, 1500)
    
    def test_set_negative_budget_raises_error(self):
        """Test that setting a negative budget raises an error."""
        with self.assertRaises(ValueError):
            self.checker.set_budget(-100)
    
    def test_add_expense(self):
        """Test adding an expense."""
        self.checker.add_expense("Groceries", 50, "Food")
        self.assertEqual(len(self.checker.expenses), 1)
        self.assertEqual(self.checker.expenses[0]["description"], "Groceries")
        self.assertEqual(self.checker.expenses[0]["amount"], 50)
        self.assertEqual(self.checker.expenses[0]["category"], "Food")
    
    def test_add_negative_expense_raises_error(self):
        """Test that adding a negative expense raises an error."""
        with self.assertRaises(ValueError):
            self.checker.add_expense("Invalid", -50, "Food")
    
    def test_add_multiple_expenses(self):
        """Test adding multiple expenses."""
        self.checker.add_expense("Groceries", 50, "Food")
        self.checker.add_expense("Rent", 500, "Housing")
        self.checker.add_expense("Gas", 30, "Transportation")
        self.assertEqual(len(self.checker.expenses), 3)
    
    def test_get_total_expenses(self):
        """Test calculating total expenses."""
        self.checker.add_expense("Groceries", 50, "Food")
        self.checker.add_expense("Rent", 500, "Housing")
        self.checker.add_expense("Gas", 30, "Transportation")
        self.assertEqual(self.checker.get_total_expenses(), 580)
    
    def test_get_total_expenses_empty(self):
        """Test total expenses when no expenses are added."""
        self.assertEqual(self.checker.get_total_expenses(), 0)
    
    def test_get_remaining_budget(self):
        """Test calculating remaining budget."""
        self.checker.add_expense("Groceries", 200, "Food")
        self.assertEqual(self.checker.get_remaining_budget(), 800)
    
    def test_is_over_budget_false(self):
        """Test is_over_budget when under budget."""
        self.checker.add_expense("Groceries", 200, "Food")
        self.assertFalse(self.checker.is_over_budget())
    
    def test_is_over_budget_true(self):
        """Test is_over_budget when over budget."""
        self.checker.add_expense("Rent", 1200, "Housing")
        self.assertTrue(self.checker.is_over_budget())
    
    def test_is_over_budget_exact(self):
        """Test is_over_budget when exactly at budget."""
        self.checker.add_expense("Expense", 1000, "General")
        self.assertFalse(self.checker.is_over_budget())
    
    def test_get_category_breakdown(self):
        """Test getting category breakdown."""
        self.checker.add_expense("Groceries", 100, "Food")
        self.checker.add_expense("Restaurant", 50, "Food")
        self.checker.add_expense("Rent", 500, "Housing")
        
        breakdown = self.checker.get_category_breakdown()
        self.assertEqual(breakdown["Food"], 150)
        self.assertEqual(breakdown["Housing"], 500)
    
    def test_get_category_breakdown_empty(self):
        """Test category breakdown when no expenses."""
        breakdown = self.checker.get_category_breakdown()
        self.assertEqual(len(breakdown), 0)
    
    def test_get_budget_status(self):
        """Test getting budget status report."""
        self.checker.add_expense("Groceries", 200, "Food")
        self.checker.add_expense("Rent", 500, "Housing")
        
        status = self.checker.get_budget_status()
        self.assertEqual(status["monthly_budget"], 1000)
        self.assertEqual(status["total_expenses"], 700)
        self.assertEqual(status["remaining_budget"], 300)
        self.assertEqual(status["percentage_used"], 70.0)
        self.assertFalse(status["over_budget"])
        self.assertEqual(status["number_of_expenses"], 2)
    
    def test_clear_expenses(self):
        """Test clearing expenses."""
        self.checker.add_expense("Groceries", 100, "Food")
        self.checker.add_expense("Rent", 500, "Housing")
        self.checker.clear_expenses()
        
        self.assertEqual(len(self.checker.expenses), 0)
        self.assertEqual(len(self.checker.categories), 0)
        self.assertEqual(self.checker.get_total_expenses(), 0)
    
    def test_default_category(self):
        """Test that default category is 'General'."""
        self.checker.add_expense("Misc item", 25)
        self.assertEqual(self.checker.expenses[0]["category"], "General")
    
    def test_zero_budget_percentage(self):
        """Test percentage calculation with zero budget."""
        checker_zero = FinanceChecker(monthly_budget=0)
        checker_zero.add_expense("Test", 100, "General")
        status = checker_zero.get_budget_status()
        self.assertEqual(status["percentage_used"], 0)


if __name__ == "__main__":
    unittest.main()
