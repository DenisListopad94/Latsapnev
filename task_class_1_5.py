'''
1.	Создайте класс fraction. 
Данные класса должны быть представлены двумя полями: числителем и знаменателем. 
Методы класса должны получать от пользователя значения числителя и знаменателя дроби и выводить значение дроби в форме 3/5. 
Кроме того, должен быть разработан метод, складывающий значения двух дробей и метод для сокращения дробей.
'''

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def input_fraction(self):
        self.numerator = int(input("Enter the numerator: "))
        while True:
            self.denominator = int(input("Enter the denominator: "))
            if self.denominator != 0:
                break
            else:
                print("Denominator cannot be zero. Please enter a valid denominator.")

    def display_fraction(self):
        print(f"{self.numerator}/{self.denominator}")

    def add_fraction(self, other_fraction):
        result_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        result_denominator = self.denominator * other_fraction.denominator
        return Fraction(result_numerator, result_denominator)

    def reduce_fraction(self):
        common_divisor = self.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a


fraction1 = Fraction()
fraction1.input_fraction()

fraction2 = Fraction()
fraction2.input_fraction()

print("\nFraction 1:")
fraction1.display_fraction()
print("\nFraction 2:")
fraction2.display_fraction()

sum_result = fraction1.add_fraction(fraction2)
print("\nSum of fractions:")
sum_result.display_fraction()

print("\nSimplified sum:")
sum_result.reduce_fraction()
sum_result.display_fraction()