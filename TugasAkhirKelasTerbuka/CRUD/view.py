from . import operasi
# 91. Membuat variable total baris -> read_console
total_baris = 0


# 90. membuat fungsi delete
def delete_console():
    # 95. Panggil lagi total barisnya
    global total_baris
    read_console() # 96. panggil read console untuk preview deletenya
    # 97. Membuat perulangan(1) untuk mengecek apakah dia data terakhir
    while True: 
        # 98. input no buku yang ingin didelete
        no_buku =  int(input("Input book's number which you want to delete : "))
        # 99. break ketika no yang dipilih adalah data terkahir
            # Hal ini karena jika kita delete data terakhir maka file akan terjadi error
        if no_buku == total_baris:
            print("Sorry, we cant delete the last book")
            break
        try:
            # 101. membuat perulangan(2) untuk delete2an
            while True:
                # 102. mengambil no buku di fungsi read agar kita mendapatkan file di baris yang kita inginkan
                data_buku = operasi.read(index = no_buku)
                if data_buku:
                    break
                else:
                    pass
        except:
            print("Data's number input is invalid, try again next time")
        # 103. setelah dapat file yang di baris kita inginkan, buat template nya
        data_break = data_buku.split(',')
        pk = data_break[0]
        add_name = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4] 
        while True:
            # 104. Buat preview untuk data yang ingin kita hapus
            print("\n" + "=" * 75)
            print("This is the book's data which you want to delete :")
            print(f"1. Title's data\t: {judul:.40}")
            print(f"2. Author's data: {penulis:.40}")
            print(f"3. Year's data\t: {tahun:.10}")
            # 105. buat peringatan untuk hapus datanya/tidak
            user_quit_option = input("\nAre you really want to DELETE the data?(y/n)\t: ")
            if user_quit_option == "Y" or user_quit_option == "y":
                print("\n" + "=" * 75 + "\n")
                # 106. Jika user bilang iya, maka akan memanggil fungsi delete -> operasi.py
                operasi.delete(no_buku)
                print("Data are deleted. Back to the main menu...")
                print("\n" + "=" * 75 + "\n")
                break
            else:
                break
        # 100. membuat break agar ketika input berjalan lancar perulangan(1) akan berhenti
        break
    
    

# 64. Membuat fungsi update
def update_console():
    # 65. Memanggil read console untuk preview data mana yang diubah
    read_console()
    try:
        # 66. Membuat input buku agar sesuai dengan apa yang kita mau
        while True:
            no_buku =  int(input("Input book's number which you want to update : "))
            # 67. import variabel no buku ke fungsi read-> operasi.py
            data_buku = operasi.read(index = no_buku)
            if data_buku:
                break
            else:
                pass
    except:
        print("Book's number input is invalid, try again next time")
    # 74. Membuat variabel lagi
    data_break = data_buku.split(',') # Bedanya, yang ini data_buku nya adalah baris ke-x dari sebuah data
    pk = data_break[0]
    add_name = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4]
    while True:
            # 75. membuat perulangan dan memberikan data suatu index serta memilih apa yang mau diganti datanya
            print("\n" + "=" * 75)
            print(f"1. Title's data\t: {judul:.40}")
            print(f"2. Author's data: {penulis:.40}")
            print(f"3. Year's data\t: {tahun:.10}")
            user_option_update = int(input("Pick data which you want to change[1,2,3]: "))

            print("\n" + "=" * 75)
            # 76. membuat input untuk file yang dipilih
            match user_option_update:
                case 1 : judul = input("\nInput your new tittle\t: ")
                case 2 : penulis = input("\nInput your new author\t: ")
                case 3:
                    while True:
                        try:
                            tahun = (input("\nInput ypur new release year\t: "))
                            if len(tahun) == 4:
                                break
                            else:
                                print("Input the year correctly (YYYY) with 4 number")
                        except:
                            print("Input the year correctly (YYYY) with number ")
                case _: print("\nIndex is invalid, try again next time")
            # 77. header setelah input data dan berikan preview data
            print("\n" + "=" * 75)
            print("Generating your new data.... Those are your new data: ")
            print("\n" + "=" * 75)
            print(f"1. Title's data\t: {judul:.40}")
            print(f"2. Author's data: {penulis:.40}")
            print(f"3. Year's data\t: {tahun:.10}")
            print("=" * 75)
            # 78. pilihan untuk lanjut/tidak
            user_quit_option = input("\nAre you done with UPDATING data?(y/n)\t: ")
            if user_quit_option == "Y" or user_quit_option == "y":
                print("\n" + "=" * 75 + "\n")
                print("(Back to the main menu)")
                print("\n" + "=" * 75 + "\n")
                break
    # 79. memnaggil fungsi update dengan parameter2nya untuk data -> operasi.py
    operasi.update(no_buku,pk ,add_name, tahun , judul , penulis)

    


# 54. Membuat function
def create_console():
    print("\n" + "=" * 71)
    print("Please input the data\n")
    # 55. Membuat input data penulis & judul
    penulis = input("Input author's name\t: ")
    judul = input("Input title\t\t: ")
    # 56. Sama seperti create_first_data, kita membuat agar tahun diinput sesuai keiinginan
    while True:
        try:
            tahun = int(input("Input release date\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Input the year correctly (YYYY) with 4 number")
        except:
            print("Input the year correctly (YYYY) with number ")
    # 58. Panggil create function dan buat functionnya -> operasi.py
    operasi.create(judul , penulis , tahun)
    print("\nThose are your new datas:")
    # 57. Panggil dulu read_console() untuk memastikan data yang diinput
    read_console()


# 37. Membuat read_console()
def read_console():
    # 92. membuat total baris menjadi variabel global -> for loop
    global total_baris
    total_baris = 0
    # 38. Memanggil fungsi read() di operasi
    dataFile = operasi.read()
    # 39. Membuat template string untuk ditampilkan di main.py
    no = "No"
    penulis = "Author"
    judul = "TItle"
    tahun = "Year"
    # 40. Masukkan template tersebut
    template = f"|{no:^6}|{judul:^30}|{penulis:^20}|{tahun:^8}"

    # 41. Buat header
    #Header
    print("\n" + 71*"=")
    # 42. Print template tadi untuk dijadikan tabel -> kembali ke operasi
    print(template)

    # 47. Buat perulangan index , data enumarate si dataFile dari operasi
    for index, data in enumerate(dataFile):
        # 93. Menambah variabel baris ini setiap for loop jalan, untuk mendapatkan info berpaa baris total filenya -> delete
        total_baris += 1
        # 48. split data dengan koma, karena kita readlines data2nya dan membentuk sebuah list
        dataBreak = data.split(",")
        # 49. Panggil 1 1 datanya
        pk = dataBreak[0]
        dataDate = dataBreak[1]
        judul = dataBreak[2]
        penulis = dataBreak[3]
        tahun = dataBreak[4]
        # 50. no nya jangan lupa ditambah 1
        no = index + 1
        # 51. Masukkan ke template
        print(f"| {no:<5}| {judul:.29}| {penulis:.19}| {tahun:.7}" , end="")
    
    # 52. Read_console() selesai dibuat, saatnya kembali ke main.py
    #Footer
    print("\n" + "-"*71)
    print(71*"=" + "\n")