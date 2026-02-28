#penanganan indeks list

angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

#2
def pembagian():
    a = input ("masukkan angka pertama :", "int")
    b = input ("masukkan angka kedua :", "int")
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("pembagi tidak boleh nol")
    else:
        print (f"hasil : {hasil}")
    finally:
        print("selesai")