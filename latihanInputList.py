print("PROGRAM INPUT DATA SISWA DAN UNIVESITASNYA".center(90 , "="))
print("\nDimohon untuk memasukkan nama dan univesitas siswa")

listMahasiswa = []

while True:
    inputNama = input("\nMasukkan nama\t\t: ")
    inputAngka = input("Masukkan Universitas\t: ")
    dataMahasiswa = [inputNama , inputAngka]
    listMahasiswa.append(dataMahasiswa)
    print("\n")
    print("BERIKUT ADALAH LISTNYA".center(57 , "="))
    print("|\tNo\t|\tNama\t|\tUniversitas\t|")

    for index, list in enumerate(listMahasiswa):
        print(f"|\t{index + 1}\t|\t{list[0]}\t|\t{list[1]}\t\t|")
    print("="*57)

    pilihan = input("\nApakah penginputan ingin dilanjut?(y/n)\t: ")
    if pilihan == "n":
        print("Baik, terimakasih sudah menggunakan program kami untuk menginput! ")
        break




