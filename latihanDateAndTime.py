import datetime as dt

print("\n")
print("Halo, program ini dibuat untuk kalian mengetahui dengan tepat berapa Umur kalian".center(90 , "="))
print("Tolong masukkan data-data di bawah ini ^^")
tanggal = int(input("Tanggal berapa kamu lahir? \t: "))
bulan = int(input("Bulan berapa kamu lahir? \t: "))
tahun = int(input("Tahun berapa kamu lahir? \t: "))

dataLahir = dt.date(tahun , bulan , tanggal)
print(f"\nAnda lahir pada {dataLahir}, di hari {dataLahir:%A}")
dataHariIni = dt.date.today()

umurHari = dataHariIni - dataLahir
umurTahun = umurHari  // 365
umurBulan = (umurHari.days % 365) // 30
umurMinggu = ((umurHari.days % 365) % 30) // 7
umurHari1 = ((umurHari.days % 365) % 30) % 7  
print(f"Umur anda (Hari) adalah {umurHari.days} hari")
print(f"Secara lengkap, umur anda adalah {umurTahun.days} Tahun {umurBulan} Bulan {umurMinggu} Minggu dan {umurHari1} Hari")
