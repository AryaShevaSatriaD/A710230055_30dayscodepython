from abc import ABC, abstractmethod

# Kelas dan Objek Dasar
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.hewan_peliharaan = []
        self.akun_bank = BankAccount("00000001", 0)

    def perkenalkan_diri(self):
        print(f"Halo, nama saya {self.nama} dan saya berumur {self.umur} tahun.")

    def tambah_hewan_peliharaan(self, hewan):
        self.hewan_peliharaan.append(hewan)
        print(f"{hewan.nama} telah ditambahkan sebagai hewan peliharaan.")

    def tampilkan_hewan_peliharaan(self):
        print(f"{self.nama} memiliki hewan peliharaan:")
        for hewan in self.hewan_peliharaan:
            hewan.bersuara()

# Pewarisan (Inheritance)
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        pass

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} berkata: Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama} berkata: Guk guk!")

# Enkapsulasi (Encapsulation)
class BankAccount:
    def __init__(self, nomor_akun, saldo):
        self.__nomor_akun = nomor_akun
        self.__saldo = saldo

    def deposit(self, jumlah):
        self.__saldo += jumlah
        print(f"Deposit sebesar {jumlah}. Saldo sekarang: {self.__saldo}")

    def withdraw(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Withdraw sebesar {jumlah}. Saldo sekarang: {self.__saldo}")
        else:
            print("Saldo tidak mencukupi.")

    def cek_saldo(self):
        print(f"Saldo: {self.__saldo}")

# Polimorfisme (Polymorphism)
class Burung:
    def bersuara(self):
        print("Burung bersuara.")

class Elang(Burung):
    def bersuara(self):
        print("Elang bersuara: Keee!")

class Beo(Burung):
    def bersuara(self):
        print("Beo bersuara: Hello!")

def buat_bersuara(burung):
    burung.bersuara()

# Abstraksi (Abstraction)
class Kendaraan(ABC):
    @abstractmethod
    def jumlah_roda(self):
        pass

class Mobil(Kendaraan):
    def jumlah_roda(self):
        return 4

class SepedaMotor(Kendaraan):
    def jumlah_roda(self):
        return 2

# Main Application
if __name__ == "__main__":
    # Bagian 1: Kelas dan Objek Dasar
    pemilik = Orang("Budi", 25)
    pemilik.perkenalkan_diri()

    # Bagian 2: Pewarisan (Inheritance)
    kucing = Kucing("Kitty")
    anjing = Anjing("Doggy")
    pemilik.tambah_hewan_peliharaan(kucing)
    pemilik.tambah_hewan_peliharaan(anjing)

    # Bagian 3: Enkapsulasi (Encapsulation)
    pemilik.akun_bank.deposit(1000)
    pemilik.akun_bank.withdraw(300)
    pemilik.akun_bank.cek_saldo()

    # Bagian 4: Polimorfisme (Polymorphism)
    elang = Elang()
    beo = Beo()
    buat_bersuara(elang)
    buat_bersuara(beo)

    # Bagian 5: Abstraksi (Abstraction)
    mobil = Mobil()
    sepeda_motor = SepedaMotor()
    print(f"Mobil memiliki {mobil.jumlah_roda()} roda.")
    print(f"Sepeda Motor memiliki {sepeda_motor.jumlah_roda()} roda.")

    # Tampilkan hewan peliharaan
    pemilik.tampilkan_hewan_peliharaan()
