class BankAccount:
    def __init__(self, account_number, account_holder):
        self.__account_number = account_number  # atribut private
        self.__account_holder = account_holder  # atribut private
        self.__balance = 0.0                    # atribut private

    # Getter untuk account number
    def get_account_number(self):
        return self.__account_number

    # Getter untuk account holder
    def get_account_holder(self):
        return self.__account_holder

    # Getter untuk balance
    def get_balance(self):
        return self.__balance

    # Method untuk menyetor uang
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} telah disetor. Saldo baru: {self.__balance}")
        else:
            print("Jumlah yang disetor harus positif.")

    # Method untuk menarik uang
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{amount} telah ditarik. Saldo baru: {self.__balance}")
            else:
                print("Saldo tidak mencukupi.")
        else:
            print("Jumlah yang ditarik harus positif.")

# Contoh penggunaan kelas BankAccount
akun1 = BankAccount("123456789", "Alice")

# Mengakses informasi akun
print(f"Nomor Akun: {akun1.get_account_number()}")
print(f"Pemilik Akun: {akun1.get_account_holder()}")
print(f"Saldo Awal: {akun1.get_balance()}")

# Melakukan setoran
akun1.deposit(500.0)
akun1.deposit(1500.0)

# Melakukan penarikan
akun1.withdraw(300.0)
akun1.withdraw(2000.0)

# Mengecek saldo akhir
print(f"Saldo Akhir: {akun1.get_balance()}")
