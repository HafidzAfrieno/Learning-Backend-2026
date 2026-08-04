class Mahasiswa:
    def __init__(self):
        self.nama = ""
        self.nim = ""
        self.umur= 0

mahasiswa_udinus = Mahasiswa()
mahasiswa_udinus.nama = "Hafidz Akmal"
mahasiswa_udinus.nim = "A11.2025.16783"
mahasiswa_udinus.umur=20
print(f"Nama {mahasiswa_udinus.nama} memiliki NIM {mahasiswa_udinus.nim} dan berusia {mahasiswa_udinus.umur}")

mahasiswa_ugm = Mahasiswa()
mahasiswa_ugm.nama = "Budiono Siregar"
mahasiswa_ugm.nim = "A11567816783"
mahasiswa_ugm.umur=19
print(f"Nama {mahasiswa_ugm.nama} memiliki NIM {mahasiswa_ugm.nim} dan berusia {mahasiswa_ugm.umur}")

mahasiswa_unnes = Mahasiswa()
mahasiswa_unnes.nama = "Yono Suptoroto"
mahasiswa_unnes.nim = "84308092A2342"
mahasiswa_unnes.umur=21
print(f"Nama {mahasiswa_unnes.nama} memiliki NIM {mahasiswa_unnes.nim} dan berusia {mahasiswa_unnes.umur}")

