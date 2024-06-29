from abc import ABC, abstractmethod

class Produk(ABC):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    @abstractmethod
    def hitung_harga_akhir(self):
        pass

    def __str__(self):
        return f"Nama Produk: {self.nama}, Harga Awal: {self.harga}"

class Elektronik(Produk):
    def __init__(self, nama, harga, garansi_tahun):
        super().__init__(nama, harga)
        self.garansi_tahun = garansi_tahun

    def hitung_harga_akhir(self):
        # Elektronik mendapatkan diskon 10%
        diskon = 0.10
        harga_akhir = self.harga * (1 - diskon)
        return harga_akhir

class Pakaian(Produk):
    def __init__(self, nama, harga, diskon_musim):
        super().__init__(nama, harga)
        self.diskon_musim = diskon_musim

    def hitung_harga_akhir(self):
        # Pakaian mendapatkan diskon musiman
        harga_akhir = self.harga * (1 - self.diskon_musim)
        return harga_akhir

class BahanPokok(Produk):
    def __init__(self, nama, harga, diskon_kedaluwarsa):
        super().__init__(nama, harga)
        self.diskon_kedaluwarsa = diskon_kedaluwarsa

    def hitung_harga_akhir(self):
        # Bahan pokok mendapatkan diskon khusus jika mendekati tanggal kedaluwarsa
        harga_akhir = self.harga * (1 - self.diskon_kedaluwarsa)
        return harga_akhir

# Perilaku polimorfik
def cetak_harga_produk(produk):
    for item in produk:
        print(f"{item} - Harga Akhir: {item.hitung_harga_akhir()}")

# Membuat instance dari berbagai jenis produk
produk = [
    Elektronik("Laptop", 15000000, 2),
    Pakaian("Kaos", 300000, 0.20),
    BahanPokok("Susu", 30000, 0.50)
]

# Mencetak harga akhir mereka
cetak_harga_produk(produk)
