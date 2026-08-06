class Mahasiswa :
    tahun = 1988
    presiden = 'Suharto'

    def __init__(self,nama='',nim='',prodi='',ipk=0.0,sks=0):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

        self.__ipk = ipk
        self.__sks = sks

    def data_diri(self):
        print('='*20)
        print(f'Mahasiswa ini Berkuliah Tahun {self.tahun} masa Kepemimpinan {self.presiden}')
        print(f'Nama:{self.nama}')
        print(f'Nim: {self.nim}')
        print(f'Prodi: {self.prodi}')
        print(f'Saudara {self.nama} Mengambil Sebanyak {self.__sks} SKS Dengan Ipk {self.__ipk}')

all_mahasiswa = []

mahasiswa_ugm = Mahasiswa('Jokowi','43424AD','Fakultas Kehutanan',3.5,21)
all_mahasiswa.append(mahasiswa_ugm)

mahasiswa_ugm = Mahasiswa('Prabowo','24324AD','Fakultas Kedokteran',3.1,22)
all_mahasiswa.append(mahasiswa_ugm)

mahasiswa_ugm = Mahasiswa('Hafidz Akmal','A112538','Fakultas Informatika',4.0,21)
mahasiswa_ugm.tahun = 2025
mahasiswa_ugm.presiden = 'Prabowo'
all_mahasiswa.append(mahasiswa_ugm)

for all in all_mahasiswa:
    all.data_diri()