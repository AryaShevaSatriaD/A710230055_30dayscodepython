class Kendaraan:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.tahun} {self.merk} {self.model}"

    def jalankan(self):
        print(f"{self.info_kendaraan()} sedang berjalan.")

class Mobil(Kendaraan):
    def __init__(self, merk, model, tahun, jumlah_pintu):
        super().__init__(merk, model, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info_kendaraan(self):
        return f"{super().info_kendaraan()} dengan {self.jumlah_pintu} pintu"

    def buka_pintu(self):
        print(f"Pintu {self.info_kendaraan()} dibuka.")

class Motor(Kendaraan):
    def __init__(self, merk, model, tahun, jenis):
        super().__init__(merk, model, tahun)
        self.jenis = jenis

    def info_kendaraan(self):
        return f"{super().info_kendaraan()} ({self.jenis})"

    def stang(self):
        print(f"Stang {self.info_kendaraan()} diputar.")

class MobilSport(Mobil):
    def __init__(self, merk, model, tahun, jumlah_pintu, kecepatan_maks):
        super().__init__(merk, model, tahun, jumlah_pintu)
        self.kecepatan_maks = kecepatan_maks

    def info_kendaraan(self):
        return f"{super().info_kendaraan()} dengan kecepatan maksimum {self.kecepatan_maks} km/jam"

    def nitro(self):
        print(f"Nitro diaktifkan pada {self.info_kendaraan()}! Kecepatan meningkat!")

class MotorListrik(Motor):
    def __init__(self, merk, model, tahun, jenis, kapasitas_baterai):
        super().__init__(merk, model, tahun, jenis)
        self.kapasitas_baterai = kapasitas_baterai

    def info_kendaraan(self):
        return f"{super().info_kendaraan()} dengan kapasitas baterai {self.kapasitas_baterai} kWh"

    def isi_baterai(self):
        print(f"Baterai {self.info_kendaraan()} sedang diisi.")

if __name__ == "__main__":
    # Membuat objek dari berbagai kelas
    mobil_sport = MobilSport("Ferrari", "488", 2021, 2, 330)
    motor_listrik = MotorListrik("Tesla", "Model M", 2020, "Sport", 100)

    # Menggunakan metode dari kelas dasar dan turunan
    mobil_sport.jalankan()
    mobil_sport.buka_pintu()
    mobil_sport.nitro()

    motor_listrik.jalankan()
    motor_listrik.stang()
    motor_listrik.isi_baterai()
