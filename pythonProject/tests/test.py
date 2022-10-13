from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 4, 5) == 20

    def test_division_success(self):
        assert self.calculator.division(self, 100, 2) == 50

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 6, 2) == 4