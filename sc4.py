nama = input("Masukkan nama anda : ")
print("Selamat datang", nama)
data_buku = {
    "buku1": {
        "judul": "Kancil dan Buaya",
        "penulis": "Rina Sari",
        "tahun_terbit": 2020
    },
    "buku2": {
        "judul": "Petualangan Si Kecil",
        "penulis": "Dina Putri",
        "tahun_terbit": 2021
    },
    "buku3": {
        "judul": "Dongeng Sebelum Tidur",
        "penulis": "Andi Pratama",
        "tahun_terbit": 2022
    }
}
while True:
    print("\n=== MENU PENGELOLAAN DATA BUKU ===")
    print("1. Tampilkan Data Buku")
    print("2. Tambahkan Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        print("\n=== DATA BUKU ===")
        for key, buku in data_buku.items():
            print("\n", key)
            print("Judul        :", buku["judul"])
            print("Penulis      :", buku["penulis"])
            print("Tahun Terbit :", buku["tahun_terbit"])
            if "penerbit" in buku:
                print("Penerbit     :", buku["penerbit"])

    elif pilihan == "2":
        print("\n=== TAMBAH DATA PENERBIT ===")
        print("1. Kancil dan Buaya")
        print("2. Petualangan Si Kecil")
        print("3. Dongeng Sebelum Tidur")
        pilih_buku = input("Pilih buku: ")
        if pilih_buku == "1":
            penerbit = input("Masukkan penerbit: ")
            data_buku["buku1"]["penerbit"] = penerbit
            print("Data penerbit berhasil ditambahkan menjadi : ", penerbit)
        elif pilih_buku == "2":
            penerbit = input("Masukkan penerbit: ")
            data_buku["buku2"]["penerbit"] = penerbit
            print("Data penerbit berhasil ditambahkan menjadi :  ", penerbit)

        elif pilih_buku == "3":
            penerbit = input("Masukkan penerbit: ")
            data_buku["buku3"]["penerbit"] = penerbit
            print("Data penerbit berhasil ditambahkan menjadi : ", penerbit)

        else:
            print("Pilihan buku tidak tersedia.")
    elif pilihan == "3":
        print("\n=== UBAH DATA PENULIS ===")
        kode = input("Masukkan kode buku (buku1/buku2/buku3): ")
        if kode in data_buku:
            penulis_baru = input("Masukkan penulis baru: ")
            data_buku[kode]["penulis"] = penulis_baru

            print("Data penulis berhasil diubah menjadi : ", penulis_baru)
        else:
            print("Kode buku tidak ditemukan.")

    elif pilihan == "4":
        print("\n=== HAPUS DATA PENERBIT ===")
        kode = input("Masukkan kode buku (buku1/buku2/buku3): ")
        if kode in data_buku:
            if "penerbit" in data_buku[kode]:
                data_buku[kode].pop("penerbit")
                print("Data penerbit berhasil dihapus.")
            else:
                print("Buku tersebut belum memiliki data penerbit.")
        else:
            print("Kode buku tidak ditemukan.")

    elif pilihan == "5":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak tersedia.")

print("\n=== DATA BUKU SETELAH PERUBAHAN ===")
for key, buku in data_buku.items():
    print("\n", key)
    print("Judul        :", buku["judul"])
    print("Penulis      :", buku["penulis"])
    print("Tahun Terbit :", buku["tahun_terbit"])

    if "penerbit" in buku:
        print("Penerbit     :", buku["penerbit"])