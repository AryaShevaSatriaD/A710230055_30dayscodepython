class tiket:
    def __init__(self, harga):
        self.harga = harga

class TiketBiasa(tiket):
    def __init__(self,harga):
        super().__init__(harga)

class TiketVIP(tiket):
    def __init__(self, harga):
        super().__init__(harga)

class TiketGold(tiket):
    def __init__(self, harga):
        super().__init__(harga)

def hitungan_total_harga(jenis_tiket, jumlah_tiket):
    if jenis_tiket == "biasa":
        tiket = TiketBiasa(40000)
    elif jenis_tiket == "vip":
        tiket = TiketGold(47000)
    elif jenis_tiket == "gold":
        tiket = TiketVIP(60000)
    else:
        raise ValueError("Jenis tiket yang diinput tidak valid")
    
    total_harga = tiket.harga  * jumlah_tiket
    return total_harga

jenis_tiket = input("Masukan jenis tiket (biasa/vip/gold) : ")
jumlah_tiket = int(input("Masukan jumlah tiket : "))

total_harga = hitungan_total_harga(jenis_tiket, jumlah_tiket)
print(f"Total Harga Tiket : Rp {total_harga}")