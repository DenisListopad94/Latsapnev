'''
4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. 
'''

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins_inside = 0

    def can_add(self, v):
        return self.coins_inside + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins_inside += v
            print(f"Added {v} coins to the money box. Total coins inside: {self.coins_inside}")
        else:
            print(f"Cannot add {v} coins. Exceeds the capacity of the money box.")

money_box = MoneyBox(20)
v1 = 5
if money_box.can_add(v1):
    money_box.add(v1)

v2 = 10
if money_box.can_add(v2):
    money_box.add(v2)

v3 = 8
if money_box.can_add(v3):
    money_box.add(v3)

print(f"Current coins inside: {money_box.coins_inside}")
