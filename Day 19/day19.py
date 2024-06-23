# Kelas dasar (parent class)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def description(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Kelas turunan (child class)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def description(self):
        return f"Mobil {self.brand} {self.model} dengan {self.doors} pintu."

class Bicycle(Vehicle):
    def __init__(self, brand, model, gear_count):
        super().__init__(brand, model)
        self.gear_count = gear_count
    
    def description(self):
        return f"Sepeda {self.brand} {self.model} dengan {self.gear_count} gigi."

class Boat(Vehicle):
    def __init__(self, brand, model, boat_type):
        super().__init__(brand, model)
        self.boat_type = boat_type
    
    def description(self):
        return f"Perahu {self.brand} {self.model} tipe {self.boat_type}."

# Membuat objek dari kelas turunan
car = Car("Toyota", "Corolla", 4)
bicycle = Bicycle("Trek", "Domane", 21)
boat = Boat("Yamaha", "242X", "speedboat")

# Menggunakan metode dari kelas turunan
car.info()
print(car.description())

bicycle.info()
print(bicycle.description())

boat.info()
print(boat.description())
