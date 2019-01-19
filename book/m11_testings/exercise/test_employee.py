import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.salary = 100000
        self.employee = Employee('alex', 'fisher', self.salary)

    def test_give_default_raise(self):
        salary = self.employee.salary
        self.employee.give_raise()

        self.assertEqual(self.employee.salary, salary + 5000)

    def test_give_custom_raise(self):
        surcharge = 6000
        salary = self.employee.salary
        self.employee.give_raise(surcharge)

        self.assertEqual(self.employee.salary, salary + surcharge)
