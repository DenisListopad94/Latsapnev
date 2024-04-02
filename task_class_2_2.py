class Transporter:
    def __init__(self, name, speed, cost_per_km):
        self.name = name
        self.speed = speed
        self.cost_per_km = cost_per_km
    
    def calculate_time(self, distance):
        return distance / self.speed
    
    def calculate_cost(self, distance):
        return distance * self.cost_per_km

class Airplane(Transporter):
    def __init__(self):
        super().__init__("Самолет", 800, 5)

class Train(Transporter):
    def __init__(self):
        super().__init__("Поезд", 120, 2)

class Car(Transporter):
    def __init__(self):
        super().__init__("Автомобиль", 100, 3)

def calculate_transport(transporter, distance):
    time = transporter.calculate_time(distance)
    cost = transporter.calculate_cost(distance)
    return time, cost

if __name__ == "__main__":
    distance = 500 

    airplane = Airplane()
    train = Train()
    car = Car()

    time_airplane, cost_airplane = calculate_transport(airplane, distance)
    time_train, cost_train = calculate_transport(train, distance)
    time_car, cost_car = calculate_transport(car, distance)

    print(f"Самолет: Время - {time_airplane:.2f} ч, Стоимость - {cost_airplane:.2f} у.е.")
    print(f"Поезд: Время - {time_train:.2f} ч, Стоимость - {cost_train:.2f} у.е.")
    print(f"Автомобиль: Время - {time_car:.2f} ч, Стоимость - {cost_car:.2f} у.е.")