print("=== REGISTRASI PESERTA SEMINAR ===")

try:
    nama = input_nama()
    umur = input_umur()
    email = input_email()
    nohp = input_nohp()

finally:
    print("Proses input selesai.")

print("\n=== DATA PESERTA ===")
print(f"Nama   : {nama}")
print(f"Umur   : {umur} tahun")
print(f"Email  : {email}")
print(f"No HP  : {nohp}")
print("Status : TERDAFTAR")