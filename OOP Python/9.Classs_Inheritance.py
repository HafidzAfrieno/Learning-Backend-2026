class Mahasiswa:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def tampil_umur(self):
        print(f'Suadara {self.nama} Umurnya adalah {self.umur}')

class Nilai_Mahasiswa(Mahasiswa):
    def __init__(self,nama,umur,ipk):
        super().__init__(nama,umur)
        self.ipk = ipk

    def tampil_nilai(self):
        print('='*20)
        self.tampil_umur()
        print(f'Saudara {self.nama} dan umurnya {self.umur} mendapatkan IPK {self.ipk}')

IPk_mahasiswa_1 = Nilai_Mahasiswa('Hafidz Akmal',20,3.8)
IPk_mahasiswa_1.tampil_nilai()