print("=== APLIKASI KASIR RESTORAN (LANGSUNG STRUK) ===")

# 1. Tampilkan Daftar Menu
print("\n--- DAFTAR MENU CAFE ---")
print("1. Burger          - Rp35.000")
print("2. Kentang Goreng  - Rp20.000")
print("3. Spaghetti       - Rp30.000")
print("4. Es Kopi Susu    - Rp15.000")
print("5. Lemon Tea       - Rp12.000")

# 2. Input Pilihan Menu dan Jumlah dari Pengguna
pilihan = int(input("\nPilih Menu (Masukkan angka 1-5): "))
jumlah = int(input("Masukkan Jumlah Pesanan: "))

# 3. Menentukan Harga Berdasarkan Pilihan (if-elif-else)
harga = 0
if pilihan == 1:
    harga = 35000
elif pilihan == 2:
    harga = 20000
elif pilihan == 3:
    harga = 30000
elif pilihan == 4:
    harga = 15000
elif pilihan == 5:
    harga = 12000
else:
    print("Pilihan tidak valid! Program dihentikan.")
    exit() # Menghentikan program jika input salah

# 4. Hitung Total Belanja dan Diskon Langsung (20%)
total_belanja = harga * jumlah
persen_diskon = 20
potongan = total_belanja * 0.20
total_bayar = total_belanja - potongan

# 5. Tampilkan Struk Pembayaran Akhir
print("\n==============================")
print("       STRUK PEMBAYARAN       ")
print("==============================")
print(f"Total Belanja : Rp {total_belanja:,}")
print(f"Diskon        : {persen_diskon}%")
print(f"Potongan      : Rp {potongan:,}")
print("------------------------------")
print(f"Total Bayar   : Rp {total_bayar:,}")
print("==============================")
print("         Terima Kasih         ")
print("==============================")