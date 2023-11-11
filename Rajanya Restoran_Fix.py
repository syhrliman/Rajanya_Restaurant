# menggunakan list untuk menampung data yang sudah di input pada berbagai macam variabel, dan data tersebut nantinya dapat dipanggil sesuai kebutuhan
listnama=[]
listharga=[]
listjp=[]
total=[]

# fungsi disini untuk menyimpan sebuah data dari "masuk()" yang mana bisa kita panggil kapanpun dijika diperlukan, dan digunakan untuk login ke POS kasir
def masuk():
    print(25*"-")
    print("{:^25}".format("Login POS Kasir"))
    print("{:^25}".format(25*"-"))
    username=input("Username\t: ")
    password=input("Password\t: ")
    print(25*"-")

    if username == "raja":
        if password == "123456":
            print("Login Berhasil")
            print("\r")
            daftar_pesanan()
            Pesan()
        else:
            print("Password salah!")
            print("\r")
            masuk()
    else:
        print("Username Salah!")
        print("\r")
        masuk()


# fungsi disini untuk menyimpan sebuah data dari "daftar_pesanan()" yang mana bisa kita panggil kapanpun dijika diperlukan
def daftar_pesanan():

    # tampilan teks berupa daftar menu pesanan
    print("|{:^87}|".format(87*"="))
    print("|{:^87}|".format("Selamat Datang di Rajanya Restoran".upper()))
    print("|{:^87}|".format("Daftar Menu Restoran".upper()))
    print("|{:^87}|".format(87*"="))
    print("|{:^43}|{:^43}|".format("Makanan".upper(),"Desert".upper()))
    print("|{:^87}|".format(87*"-"))
    print("| {:<19} | {:^40} |".format("1. Mie Ayam\t\t\t: Rp 15.000","16. Bakpao                   : Rp 10.000"))
    print("| {:<30} | {:^40} |".format("2. Bakso\t\t: Rp 15.000","17. Dimsum                   : Rp 15.000"))
    print("| {:<40} | {:^40} |".format("3. Ayam Geprek              : Rp 20.000","18. Salad                    : Rp 15.000"))
    print("| {:<40} | {:^40} |".format("4. Soto Lamongan            : Rp 17.000","19. Waffle                   : Rp 15.000"))
    print("| {:<40} | {:^40} |".format("5. SOP Iga                  : Rp 25.000","20. Hot Pot                  : Rp 20.000"))
    print("| {:<40} |{:^40}|".format("6. Rawon                    : Rp 25.000",42*"-"))
    print("| {:<40} | {:^40} |".format("7. Sate Taichan             : Rp 25.000","Aneka Jus".upper()))
    print("| {:<40} |{:^40}|".format("8. Ikan Bakar               : Rp 30.000",42*"-"))
    print("| {:<40} | {:^40} |".format("9. Nasi Goreng Spesial      : Rp 20.000","21. Alpukat                  : Rp 12.000"))
    print("| {:<40} | {:^40} |".format("10. Nasi Kebuli Family      : Rp 50.000","22. Mangga                   : Rp 11.000"))
    print("|{:<40}| {:^40} |".format(42*"-","23. Jambu                    : Rp 10.000"))
    print("| {:^40} | {:^40} |".format("Minuman".upper(),"24. Apel                     : Rp 12.000"))
    print("|{:<40}| {:^40} |".format(42*"-","25. Sirsak                   : Rp 11.000"))
    print("| {:<40} | {:^40} |".format("11. Air Mineral             : Rp 5.000",""))
    print("| {:<40} | {:^40} |".format("12. Teh Manis Hangat/Dingin : Rp 5.000",""))
    print("| {:<40} | {:^40} |".format("13. Teh Tarik               : Rp 6.000",""))
    print("| {:<40} | {:^40} |".format("14. Es Jeruk                : Rp 8.000",""))
    print("| {:<40} | {:^41}|".format("15. Jasmine Tea             : Rp 10.000",""))
    print("|{:^85}|".format(85*"="))
    print("\r")

# fungsi disini untuk menyimpan sebuah data dari "Pesan()" yang mana bisa kita panggil kapanpun dijika diperlukan
def Pesan():
    pesan=input("Apakah anda ingin lanjut memesan? pilih Y untuk Ya atau pilih T untuk Tidak [Y/T] : ")
    if pesan == "Y" or pesan == "y":
        ulang()
    elif pesan == "T" or pesan == "t":
        print("Terima Kasih!!!")
    else:
        print("Pilihan yang anda masukan salah!")
        Pesan()

# fungsi disini untuk menyimpan sebuah data dari "ulang()" yang mana bisa kita panggil kapanpun dijika diperlukan, digunakan untuk input menu secara berulang tergantung jumlah pesanan
def ulang():
    berapa=int(input("Jumlah pesan menu : "))
    for i in range(berapa):
        print("\r")
        print("Pesanan ke "+str(i+1))
        Kode()
    Tanya()

