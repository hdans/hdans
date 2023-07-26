import CRUD
tes = """d s k a f u,23-07-26-10-26+0700,Aku si perasis handal                                                                                                                                                                                                                                          ,Fajar Racing                                                                                                                                                                                                                                                   ,2020"""
print(len(tes))
tes2 = """r l W J U e,23-07-26-10-08+0700,Cara tobat dari gay                                                                                                                                                                                                                                            ,Kibet Gay                                                                                                                                                                                                                                                      ,2030"""
print(len(tes2))

with open("DataTEST.txt" , "w" , encoding="utf-8") as file:
    tesWoi = file.write("Agus bapak lo kahhh?")
    file.write(tesWoi.rstrip("?"))