#Capstone Project Modul 1
#Menu Rental Mobil
#Sultan Rafif Ghazali
#Data Science & Machine Learning

def main_menu():
    while True:
        # Tampilkan opsi menu
        print("\nSelamat Datang Di Rental Mobil Sejahtera:")
        print("1. Lihat Semua Data Rental Mobil")
        print("2. Menambahkan Data Rental Mobil")
        print("3. Mengganti Data Rental Mobil")
        print("4. Menghapus Data Rental Mobil")
        print("5. Save Data")

        # Minta input dari pengguna
        choice = input("Pilihlah opsi angka (1-5): ")

        # Pilihan tidak valid
        if choice not in ['1', '2', '3', '4', '5']:
            print("Opsi yang anda masukkan tidak valid. Silahkan coba kembali")
            continue  # kembali ke awal loop untuk meminta input lagi

        # Eksekusi opsi yang dipilih
        if choice == '1':
            lihat_semua_data_rental_mobil()
        elif choice == '2':
            menambahkan_data_rental_mobil()
        elif choice == '3':
            mengganti_data_rental_mobil()
        elif choice == '4':
           menghapus_data_rental_mobil()
        elif choice == '5':
            print("Data Sudah Tersimpan")
            break

def lihat_semua_data_rental_mobil():
    data = [
        {"id": 1, "nama": "Mobil A", "harga": 200000},
        {"id": 2, "nama": "Mobil B", "harga": 300000},
    ]
    while True:
        print("\nMenu Menampilkan Data.")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan ID")
        print("3. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan Anda (1-3): ")

        if pilihan == '1':
            tampilkan_semua_data(data)
        elif pilihan == '2':
            cari_data_berdasarkan_id(data)
        elif pilihan == '3':
            main_menu()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tampilkan_semua_data(data):
    if not data:
        print("Data tidak ditemukan.")
    else:
        for item in data:
            print(item)

def cari_data_berdasarkan_id(data):
    id_cari = input("Masukkan ID yang ingin dicari: ")
    hasil = [item for item in data if item['id'] == int(id_cari)]
    if hasil:
        for item in hasil:
            print(item)
    else:
        print("Data tidak ditemukan.")

def menambahkan_data_rental_mobil():
    data = []

    while True:
        print("\nMenu Menambahkan Data")
        print("1. Tambahkan data baru")
        print("2. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan Anda (1-2): ")

        if pilihan == '1':
            id = input("Masukkan id: ")
            nama = input("Masukkan nama: ")
            harga = input("Masukkan harga: ")

            # Cek apakah data dengan ID yang sama sudah ada
            data_ada = False
            for item in data:
                if item['id'] == id:
                    print("Data dengan ID yang sama sudah ada!")
                    data_ada = True
                    break

            if not data_ada:
                data_baru = {"id": id, "nama": nama, "harga": harga}
                data.append(data_baru)
                print("Data berhasil disimpan!")
            
        elif pilihan == '2':
            main_menu()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def mengganti_data_rental_mobil():
    data = [
        {"id": 1, "nama": "Mobil A", "harga": 200000},
        {"id": 2, "nama": "Mobil B", "harga": 300000},
    ]
    while True:
        print("\nMenu Mengganti Data")
        print("1. Update data")
        print("2. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan Anda (1-2): ")

        if pilihan == '1':
            id_update = input("Masukkan ID data yang ingin diubah: ")

            # Cari data berdasarkan ID
            data_found = data
            for item in data:
                if item["id"] == id_update:
                    data_found = item

            if data_found:
                print("Data ditemukan:")
                print(data_found)

                # Konfirmasi update
                konfirmasi = input("Apakah Anda ingin melanjutkan update? (y/n): ")
                if konfirmasi.lower() == 'y':
                    kolom = input("Masukkan nama kolom yang ingin diubah: ")
                    nilai_baru = input("Masukkan nilai baru: ")

                    # Update data
                    data_found[kolom] = nilai_baru
                    print("Data berhasil diupdate!")
                else:
                    print("Update dibatalkan.")
            else:
                print("Data tidak ditemukan.")

        elif pilihan == '2':
            main_menu()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def menghapus_data_rental_mobil():
    data = [
        {"id": 1, "nama": "Mobil A", "harga": 200000},
        {"id": 2, "nama": "Mobil B", "harga": 300000},
    ]

    while True:
        print("\nMenu Penghapusan Data")
        print("1. Hapus data")
        print("2. Kembali ke menu utama")

        pilihan = input("Masukkan pilihan Anda (1-2): ")

        if pilihan == '1':
            id_hapus = input("Masukkan ID data yang ingin dihapus: ")

            # Cari data berdasarkan ID
            data_found = None
            for index, item in enumerate(data):
                if item['id'] == id_hapus:
                    data_found = index
                    break

            if data_found is not None:
                print("Data ditemukan:")
                print(data[data_found])

                # Konfirmasi penghapusan
                konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                if konfirmasi.lower() == 'y':
                    del data[data_found]
                    print("Data berhasil dihapus!")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print("Data tidak ditemukan.")

        elif pilihan == '2':
            main_menu()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
  
