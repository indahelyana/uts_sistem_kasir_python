# =====================================
# SISTEM KASIR SEDERHANA
# Menggunakan konsep OOP Python
# =====================================

# CLASS BARANG
class Barang:
    jumlah_barang = 0

    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga  # Encapsulation
        Barang.jumlah_barang += 1

    # Property untuk mengambil harga
    @property
    def harga(self):
        return self.__harga

    # Setter untuk mengubah harga
    @harga.setter
    def harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
        else:
            print("Harga harus lebih dari 0!")

    # Class Method
    @classmethod
    def total_barang(cls):
        return cls.jumlah_barang

    # Static Method
    @staticmethod
    def format_rupiah(angka):
        return f"Rp{angka:,.0f}".replace(",", ".")


# CLASS KASIR
class Kasir:
    def __init__(self):
        self.daftar_barang = [
            Barang("Buku", 5000),
            Barang("Pulpen", 3000),
            Barang("Pensil", 2000),
            Barang("Penghapus", 1500),
            Barang("Penggaris", 4000)
        ]

    # Method menampilkan barang
    def tampilkan_barang(self):
        print("\n===== DAFTAR BARANG =====")

        for nomor, barang in enumerate(self.daftar_barang, 1):
            print(
                f"{nomor}. {barang.nama} - "
                f"{Barang.format_rupiah(barang.harga)}"
            )

    # Method proses pembelian
    def proses_pembelian(self):
        self.tampilkan_barang()

        try:
            pilihan = int(input("\nPilih nomor barang: "))

            if pilihan < 1 or pilihan > len(self.daftar_barang):
                print("Pilihan tidak tersedia!")
                return

            barang = self.daftar_barang[pilihan - 1]

            jumlah = int(input("Masukkan jumlah pembelian: "))

            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                return

            total = barang.harga * jumlah

            print("\n===== TOTAL PEMBELIAN =====")
            print("Nama barang :", barang.nama)
            print("Jumlah      :", jumlah)
            print("Total       :", Barang.format_rupiah(total))

            bayar = int(input("Uang pembayaran: Rp"))

            if bayar < total:
                print("Uang pembayaran tidak cukup!")
                return

            kembalian = bayar - total

            print("\n===== STRUK PEMBELIAN =====")
            print("Nama barang :", barang.nama)
            print("Jumlah      :", jumlah)
            print("Total       :", Barang.format_rupiah(total))
            print("Bayar       :", Barang.format_rupiah(bayar))
            print("Kembalian   :", Barang.format_rupiah(kembalian))
            print("===========================")
            print("Terima kasih sudah berbelanja!")

        except ValueError:
            print("Masukkan angka yang benar!")


# PROGRAM UTAMA
def main():
    kasir = Kasir()

    print("================================")
    print("       SISTEM KASIR")
    print("================================")

    print("Total jenis barang:",
          Barang.total_barang())

    while True:
        print("\n1. Tampilkan Barang")
        print("2. Pembelian")
        print("3. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            kasir.tampilkan_barang()

        elif pilihan == "2":
            kasir.proses_pembelian()

        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()