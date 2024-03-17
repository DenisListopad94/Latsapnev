class LivingBeing:
    def __init__(self, age_limit):
        self.age = 0
        self.age_limit = age_limit
        self.alive = True

    def eat(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def is_alive(self, food_available=True):
        if self.age >= self.age_limit or not food_available:
            self.alive = False
        return self.alive

class Fox(LivingBeing):
    def __init__(self):
        super().__init__(5)

    def eat(self, food):
        if isinstance(food, Rabbit):
            return True
        return False

class Rabbit(LivingBeing):
    def __init__(self):
        super().__init__(3)

    def eat(self, food):
        if isinstance(food, Plant):
            return True
        return False

class Plant(LivingBeing):
    def __init__(self):
        super().__init__(10)

    def eat(self):
        return True

if __name__ == "__main__":
    fox = Fox()
    rabbit = Rabbit()
    plant = Plant()

    print("Fox eats rabbit:", fox.eat(rabbit))
    print("Rabbit eats plant:", rabbit.eat(plant))
    print("Plant eats sunlight:", plant.eat())

    print("Fox is alive:", fox.is_alive())
    print("Rabbit is alive:", rabbit.is_alive())
    print("Plant is alive:", plant.is_alive(food_available=False))