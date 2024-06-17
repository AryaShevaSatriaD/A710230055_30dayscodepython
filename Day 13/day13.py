class employee:
    def __init__(self, name, age, gaji):
        self.__name = name
        self.__age = age
        self.__gaji = gaji

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def get_gaji(self):
        return self.__gaji
    
    def set_gaji(self, gaji):
        self.__gaji = gaji

employee1 = employee("Raju", 20, 100000)
print(employee1.get_name())
print(employee1.get_age())
print(employee1.get_gaji())
print()
employee1.set_name("Ijat")
employee1.set_age(22)
employee1.set_gaji(200000)
print(employee1.get_name())
print(employee1.get_age())
print(employee1.get_gaji())