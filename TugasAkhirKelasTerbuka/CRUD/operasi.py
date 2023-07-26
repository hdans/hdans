from . import Database
from .Util import random_string
import time
import os


"""
    # 107. Note: di fungsi delete ini kita agak berbeda cara kita mendeletenya, mekanisme nya adalah:
        1. Kita akan membuat dataFile yang baru (dataFile2 <- misal) 
        2. Setelah itu kita akan membaca data file yang lama menggunakan read + counter untuk mengetahui
            data mana yang ingin kita delete dan mana yang tetap kita simpan
        3. Data yang akan kita simpan akan kita copy, dan akan kita pindahkan ke dataFile2 tanpa mengcopy data yang kita delete
        4. Setelah itu data yang sudah kita copy bersih akan ditukar filenya dengan data asli
        5. Yang akhirnya data kotor yang masih ada data yg kita delete akan bernama dataFile2, sedangkan data yang bersih
            adalah data yang asli, hal ini karena kita tuker
"""
# 108. membuat fungsi delete
def delete(no_buku):
    try:
        # 109. mencoba untuk membaca data
        with open(Database.DT_NAME , 'r') as file:
            # 110. buat variabel counter(penghitung), untuk mengecek garis mana yang kita mau copy ke template
            counter = 0
            while True:
                # 111. Kita akan membaca file nya di perulangan sehingga membaca nya bisa baris per baris seiringnya perulangan
                content = file.readline()
                # 113. Jika konten nya tidak ada apa2, berarti pembacaan semua baris sudah selesai
                if len(content) == 0:
                    break
                # 114. Jika counter nya setara dengan no_buku-1, maka akan diabaikan & tidak dicopy
                    # Ini artinya kita membiarkan data yang kita delete untuk tidak disimpan
                elif counter == no_buku-1:
                    pass
                # 115. Di sisi lain, kita akan membuat file baru untuk kita taruh data bersih nya
                else:
                    with open("data_temp.txt" , 'a' , encoding='utf-8') as file_temp:
                        file_temp.write(content)
                # 112. Membuat counter nya bertambah tiap perulangan
                counter += 1
    except:
        print("Error cowg")
    # 116. Dan kita akan menukar data bersih dengan data asli, sehingga data asli menjadi data bersih -> main.py
    os.replace("data_temp.txt",Database.DT_NAME)

        

# 80. membuat fungsi update
def update(no_buku,pk ,add_name, tahun , judul , penulis):
    # 81. membuat template nya
    data_template = Database.TEMPLATE.copy()
    data_template['pk'] = pk
    data_template['date_add'] = add_name # 82. Untuk pk dan date add gausah diganti lagi karena data nya sama
    data_template['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data_template['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data_template['tahun'] = str(tahun)
    
    # 83. Masukkan data tadi ke template string
    data_str = data_str = f"\n{data_template['pk']},{data_template['date_add']},{data_template['judul']},{data_template['penulis']},{data_template['tahun']}"
    
    # 84. membuat data panjang dari str
    panjang_data = len(data_str)
    try:
        # 85. Dengan kita tau panjang dari datastr tu berapa, kita juga bisa membuat agar kita mengubah data yang keberapa
        with open(Database.DT_NAME , "r+" , encoding="utf-8") as file: # 86. Jangan lupa jadiin r+ (read + write)
            # 87. Kita mengarahkan kursor untuk pergi ke kolom panjang data x index buku agar di situ kita bisa ubah file nya
            file.seek(panjang_data * (no_buku -1)) 
            # 88. Setelah kita tau file nya di baris berapa, kita timpa dia dengan write -> main.py
            file.write(data_str)
    except:
        print("Error")


# 59. Membuat function create dengan parameter judul penulis tahun karena kita membutuhkannya
def create(judul , penulis , tahun):
    # 60. Lakukan hal yang sama di create ini, yaitu mengekstrak data yang kita input
    data_template = Database.TEMPLATE.copy()
    data_template['pk'] = random_string(6)
    data_template['date_add'] = time.strftime("%y-%m-%d-%H-%S%z" , time.gmtime())
    data_template['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data_template['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data_template['tahun'] = str(tahun)

    # 61. Masukkan ke template
    data_str = f"\n{data_template['pk']},{data_template['date_add']},{data_template['judul']},{data_template['penulis']},{data_template['tahun']}"
    try:
        # 62. append (a) data tadi ke konstanta database -> main.py
        with open(Database.DT_NAME, "a" , encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("bang udah bang gw cape error mulu:(")

# 19. Membuat fungsi yang membuat data baru
def create_first_data():
    print("\n" + "=" * 70)
    # 20. Membuat input untuk penulis dan judul
    judul = input("\nInput book's tittle\t: ")
    penulis = input("Input Author's\t\t: ")
    # 21. Membuat perulangan agar tahun nya sesuai dengan apa yang kita inginkan
    while True:
        try:
            tahun = int(input("Input release date\t: "))
            # 22. Mengecek tahun agar 4 angka
            if len(str(tahun)) == 4:
                break
            else:
                print("Input the year correctly (YYYY) with 4 number")
        # 23. Mengecek tahun agar tidak String
        except:
            print("Input the year correctly (YYYY) with number ")
    # 24. Membuat copy dari TEMPLATE
    data_template = Database.TEMPLATE.copy()
    # 25. Membuat kode unik sebagai id data, dengan membuat random_string di Util.py -> lanjut ke util
    data_template['pk'] = random_string(6)
    # 30. membuat tanggal sebagai data untik pakai import nya time , time.strftime("%y-%m-$d-$H-%S%z" , time.gettime()) 
    data_template['date_add'] = time.strftime("%y-%m-%d-%H-%S%z" , time.gmtime())
    # 31. membuat judul, judulnya ditambah data maksimum dari judul agar tidak error
    data_template['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    # 32. membuat penulis, penulis juga ditambah panjang maks dari penulis, penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data_template['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    # 33. input tahun, jangan lupa dijadiin string
    data_template['tahun'] = str(tahun)

    # 34. membuat template string untuk dimasukkan ke data
    data_str = f"{data_template['pk']},{data_template['date_add']},{data_template['judul']},{data_template['penulis']},{data_template['tahun']}"

    # 35. Mencoba untuk write data_str nya di file baru -> Lanjut ke main.py
    try:
        with open(Database.DT_NAME, "w" , encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("bang udah bang gw cape error mulu:(")
    print("\n" + "=" * 70)
# 43. Membuat fungsi read()
def read(**kwargs): # 68. Membuat kwargs di parameter
    # 44. mencoba membaca data
    try:
        with open(Database.DT_NAME , "r") as file:
            # 45. baca data per baris
            fileNya = file.readlines()

            #69. Membuata var jumlah buku
            jumlah_buku = len(fileNya)
            # 70. Mengecek apabila ada key 'index' kwargs
            if "index" in kwargs:
                # 71. janlup index - 1
                index_buku = kwargs['index'] - 1
                # 72. Membuat antisipasi jika input aneh aneh
                if index_buku < 0 or index_buku > jumlah_buku :
                    return False
                else:
                    # 73. Jika tidak aneh aneh. returnnya baris keberapa dari data tsb -> view.py
                    return fileNya[index_buku]
            else:
                # 46. Menghasilkan fileNya -> lanjut view
                return fileNya
    except:
        print("Terjadi error")
        return False