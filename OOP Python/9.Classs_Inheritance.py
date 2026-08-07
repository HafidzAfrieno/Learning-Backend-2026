class Mahasiswa:
    def __init__(self,nama = 'none',umur = '0'):
        self.nama = nama
        self.umur = umur

    def tampil_umur(self):
        print(f'Suadara {self.nama} Umurnya adalah {self.umur}')

class Dosen_Wali(Mahasiswa):
    def __init__(self,dosen,**kwargs):
        super().__init__(**kwargs)
        self.dosen = dosen

    def tampil_dosen(self):
        print(f'Dosen Wali Saudara {self.nama} Bernama {self.dosen}')

class Nilai_Mahasiswa(Dosen_Wali,Mahasiswa):
    def __init__(self,ipk,nama,umur,dosen):
        super().__init__(nama=nama,umur=umur,dosen=dosen)
        self.ipk = ipk

    def tampil_nilai(self):
        print(f'Saudara {self.nama} dan umurnya {self.umur} mendapatkan IPK {self.ipk}')

IPk_mahasiswa_1 = Nilai_Mahasiswa('Hafidz Akmal',20,3.8,'Eko')

IPk_mahasiswa_1.tampil_umur()
IPk_mahasiswa_1.tampil_nilai()
IPk_mahasiswa_1.tampil_dosen()