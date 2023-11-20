def cek_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False
    return True

def buat_pola_unik(x):
    while x >= 10 and cek_prima(x):
        satuan_terakhir = x % 10
        x = (x - satuan_terakhir) // 10

    if cek_prima(x):
        print(f"Pola unik yang tersisa adalah {x}")
    else:
        print("Tidak ada pola unik yang sesuai")

x = int(input("Masukkan Bilangan bulat = "))
buat_pola_unik(x)