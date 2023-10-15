import os


# Kamus berisi pasangan nama dan NIM yang diizinkan untuk login
data_login = {
    "Fadil": "12345",
    "Fadhil Ahmad Khairan": "2309116071",
}

# Menu Login
def login():
    batas_percobaan = 3
    while batas_percobaan > 0:
        print("==================")
        print("|     LOGIN      |")
        print("==================\n")
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        os.system('cls')

        # Verifikasi nama dan NIM
        if nama in data_login and data_login[nama] == nim:
            print(f"\nSelamat datang, {nama}!\n")
            return True
        else:
            batas_percobaan -= 1
            if batas_percobaan == 2 or batas_percobaan == 1:
                print("\nSalah!")
                print(f"Anda memiliki {batas_percobaan} kesempatan lagi.\n")
            elif batas_percobaan == 0:
                print("\nAnda telah mencapai batas maksimal percobaan.\n")
                return False
                


# Konversi Mata Uang
def konversi(rupiah, mata_uang):
    nilai_tukar = {
        "USD": 0.00007,
        "Yen": 0.0078,
        "Ringgit": 0.00029
    }

    return rupiah * nilai_tukar[mata_uang]

# Tampilan Tabel Konversi
def tampilkan_tabel_konversi():
    print("\n========== TABEL KONVERSI ===========")
    print("| Mata Uang       | Nilai Tukar     |")
    print("|-----------------|-----------------|")
    print("| 1. USD          | 0.00007         |")
    print("| 2. Yen          | 0.0078          |")
    print("| 3. Ringgit      | 0.00029         |")
    print("| 4. Keluar       |                 |")
    print("|-----------------|-----------------|")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not login():
        return

    while True:  # Loop untuk kembali ke menu utama setelah konversi
        tampilkan_tabel_konversi()

        print("=== KONVERSI MATA UANG ===")
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

        if pilihan == 1:
            mata_uang = "USD"
        elif pilihan == 2:
            mata_uang = "Yen"
        elif pilihan == 3:
            mata_uang = "Ringgit"
        elif pilihan == 4:
            print("\nTerima kasih telah menggunakan program ini!")
            break  # Keluar dari loop dan mengakhiri program
        else:
            print("Pilihan tidak valid!")
            continue  # Kembali ke awal loop

        rupiah = float(input(f"\nMasukkan jumlah Rupiah yang ingin dikonversikan ke {mata_uang}: "))
        hasil = konversi(rupiah, mata_uang)
        print(f"\n{rupiah} Rupiah setara dengan {hasil} {mata_uang}\n")

        input("Tekan Enter untuk kembali ke menu utama...")  # Memberi kesempatan kepada pengguna untuk melihat hasil sebelum kembali ke menu
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "_main_":
    main()