# fungsi disini untuk menyimpan sebuah data dari "Kode()" yang mana bisa kita panggil kapanpun dijika diperlukan
def Kode():
    # muncul tampilan input untuk memilih menu yang tersedia mulai dari angka 1-25
    # jika angka yang di input selain dari angka "1-25" maka program langsung berjalan ke syntaks else dan akan menampilkan kembali fungsi "daftar_pesanan()"
    kode = input("Masukkan angka sesuai dengan menu yang tersedia\t: ")
    if kode == "1":
        harga = 15000
        nama="Mie Ayam"
    elif kode == "2":
        harga = 15000
        nama=("Bakso")
    elif kode == "3":
        harga = 20000
        nama=("Ayam Geprek")
    elif kode == "4":
        harga = 17000
        nama=("Soto Lamongan")
    elif kode == "5":
        harga = 25000
        nama=("SOP Iga")
    elif kode == "6":
        harga = 25000
        nama=("Rawon")
    elif kode == "7":
        harga = 25000
        nama=("Sate Taichan")
    elif kode == "8":
        harga = 30000
        nama=("Ikan Bakar")
    elif kode == "9":
        harga = 20000
        nama=("Nasi Goreng Spesial")
    elif kode == "10":
        harga = 50000
        nama=("Nasi Kebuli Family")
    elif kode == "11":
        harga = 5000
        nama=("Air Mineral")
    elif kode == "12":
        harga = 5000
        nama=("Teh Manis Hangat/Dingin")
    elif kode == "13":
        harga = 6000
        nama=("Teh Tarik")
    elif kode == "14":
        harga = 8000
        nama=("Es Jaruk")
    elif kode == "15":
        harga = 10000
        nama=("Jasmine Tea")
    elif kode == "16":
        harga = 10000
        nama=("Bakpao")
    elif kode == "17":
        harga = 15000
        nama=("Dimsum")
    elif kode == "18":
        harga = 15000
        nama=("Salad")
    elif kode == "19":
        harga = 15000
        nama=("Waffle")
    elif kode == "20":
        harga = 20000
        nama=("Hot Pot")
    elif kode == "21":
        harga = 12000
        nama=("Jus Alpukat")
    elif kode == "22":
        harga = 11000
        nama=("Jus Mangga")
    elif kode == "23":
        harga = 10000
        nama=("Jus Jambu")
    elif kode == "24":
        harga = 12000
        nama=("Jus Apel")
    elif kode == "25":
        harga = 11000
        nama=("Jus Sirsak")
    else:
        print("Pilihan yang anda masukan salah!\nSilahkan pilih menu lagi\n")
        Kode()
        
    # jika perintah yang di input ada pada syntaks if & elif , maka program selanjutnya akan berjalan kesini "input jumlah pesanan"
    jumlah = int(input("Masukkan jumlah Pesanan\t\t\t\t: "))
   
    # perhitungan item yang sudah dipesan dan apa yang sudah di input otomatis akan di tambahkan ke list yang sudah di buat sebelumnya dengan perintah ".append"
    subtotal = harga * jumlah
    total.append(subtotal)
    listnama.append(nama)
    listjp.append(jumlah)
    listharga.append(harga)
 
# fungsi disini untuk menyimpan sebuah data dari "Tanya()" yang mana bisa kita panggil kapanpun dijika diperlukan, digunakan untuk lanjut pesan atau tidak
def Tanya():
    print(62*"-")
    tanya = input("Mau pesan lagi? pilih Y jika Ya, pilih T jika Tidak [Y/T] : ")
    print("\r")
    if tanya == "y" or tanya == "Y":
        ulang()
        Kode()
    elif tanya == "t" or tanya == "T":
        Take_dine()
    else:
        print("Pilihan yang anda masukan salah!")
        print("Silahkan input kembali pilihan anda\n")
        Tanya()


# fungsi disini untuk menyimpan sebuah data dari "Take_dine()" yang mana bisa kita panggil kapanpun dijika diperlukan, digunakan untuk memilih take away atau dine in
def Take_dine():
    take_dine = input("Take Away / Dine In ? pilih Y jika Take Away, pilih T jika Dine In [Y/T] : ")
    if take_dine == "y" or take_dine == "Y":
        take()
        list_pembelian()
        akhir()
    elif take_dine == "t" or take_dine == "T":
        nomeja=input("Input Nomor Meja [1-20] : ")
        dine(nomeja)
        list_pembelian()
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")
        print("Silahkan input kembali pilihan anda\n")
        Tanya()
    
# fungsi disini untuk menyimpan sebuah data dari "take()" yang mana bisa kita panggil kapanpun dijika diperlukan, digunakan untuk menampilkan menu pesanan take away
def take():
    print("\r")
    print("|{:^66}|".format(66*"="))
    print("|{:^66}|".format('Selamat Datang di Rajanya Restoran'.upper()))
    print("|{:^66}|".format('daftar menu pesanan'.upper()))
    print("|{:^66}|".format(66*"="))
    print("|{:^66}|".format('take away'.upper()))
    print("|{:^66}|".format(66*"="))


