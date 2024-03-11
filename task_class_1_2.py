'''
2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне. 
Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями. 
Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. Написать программу, демонстрирующую все возможности класса.
'''

class DecimalCounter:
    def __init__(self, minimum=0, maximum=10, initial_value=None):
        self.minimum = minimum
        self.maximum = maximum
        if initial_value is not None:
            self._value = self._validate_value(initial_value)
        else:
            self._value = self.minimum

    def _validate_value(self, value):
        return max(self.minimum, min(value, self.maximum))

    @property
    def current_value(self):
        return self._value

    def increment(self):
        self._value = self._validate_value(self._value + 1)

    def decrement(self):
        self._value = self._validate_value(self._value - 1)

counter1 = DecimalCounter() 
print(f"Initial value: {counter1.current_value}")

counter1.increment()
print(f"After increment: {counter1.current_value}")

counter1.decrement()
print(f"After decrement: {counter1.current_value}")

counter2 = DecimalCounter(minimum=-5, maximum=5, initial_value=2)
print(f"Custom counter value: {counter2.current_value}")

counter2.increment()
print(f"After increment: {counter2.current_value}")

counter2.decrement()
print(f"After decrement: {counter2.current_value}")