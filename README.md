# Postest_1
Nama:Fadhil Ahmad Khairan
NIM:2309116071
Sistem Informasi B

![Screenshot 2023-09-25 232932](https://github.com/Fadhilllak/Postest_1/assets/146011121/c036ef3a-7e89-4e88-87af-d8611887b5c0)

![Screenshot 2023-09-25 232943](https://github.com/Fadhilllak/Postest_1/assets/146011121/f6970074-ebfe-4bc0-b81a-d70e299a3f73)

![Screenshot 2023-09-26 000028](https://github.com/Fadhilllak/Postest_1/assets/146011121/4a079a69-e83a-4720-90e5-e473fc425057)
foto di atas adalah tampilan menu awal

![Screenshot 2023-09-26 000123](https://github.com/Fadhilllak/Postest_1/assets/146011121/df417274-0eb8-4fd9-a007-485681d9e6f9)
Setelah itu masukan nama dan nim

![Screenshot 2023-09-26 000207](https://github.com/Fadhilllak/Postest_1/assets/146011121/c8a75d73-1629-4622-ac7d-168c2c584e4e)
berikut adalah daftar mata uang yaitu dollar,yen,ringgit

![Screenshot 2023-09-26 000231](https://github.com/Fadhilllak/Postest_1/assets/146011121/6c37b617-d6d4-4b77-988f-3dbe4a463953)
Ini adalah tampilan memilih dollar sebesar 20 ribu

![Screenshot 2023-09-26 000310](https://github.com/Fadhilllak/Postest_1/assets/146011121/74adef03-244a-4fee-b8f7-6b274761b0d8)
Ini adalah tampilan memilih yen sebesar 20 ribu
![Screenshot 2023-09-26 000319](https://github.com/Fadhilllak/Postest_1/assets/146011121/2e0dff0a-5ebc-4f18-9ee6-a3fa0b8cf994)
lanjutan dari yen

![Screenshot 2023-09-26 000342](https://github.com/Fadhilllak/Postest_1/assets/146011121/20faf624-cfa8-4f0a-b716-2cc6d48cfd56)
Ini adalah tampilan dari ringgit

![Screenshot 2023-09-26 000426](https://github.com/Fadhilllak/Postest_1/assets/146011121/2d6afebe-4ff5-4ba9-b238-3ecd03231ffa)
dan ini adalah tampilan terakhir yaitu angka 4 untuk menyelesaikan nya


Beerikut adalah codingan nya
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

