class Mahasiswa :
    def __init__(self,nama='',nim='',prodi='',ipk=0.0,sks=0):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

        self.__ipk = ipk
        self.__sks = sks

    def data_diri(self):
        print(f'Nama:{self.nama}')
        print(f'Nim: {self.nim}')
        print(f'Prodi: {self.prodi}')
        print(f'Saudara {self.nama} Mengambil Sebanyak {self.__sks} SKS Dengan Ipk {self.__ipk}')

mahasiswa_ugm = Mahasiswa('Jokowi','43424AD','Fakultas Kehutanan',3.5,21)
mahasiswa_ugm.data_diri()