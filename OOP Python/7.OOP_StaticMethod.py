class Mahasiswa:
    def __init__(self):
        self.nama   : str
        self.nim    : str
        self.univ   : str

    @classmethod
    def create(cls,nama='',nim='',univ=''):
        obj = cls()
        obj.nama = nama
        obj.nim  = nim
        obj.univ = univ
        return obj

    def info_mahasiswa(self):
        print('='*20)
        print(f'Nama: {self.nama}')
        print(f'NIM : {self.nim}')

    @staticmethod
    def hey_maba(nama:str,univ:str):
        print(f'Halo {nama} selamat datang di {univ}')

mahasiswa_1 = Mahasiswa.create('Hafidz Akmal','A11202573','Universitas Dian Nuswantoro')
mahasiswa_1.info_mahasiswa()
mahasiswa_1.hey_maba(mahasiswa_1.nama,mahasiswa_1.univ)

        