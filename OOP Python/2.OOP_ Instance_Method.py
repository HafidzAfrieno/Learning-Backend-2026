class Mahasiswa:
    def __init__(self):
        self.nama = ""
        self.nim = ""
        self.univ = ""
        self.umur= 0

    def info_mahasiswa(self):
        print(f'Nama: {self.nama}')
        print(f'NIM : {self.nim}')
        print(f'Umur: {self.umur}')
        print(f'Universitas : {self.univ}')

    def update_name(self,nama):
        self.nama = nama

All_mahasiswa = []

mahasiswa_udinus = Mahasiswa()
mahasiswa_udinus.nama = "Hafidz Akmal"
mahasiswa_udinus.nim = "A11.2025.16783"
mahasiswa_udinus.umur=20
mahasiswa_udinus.univ = "Udinus"
All_mahasiswa.append(mahasiswa_udinus)

mahasiswa_ugm = Mahasiswa()
mahasiswa_ugm.nama = "Budiono Siregar"
mahasiswa_ugm.nim = "A11567816783"
mahasiswa_ugm.umur=19
mahasiswa_ugm.univ = "UGM"
All_mahasiswa.append(mahasiswa_ugm)

mahasiswa_unnes = Mahasiswa()
mahasiswa_unnes.nama = "Yono Suptoroto"
mahasiswa_unnes.nim = "84308092A2342"
mahasiswa_unnes.umur=21
mahasiswa_unnes.univ= "Unnes"
All_mahasiswa.append(mahasiswa_unnes)

#memasukan data langsung ke class
Mahasiswa.update_name(mahasiswa_unnes,'Yono Subakrie')

for data in All_mahasiswa:
    data.info_mahasiswa()
    print('='*20)