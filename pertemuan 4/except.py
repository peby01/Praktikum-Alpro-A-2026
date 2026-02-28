#syntax dasar
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print('Error: Tidak bisa membagi dengan nol!')

#menangkap beberapa exception
try:
    angka = int(input('Masukkan angka: '))
    hasil = 100 / angka
except ValueError:
    print('Error: Input harus berupa angka!')
except ZeroDivisionError:
    print('Error: Tidak bisa membagi dengan nol!')
except Exception as e:
    print(f'Error tidak terduga: {e}')

#else dan finnaly
try:
    angka = int(input('Masukkan angka positif: '))
    if angka < 0:
        raise ValueError('Angka harus positif!')
    hasil = 100 / angka
except ValueError as e:
    print(f'Input tidak valid: {e}')
except ZeroDivisionError:
    print('Angka tidak boleh nol!')
else:
    print(f'Berhasil! Hasil = {hasil}')
finally:
    print('Proses selesai.')

#raise dan custom exception
class UmurTidakValidError(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f'Umur {umur} tidak valid. Harus antara 0-150.')


def validasi_umur(umur):
    if umur < 0 or umur > 150:
        raise UmurTidakValidError(umur)
    return True


try:
    validasi_umur(200)
except UmurTidakValidError as e:
    print(f'Error: {e}')

#fungsi input
nama = input('Masukkan nama Anda: ')
umur = int(input('Masukkan umur Anda: '))
tinggi = float(input('Masukkan tinggi (m): '))

#kombinasi input dan try-except
def input_angka(pesan, tipe='int'):
    while True:
        try:
            nilai = input(pesan)
            if tipe == 'int':
                return int(nilai)
            elif tipe == 'float':
                return float(nilai)
        except ValueError:
            print(f'Input tidak valid! Masukkan angka {tipe}.')

umur = input_angka('Masukkan umur Anda: ', 'int')
berat = input_angka('Masukkan berat badan (kg): ', 'float')
print(f'Umur: {umur}, Berat: {berat} kg')

