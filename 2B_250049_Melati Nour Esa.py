def main():
    print("")
    print("================================Jasmine Library================================")
    print("=======================SELAMAT DATANG DI DUNIA PERBUKUAN=======================")
    print("===============================================================================")
    print("==Kalian bisa menikmati waktu kalian dengan tenang sambil membaca buku disini==")
    print("==========Diizinkan untuk meminjam buku sesuai dengan aturan yang ada==========")
    print("====================Silahkan isi formulir peminjaman disini====================")
    nama=input("Nama Peminjam  :")
    telp=input("No. Telepon    :")
    Alamat=input("Alamat Rumah :")
    Judul=input("Judul Buku    :")
 
    print("===Batas peminjaman hanya satu minggu, lewat dari batas ketentuan mendapat denda===")
    
    Bts_pinjam=input("Batas Peminjaman  :")
    tlt_pgbln=int(input("Masukan waktu telat pengembalian  :"))
    jml_pmjm=int(input("Masukan Jumlah Peminjaman  :"))

    if  tlt_pgbln>=11:
        denda=7000
        jumlah=int(tlt_pgbln*denda)
    elif tlt_pgbln>=6:
        denda=6000
        jumlah=int(tlt_pgbln*denda)
    elif tlt_pgbln>=1:
        denda=5000
        jumlah=int(tlt_pgbln*denda)
    else:
        denda=0

    total=jml_pmjm*jumlah

    print("Total:",total)

    print("=====================================================================================")

    print("============Terjadi kerusakan pada buku,bayar sesuai dengan jenis buku============")

    print("\n-----Jenis Buku-----")
    print("1. Buku Science")
    print("2. Buku Sejarah")
    print("3. Novel")
    print("4. Komik")
    print("5. Self Development")
    print("6. Misteri")

    pilihan=int(input("\nMasukan Pilihan  :"))

    if pilihan==1:
        print("Harga= 150000")
        nm_buku="Buku Science"
    elif pilihan==2:
        print("Harga= 140000")
        nm_buku="Buku Sejarah"
    elif pilihan==3:
        print("Harga= 120000")
        nm_buku="Novel"
    elif pilihan==4:
        print("Harga= 110000")
        nm_buku="Komik"
    elif pilihan==5:
        print("Harga= 100000")
        nm_buku="Self Development"
    elif pilihan==6:
        print("Harga= 95000")
        nm_buku="Misteri"
    else:
        print("Barang tidak ditemukan..!")

    print("============================TERIMAKASI ATAS KERJA SAMANYA==============================")

    
main()
    
