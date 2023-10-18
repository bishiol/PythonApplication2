
class BigInteger:
    def __init__(self):
        self.data = []  # Масив 64-бітних беззнакових цілих чисел

    def setHexString(self, hex_string):
        # Метод для встановлення числа з шістнадцяткової системи числення
        self.data = []
        hex_length = len(hex_string)
        for i in range(hex_length, 0, -16):
            chunk = hex_string[max(0, i - 16):i]
            self.data.insert(0, int(chunk, 16))

    def getHexString(self):
        # Метод для повернення числа у шістнадцятковій системі числення
        hex_string = ""
        for chunk in self.data:
            hex_string += format(chunk, '016x')
        return hex_string

    def setDecimal(self, decimal_string):
        # Метод для встановлення числа з десяткового рядка
        self.data = []
        decimal_int = int(decimal_string)
        while decimal_int > 0:
            chunk = decimal_int & 0xFFFFFFFFFFFFFFFF
            self.data.insert(0, chunk)
            decimal_int >>= 64

    def getDecimal(self):
        # Метод для повернення числа в десятковому форматі
        decimal_string = "0"
        for chunk in self.data:
            decimal_string = str(int(decimal_string) * (2**64) + chunk)
        return decimal_string



    def inv(self):
        # Побітова інверсія
        result = BigInteger()
        for chunk in self.data:
            result.data.append(~chunk & 0xffffffffffffffff)
        return result

    def xor(self, other):
        # Побітове виключне або
        result = BigInteger()
        for a, b in zip(self.data, other.data):
            result.data.append(a ^ b)
        return result

    def or_(self, other):
        # Побітове або
        result = BigInteger()
        for a, b in zip(self.data, other.data):
            result.data.append(a | b)
        return result

    def and_(self, other):
        # Побітове і
        result = BigInteger()
        for a, b in zip(self.data, other.data):
            result.data.append(a & b)
        return result

    def shiftR(self, n):
        # Зсув праворуч на n бітів
        result = BigInteger()
        carry = 0
        for chunk in self.data:
            shifted_chunk = (chunk >> n) | (carry << (64 - n))
            carry = chunk & ((1 << n) - 1)
            result.data.append(shifted_chunk)
        return result

    def shiftL(self, n):
        # Зсув ліворуч на n бітів
        result = BigInteger()
        carry = 0
        for chunk in self.data[::-1]:
            shifted_chunk = (chunk << n) | carry
            carry = chunk >> (64 - n)
            result.data.insert(0, shifted_chunk)
        return result



    def add(self, other):
        # Метод для додавання
        if not isinstance(other, BigInteger):
            raise TypeError("Unsupported operand type for +: BigInteger and {}".format(type(other))) # Якщо непідтримуваний тип операнда
        result = BigInteger()
        carry = 0
        for a, b in zip(self.data, other.data):
            temp_sum = a + b + carry
            result.data.append(temp_sum & 0xffffffffffffffff)
            carry = temp_sum >> 64
        return result

    def sub(self, other):
        # Метод для віднімання
        if not isinstance(other, BigInteger):
            raise TypeError("Unsupported operand type for -: BigInteger and {}".format(type(other))) # Якщо непідтримуваний тип операнда для
        result = BigInteger()
        borrow = 0
        for a, b in zip(self.data, other.data):
            temp_diff = a - b - borrow
            result.data.append(temp_diff & 0xffffffffffffffff)
            borrow = 1 if temp_diff < 0 else 0
        return result

    def mod(self, mod_value):
        # Метод для взяття за модулем
        result = BigInteger()
        for a in self.data:
            mod_result = a % mod_value
            result.data.append(mod_result)
        return result



# 1. Приклади використання власного типу даних великого числа:
num1 = BigInteger()
num1.setHexString("51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4")
num2 = BigInteger()
num2.setHexString("403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c")

num3 = BigInteger()
num3.setHexString("36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80")
num4 = BigInteger()
num4.setHexString("70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb")

num5 = BigInteger()
num5.setHexString("33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc")
num6 = BigInteger()
num6.setHexString("22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03")

num7 = BigInteger()
num7.setHexString("7d7deab2affa38154326e96d350deee1")
num8 = BigInteger()
num8.setHexString("97f92a75b3faf8939e8e98b96476fd22")

num9 = BigInteger()
num9.setDecimal("18102023")

print("Num1String:", num1.getHexString())
print("Num2String:", num2.getHexString())
print("Num3String:", num3.getHexString())
print("Num4String:", num4.getHexString())
print("Num5String:", num5.getHexString())
print("Num6String:", num6.getHexString())
print("Num7String:", num7.getHexString())
print("Num8String:", num8.getHexString())

print("Num1Decimal: ",num1.getDecimal())
print("Num3Decimal: ",num3.getDecimal())

print("Num9Decimal: ",num9.getDecimal())
print("Num9String:", num9.getHexString())




# 2. Прикоди побітових операцій
print("\n\n")

inv_result = num1.inv()
print("INV:", inv_result.getHexString())

xor_result = num1.xor(num2)
print("XOR:", xor_result.getHexString())

or_result = num3.or_(num2)
print("OR:", or_result.getHexString())

and_result = num5.and_(num2)
print("AND:", and_result.getHexString())

shift_right_result = num4.shiftR(3)
print("Shift Right:", shift_right_result.getHexString())

shift_left_result = num6.shiftL(2)
print("Shift Left:", shift_left_result.getHexString())




# 3. Прикоди побітових операцій
print("\n\n")

print("ADD:", num3.add(num4).getHexString())

sub_result = num6.add(num5)
print("SUB:", sub_result.getHexString())

mod_result = num4.mod(2)
print("MOD:", mod_result.getHexString())