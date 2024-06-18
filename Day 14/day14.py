class Mobil:
    def move(self):
        print("berjalan di jalan raya")

class Pesawat:
    def move(self):
        print("Terbabng di udara")

class kapal:
    def move(self):
        print("Berlayar di laut")

v1 = Mobil()
v2 = Pesawat()
v3 = kapal()
for vehicle in (v1,v2,v3):
    vehicle.move()

