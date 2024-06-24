class Kendaraan:
    def __init__(self, nama):
        self.nama = nama

    def hitung_biaya(self, jarak):
        pass

class Mobil(Kendaraan):
    def __init__(self, nama, konsumsi_bahan_bakar_per_km, harga_bahan_bakar_per_liter):
        super().__init__(nama)
        self.konsumsi_bahan_bakar_per_km = konsumsi_bahan_bakar_per_km
        self.harga_bahan_bakar_per_liter = harga_bahan_bakar_per_liter

    def hitung_biaya(self, jarak):
        biaya = jarak * self.konsumsi_bahan_bakar_per_km * self.harga_bahan_bakar_per_liter
        return biaya

class Motor(Kendaraan):
    def __init__(self, nama, konsumsi_bahan_bakar_per_km, harga_bahan_bakar_per_liter):
        super().__init__(nama)
        self.konsumsi_bahan_bakar_per_km = konsumsi_bahan_bakar_per_km
        self.harga_bahan_bakar_per_liter = harga_bahan_bakar_per_liter

    def hitung_biaya(self, jarak):
        biaya = jarak * self.konsumsi_bahan_bakar_per_km * self.harga_bahan_bakar_per_liter
        return biaya

class MobilListrik(Kendaraan):
    def __init__(self, nama, konsumsi_listrik_per_km, harga_listrik_per_kwh):
        super().__init__(nama)
        self.konsumsi_listrik_per_km = konsumsi_listrik_per_km
        self.harga_listrik_per_kwh = harga_listrik_per_kwh

    def hitung_biaya(self, jarak):
        biaya = jarak * self.konsumsi_listrik_per_km * self.harga_listrik_per_kwh
        return biaya

def kalkulasi_biaya_perjalanan(kendaraan, jarak):
    print(f"Biaya perjalanan dengan {kendaraan.nama} untuk jarak {jarak} km adalah: {kendaraan.hitung_biaya(jarak)}")

# Membuat objek dari kelas Mobil, Motor, dan MobilListrik
mobil = Mobil("Toyota Avanza", 0.12, 9000)
motor = Motor("Honda Vario", 0.05, 9000)
mobil_listrik = MobilListrik("Tesla Model 3", 0.2, 1500)

# Menunjukkan polimorfisme
kalkulasi_biaya_perjalanan(mobil, 100)         # Output: Biaya perjalanan dengan Toyota Avanza untuk jarak 100 km adalah: 108000.0
kalkulasi_biaya_perjalanan(motor, 100)         # Output: Biaya perjalanan dengan Honda Vario untuk jarak 100 km adalah: 45000.0
kalkulasi_biaya_perjalanan(mobil_listrik, 100) # Output: Biaya perjalanan dengan Tesla Model 3 untuk jarak 100 km adalah: 30000.0
