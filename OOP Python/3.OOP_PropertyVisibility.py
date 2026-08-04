class Mahasiswa:
    def __init__(self,nama,nim,namaIbu,namaAyah,nomorRekening,nomorKtp):
        # Visibility Public:
        self.nama =nama
        self.nim = nim

        # Visibility Protected (_):
        self._namaIbu = namaIbu
        self._namaAyah = namaAyah

        #Visibility Private (__):
        self.__nomorRekening = nomorRekening
        self.__nomorKtp = nomorKtp

    def info_mahasiswa(self):
        print(f'Nama: {self.nama}\n')
        print(f'NIM : {self.nim}\n')

    def tampilkan_rekening(self):
        print(f'Jumalh Saldo: {self.__nomorRekening}\n')

class OrtuMahasiswa(Mahasiswa):
    def tampilakan_ortu(self):
        print(f'Nama Ibu : {self._namaIbu}\n')
        print(f'Nama Ayah : {self._namaAyah}\n')

mahasiswa_semarang = Mahasiswa('hafidz','432kdf','DDYH','Hryt',4234432,19392)

mahasiswa_semarang.info_mahasiswa()
mahasiswa_semarang.tampilkan_rekening()

ortu_mahasiswa = OrtuMahasiswa('hafidz', '432kdf', 'DDYH', 'Hryt', 4234432, 19392)
ortu_mahasiswa.tampilakan_ortu()