class Employee:

    def __init__(self, name, surname, salary):
        """Класс представляющий работника"""
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self, surcharge=5000):
        self.salary += surcharge
