import random # 26. Import random dan string
import string

# 27. Membuat random string dengan int panjang dan menghasilkan string
def random_string(panjang:int) -> str:
    # 28. ' '.join(random.choice(string.ascii_letters) for i in range(panjang))
    # Kita akan membuat kode random dari huruf2
    hasil_string = ' '.join(random.choice(string.ascii_letters) for i in range(panjang))
    # 29. Menghasilkan string -> Balik lagi ke Operasi
    return hasil_string
