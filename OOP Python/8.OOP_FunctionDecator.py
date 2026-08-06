def cetak_header_footer(func):
    def wrapper(self, *args, **kwargs):
        print("=" * 30)
        print("MENGAMBIL DATA MAHASISWA...")
        print("-" * 30)
        
        # Menjalankan fungsi aslinya (info_mahasiswa)
        hasil = func(self, *args, **kwargs)
        
        print("-" * 30)
        print("SELESAI")
        print("=" * 30)
        return hasil
    return wrapper

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

    # Menerapkan decorator pada method info_mahasiswa
    @cetak_header_footer
    def info_mahasiswa(self):
        print(f'Nama : {self.nama}')
        print(f'NIM  : {self.nim}')
        print(f'Univ : {self.univ}')

    @staticmethod
    def hey_maba(nama:str,univ:str):
        print(f'Halo {nama} selamat datang di {univ}')

mahasiswa_1 = Mahasiswa.create('Hafidz Akmal','A11202573','Universitas Dian Nuswantoro')
mahasiswa_1.info_mahasiswa()


        