#Sistem Registrasi Peserta Event

class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"Nama terlalu pendek! Minimal 3 karakter.")

class UmurError(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f"Umur tidak memenuhi syarat (17-60 tahun).")
        
def input_nama():
        while True:
            try:
                nama = input("Nama lengkap: ")
                if len(nama) < 3:
                    raise NamaError(nama)
                return nama
            except NamaError as e:
                print(f"[ERROR] {e}")

def input_umur():
    while True:
        try:
            umur = int(input("Umur: "))
            if umur < 17 or umur > 60:
                raise UmurError(umur)
            return umur
        except ValueError:
            print("[ERROR] Umur harus berupa angka!")
        except UmurError as e:
            print(f"[ERROR] {e}")

def input_email():
    while True:
        try:
            email = input("Email: ")
            if "@" not in email:
                raise ValueError("Email tidak valid! Harus mengandung '@'.")
            return email
        except ValueError as e:
            print(f"[ERROR] {e}")


def input_nohp():
    while True:
        try:
            nohp = input("No HP: ")
            if not nohp.isdigit():
                raise ValueError("No HP harus berupa angka.")
            if len(nohp) < 10 or len(nohp) > 13:
                raise ValueError("No HP tidak valid! Harus 10-13 digit angka.")
            return nohp
        except ValueError as e:
            print(f"[ERROR] {e}")


# PROGRAM UTAMA

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