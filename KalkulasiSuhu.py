Suhu = int(input("Masukkan berapa derajat suhu: "))
print("a. Celcius")
print("b. Reamur")
print("c. Farenheit")
print("d. Kelvin")
jenis = input("Apa besaran Suhu mu? ")
print("=====================")
if(jenis == "a"):
    print("Jadi suhu nya adalah" , Suhu , "Celcius")
    yesOrNot = input("Apakah kamu mau mengonversi nya? yes/no: ")
    print("=====================")
    if(yesOrNot == "yes"):
        print("a. Reamur")
        print("b. Farenheit")
        print("c. Kelvin")
        suhuApa = input("Mau jadi suhu apa? ")
        print("=====================")
        if(suhuApa == "a"):
            print("Suhu nya jadi" , 4 / 5 * Suhu , "Derajat Reamur")
        if(suhuApa == "b"):
            print("Suhu nya jadi" , 9 / 5 * Suhu + 32 , "Derajat Farenheit")
        if(suhuApa == "c"):
            print("Suhu nya jadi" , Suhu + 273 , "Derajat Kelvin")
    else:
        print("Ok!")
if(jenis == "b"):
    print("Jadi suhu nya adalah" , Suhu , "Reamur")
    yesOrNot = input("Apakah kamu mau mengonversi nya? yes/no: ")
    print("=====================")
    if(yesOrNot == "yes"):
        print("a. Celcius")
        print("b. Farenheit")
        print("c. Kelvin")
        suhuApa = input("Mau jadi suhu apa? ")
        print("=====================")
        if(suhuApa == "a"):
            print("Suhu nya jadi" , 5 / 4 * Suhu , "Derajat Celcius")
        if(suhuApa == "b"):
            print("Suhu nya jadi" , 9 / 4 * Suhu + 32 , "Derajat Farenheit")
        if(suhuApa == "c"):
            print("Suhu nya jadi" , 5 / 4 * Suhu + 273 , "Derajat Kelvin")
    else:
        print("Ok!")
if(jenis == "c"):
    print("Jadi suhu nya adalah" , Suhu , "Farenheit")
    yesOrNot = input("Apakah kamu mau mengonversi nya? yes/no: ")
    print("=====================")
    if(yesOrNot == "yes"):
        print("a. Celcius")
        print("b. Reamur")
        print("c. Kelvin")
        suhuApa = input("Mau jadi suhu apa? ")
        print("=====================")
        if(suhuApa == "a"):
            print("Suhu nya jadi" , 5 / 9 * (Suhu - 32) , "Derajat Celcius")
        if(suhuApa == "b"):
            print("Suhu nya jadi" , 4 / 9 * (Suhu - 32) , "Derajat Reamur")
        if(suhuApa == "c"):
            print("Suhu nya jadi" , 5 / 9 * (Suhu - 32) + 273 , "Derajat Kelvin")
    else:
        print("Ok!")
if(jenis == "d"):
    print("Jadi suhu nya adalah" , Suhu , "Kelvin")
    yesOrNot = input("Apakah kamu mau mengonversi nya? yes/no: ")
    print("=====================")
    if(yesOrNot == "yes"):
        print("a. Celcius")
        print("b. Reamur")
        print("c. Farenheit")
        suhuApa = input("Mau jadi suhu apa? ")
        print("=====================")
        if(suhuApa == "a"):
            print("Suhu nya jadi" , (Suhu - 273) , "Derajat Celcius")
        if(suhuApa == "b"):
            print("Suhu nya jadi" , 4 / 5 * (Suhu - 273) , "Derajat Reamur")
        if(suhuApa == "c"):
            print("Suhu nya jadi" , 9 / 5 * (Suhu - 273) +32 , "Derajat Farenheit")
    else:
        print("Ok!")

print("=====================")