class NumberConverter:
    def __init__(self, number, base=10):
        self.number = number
        self.base = base

    def to_binary(self):
        if self.base == 10:
            return self.decimal_to_binary(self.number)
        elif self.base == 2:
            return self.number  # Already in binary
        else:
            raise ValueError("Unsupported base for binary conversion")

    def to_decimal(self):
        if self.base == 2:
            return self.binary_to_decimal(self.number)
        elif self.base == 10:
            return self.number  # Already in decimal
        else:
            raise ValueError("Unsupported base for decimal conversion")

    @staticmethod
    def decimal_to_binary(decimal_number):
        if decimal_number == 0:
            return '0'
        binary_number = ''
        while decimal_number > 0:
            binary_number = str(decimal_number % 2) + binary_number
            decimal_number //= 2
        return binary_number

    @staticmethod
    def binary_to_decimal(binary_number):
        decimal_number = 0
        binary_number = str(binary_number)
        for digit in binary_number:
            decimal_number = decimal_number * 2 + int(digit)
        return decimal_number

# Contoh penggunaan
if __name__ == "__main__":
    decimal_converter = NumberConverter(42, base=10)
    print(f"Desimal {decimal_converter.number} dalam biner adalah {decimal_converter.to_binary()}")

    binary_converter = NumberConverter('101010', base=2)
    print(f"Biner {binary_converter.number} dalam desimal adalah {binary_converter.to_decimal()}")
