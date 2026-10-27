#variabel dan tipe data

print("============nilai mahasiswa===========")
nalgoritma = 90
nagama = 90
nbasisdata = 90
npancasila = 90
nmatematika = 80
nbahasa = 85
npemograman = 90

# nama_mhs = "kanaya"
# kelas = "C1"


namamhs = input("masukkan nama mahasiswa :")
nilaialgo = int(input("masukkan nilai algoritma :"))
nilaiagama = int(input("masukkan nilai agama :"))
nilaibasisdata = int(input("masukkan nilai basis data :"))
nilaipancasila = int(input("masukkan nilai pancasila :"))
nilaimatematika = int(input("masukkan nilai matematika :"))
nilaibahasa = int(input("masukkan nilai bahasa :"))
nilaipemograman = int(input("masukkan nilai pemograman :"))


rata_rata = (nilaialgo + nilaiagama + nilaibasisdata + nilaipancasila + nilaimatematika + nilaibahasa + nilaipemograman) / 7
print(rata_rata)
#nilai = int(input("masukkan nilai:"))

# penentuan lulus atau tidak
if rata_rata >=85 and rata_rata<=100:
    #kondisi jika terpenuhi
    #maka
    print("nilai : A")
elif rata_rata>=60 and rata_rata <=85:
    print("nilai : B")
elif rata_rata >=50 and rata_rata <=70:
    print("nilai : C")
elif rata_rata >=20 and rata_rata <=45:
    print("nilai : D") 
else:
    # cukup menampilkan hasil
    # maka
    print("nilai lebih dari 100 atau dibawah 50")