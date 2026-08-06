class Mahasiswa:
    generasi = 'Gen-Z'
    def __init__(self,nama='',umur=0):
        self.nama = nama
        self.umur = umur

    @classmethod
    def create(cls,nama='',umur=0):
        obj = cls()
        obj.nama = nama
        obj.umur = umur
        return obj

    def info(self):
        print(f'seorang Mahasiswa Bernama {self.nama} Berumur {self.umur}')

mahasiswa_1 = Mahasiswa('Hafidz Akmal',20)
mahasiswa_2 = Mahasiswa.create('Afrieno',21)

mahasiswa_1.info()
mahasiswa_2.info()

mahasiswa_1.generasi = 'Gen-Y'

print(f'Mahasiswa Bernama {mahasiswa_1.nama} Dari Generasi {mahasiswa_1.generasi}')
print(f'Mahasiswa Bernama {mahasiswa_2.nama} Dari Generasi {mahasiswa_2.generasi}')