import exceptions
import engine
from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print('Engine started')
            else:
                raise exceptions.LowFuelError('Not enought fuel for start')
        else:
            print('Already started')

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel = self.fuel - required_fuel
            print(f'Moved on {distance} successfully')
        else:
            raise exceptions.NotEnoughFuel(f'Not enought fuel for moving on {distance}')

class Car(Vehicle):
    def __init__(self, weight=500, fuel=200, fuel_consumption=5):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine
        print('Engine loaded succefully')

class Plane(Vehicle):
    def __init__(self, weight=50000, fuel=2000, fuel_consumption=100, max_cargo=10000):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        new_cargo = self.cargo + int(amount)
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
            print(f'Loaded {amount} cargo. Total cargo: {self.cargo}')
        else:
            raise exceptions.CargoOverload(f'Too much cargo: {new_cargo}')

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        print(f'Unloaded {removed_cargo} cargo. Total cargo: {self.cargo}')
        return removed_cargo

# Создание engine
engine = engine.Engine(2,4)

def main():
    choice = input('Do you want to create a Car or a Plane? (C/P): ').upper()

    if choice == 'C':
        car = Car()
        distance = int(input('Enter the distance for your car to travel: '))
        car.set_engine(engine)
        car.start()
        car.move(distance)

    elif choice == 'P':
        plane = Plane()
        cargo_amount = int(input('Enter amount of cargo to load: '))
        plane.load_cargo(cargo_amount)

if __name__ == "__main__":
    main()