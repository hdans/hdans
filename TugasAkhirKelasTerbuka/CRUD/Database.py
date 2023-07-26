from . import operasi
# 16. membuat file operasi dan mengimport nya
# 17. Membuat konstanta data yang akan dibuat 
DT_NAME = "data_text.txt"
# 18. Membuat dict yang berisi template untuk diisi nanti -> Lanjut ke operasi
TEMPLATE = {
    'pk' :'XXXXXX',
    'date_add' : 'YYYY-MM-DD',
    'judul' : 255* ' ',
    'penulis' : 255 * ' ',
    'tahun' : "YYYY"
}

# 13. Membuat function init_console()
def init_console():
    # 14. Mengecek apakah data file ada / tidak
    try:
        with open(DT_NAME ,  "r") as file:
            print("Data text is available")
    except:
        # 15. Jika tidak ada, maka akan memanggil fungsi membentuk data baru
        print("\nData books are not found, generating to make a first data book...")
        operasi.create_first_data()

