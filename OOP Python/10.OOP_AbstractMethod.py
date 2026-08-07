class Mahasiswa:
    def tampil_mahasiswa():
        pass

class Mahasiswa_Baru(Mahasiswa):
    def __init__(self,nama : str,nim : str):
        self.tugas = 'ospek'
        self.nama = nama
        self.nim = nim

    def tampil_mahasiswa(self):
        print(f'Saudara {self.nama} dengan NIM {self.nim} Adalah MABA Yang Sedang {self.tugas}')

class Mahasiswa_Lama(Mahasiswa):
    def __init__(self,nama : str,nim : str):
        self.tugas = 'Skirpsi'
        self.nama = nama
        self.nim = nim

    def tampil_mahasiswa(self):
        print(f'Saudara {self.nama} dengan NIM {self.nim} Adalah MAKIR Yang Sedang {self.tugas}')

mahasiswa_1 = Mahasiswa_Baru('hafidz akmal','A11202548')
mahasiswa_2 = Mahasiswa_Lama('Budiono','A1378983')

mahasiswa_1.tampil_mahasiswa()
mahasiswa_2.tampil_mahasiswa()