# fungsi disini untuk menyimpan sebuah data dari "take()" yang mana bisa kita panggil kapanpun dijika diperlukan, digunakan untuk menampilkan menu pesanan dine in
def dine(nomeja):
    print("\r")
    print("|{:^66}|".format(66*"="))
    print("|{:^66}|".format('Selamat Datang di Rajanya Restoran'.upper()))
    print("|{:^66}|".format('daftar menu pesanan'.upper()))
    print("|{:^66}|".format(66*"="))
    print("|{:>43}{:<23}|".format('dine in - nomor meja : '.upper(),nomeja))
    print("|{:^66}|".format(66*"="))

# fungsi disini untuk menyimpan sebuah data dari "list_pembelian()" yang mana bisa kita panggil kapanpun dijika diperlukan
def list_pembelian():

    # ditambahkan waktu terkini pada tampilan total pesanan, untuk kebutuhan pada struk kasir
    import time;
    localtime = time.asctime(time.localtime(time.time()))
    tgl="Tanggal :"
    kasir=("Kasir : Raja")
    print("| {:<10}{:<23}{:>30} |".format(tgl,localtime,kasir))
    print("|{:^66}|".format(66*"="))
    print("|{:^4}|{:^27}|{:^8}|{:^11}|{:^12}|".format(' No','Nama','Jumlah','Harga','Subtotal'))
    print("|{:^66}|".format(66*"="))

    # fungsi zip() digunakan untuk membentuk iterator berisi item dengan cara mendapatkan iterable (bisa satu atau lebih) yang kemudian digabungkan ke dalam tuple dan dikembalikan.
    # iterables – bisa satu atau lebih iterator seperti iterator bawaan python (built-in iterables) string, list, tuple, dict dan lain-lain atau iterator yang ditentukan oleh pengguna (user-defined iterables)
    count=1
    for nama,jp,harga in zip(listnama,listjp,listharga) :
        print("|{:^4}| {:<26}|{:^8}|{:^11}|{:>11} |".format(count,nama,jp,harga,harga*jp))
        count = count + 1
    print("|{:^66}|".format(66*"="))

# fungsi disini untuk menyimpan sebuah data dari "akhir()" yang mana bisa kita panggil kapanpun dijika diperlukan
def akhir():

    # fungsi sum() berfungsi untuk menjumlahkan semua bilangan atau item yang menjadi argumennya.
    total1=sum(total)
    pajak=int(total1*0.10)
    total2=int(pajak+total1)
    print("|{:^43}{:<10}|{:>11} |".format('', 'Subtotal',total1))
    print("|{:^43}{:<10}|{:>11} |".format('', 'Pajak 10%',pajak))
    print("|{:^43}{:<10}|{:>11} |".format('', 'Total',total2))
    print("|{:^66}|".format(66*"="))
    print("\r")
    print("Total Harga Pesanan \t: Rp",total2)
    uang=int(input("Masukkan nominal uang \t: Rp "))
    print(37*"-")

    # statment jika jumlah uang lebih besar dari pada total pesanan
    if uang > total2 :
        print("Kembalian \t\t: Rp", uang - total2)
        print(37*"-")
        print("Terima Kasih Sudah Belanja Di Restoran Kami :)\n")
        print("Cetak Struk Berhasil...\n")
        Ask()

    # statment jika jumlah uang sama dengan total pesanan
    elif uang == total2:
        print("Kembalian \t\t: Rp 0")
        print(37*"-")
        print("Terima Kasih Sudah Belanja Di Restoran Kami :)\n")
        print("Cetak Struk Berhasil...\n")
        Ask()

    # statment jika jumlah uang kurang dari total pesanan
    elif uang < total2:

        # Perulangan dimana ketika uang yang di input kurang dari total pesanan maka perulangan akan terus terjadi(selama kondisinya true)
        while(True):
            print("Uang tidak cukup Rp", uang - total2,"\nMohon tambahkan kekurangannya")
            print(37*"-")
            uang=int(input("Masukkan nominal uang anda : Rp "))
            if uang == total2:
                print("Kembalian \t\t: Rp 0")
                print(37*"-")
                print("Terima Kasih Sudah Belanja Di Restoran Kami :)\n")
                print("Cetak Struk Berhasil...\n")
                Ask()
            elif uang > total2 :
                print("Kembalian \t\t: Rp", uang - total2)
                print(37*"-")
                print("Terima Kasih Sudah Belanja Di Restoran Kami :)\n")
                print("Cetak Struk Berhasil...\n")
                Ask()
    
# function untuk menanyakan apakah hendak lanjut ke program awal atau keluar dari program
def Ask():
    ask=(input("Pilih Y jika Lanjut, pilih T untuk Keluar Program [Y/T] : "))
    if ask == "Y" or ask == "y":
        print("\r")

        # fungsi .clear, berfungsi untuk menghapus semua data yang ada pada list, yang sudah di tentukan listnya
        listnama.clear()
        listharga.clear()
        listjp.clear()
        total.clear()
        daftar_pesanan()
        Pesan()
    elif ask == "T" or ask == "t":

        # fungsi exit() berfungsi untuk keluar dari program
        exit()
    else:
        print("Pilihan yang anda masukkan salah!")
        Ask()

# fungsi disini, yaitu untuk memanggil atau menampilkan tampilan menu yang ada pada fungsi "masuk()"
masuk()