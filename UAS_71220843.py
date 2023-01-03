print("****** Kredit Keaktiffan Mahasiswa ****** ")
print("(Student Activities Credit)")
print("1. Menambahkan Kegiatan")
print("2. Menampilkan Jumlah Poin")
print("3. Keluar")
print("-----------------------")
pi = (input("Silahkan masukan pilihan yang Anda: "))
if pi == "1":
    nm = input("Nama Kegiatan: ")
    tg = input("Tanggal Kegiatan: ")
    print("Pilihan Kategori Kegiatan: ")
    sa = print(" - Prestasi")
    du = print(" - Organisasi")
    ti = print(" - Kepanitian")
    em = print(" - Rekognisi")
    input("Masukkan Kategori Kegiatan: ")
    print("Kegiatan berhasil ditambahkan.")
elif pi == "2":
    print("-----------------------")
    print("Nama Kegiatan           Tanggal            Kategori         Poin ")     
    print("1. ")
    print("2. ")
    print("3. ")
elif pi == "3":
    print("-----------------------")
    print("Sistem Berhenti...")




