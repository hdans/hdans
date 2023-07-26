import os
# 8. Mengimport CURD
import CRUD as CRUD

#1. Membuat perulangan di main menu program
while True:
    # 3. Membuat if seperti ini untuk mengclear terminal2
    if __name__ == "__main__":
        # 4. Mengambil nama device nya
        system_operation = os.name
        match system_operation:
            # 5. Jika posix(linux / os ) maka menghasilkan clear
            case "posix" : os.system("clear")
            # 6. Jika nt(Windows) maka menghasilkan cls
            case "nt" : os.system("cls")
    # 7. Membuat header untuk program
    print("=" * 36)
    print("WELCOME TO INPUT DATA BOOKS PRGORAM")
    print("DATABASE LIBRARIES".center(36 , " "))
    print("=" * 36)
    # 10. Memanggil fungsi CRUD.init_console() yang akan kita buat di file Database
    CRUD.init_console()
    # 11. Kita membuat dahulu pilihan-pilihan nya
    print("What do you want to do?\n")
    print("a. Read books data")
    print("b. Add books data")
    print("c. Update boooks data")
    print("d. Delete books data\n")
    # 12. Bikin input dan masukkan pilihan-pilihan nya --> Lanjut ke file database
    user_option = input("Pick what do you want?\t: ")
    match user_option:
        case "a" : CRUD.read_console() # 36. Membuat fungsi read_console() di view.py -> pindah ke view.py
        case "b" : CRUD.create_console() # 53. Membuat fungsi create -> view.py
        case "c" : CRUD.update_console() # 63. Membuat fungsi update -> view.py
        case "d" : CRUD.delete_console() # 89. membuat fungsi delete -> view.py


    #2. Membuat pilihan untuk menghentikan program
    user_quit_option = input("Are you done with our PROGRAM?(y/n)\t: ")
    if user_quit_option == "Y" or user_quit_option == "y":
        break
system_operation = os.name
match system_operation:
    case "posix" : os.system("clear")
    case "nt" : os.system("cls")

# 117. Pencatatan selesai, gg coy
print("=" * 70)   
print("\nThankyou for using our program, have a nice day! \\(^^)/\n")
print("=" * 70)   
    