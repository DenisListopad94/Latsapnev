'''
1.	Создать класс c двумя переменными. 
Добавить функцию вывода на экран и функцию изменения этих переменных. 
Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит наибольшее значение из этих двух переменных.
'''

class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display_variables(self):
        print(f"Variable 1: {self.var1}")
        print(f"Variable 2: {self.var2}")

    def modify_variables(self, new_var1, new_var2):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_of_variables(self):
        return self.var1 + self.var2

    def max_variable(self):
        return max(self.var1, self.var2)

my_object = MyClass(3, 7)
my_object.display_variables()

my_object.modify_variables(5, 10)
my_object.display_variables()

sum_result = my_object.sum_of_variables()
max_result = my_object.max_variable()

print(f"Sum of variables: {sum_result}")
print(f"Maximum variable: {max_result}")