def cek_ganjil_genap(angka: int) -> str:
    """Mengembalikan 'Genap' jika angka genap, dan 'Ganjil' jika ganjil."""
    if not isinstance(angka, int):
        raise TypeError("Input harus berupa bilangan bulat (integer)")
    return "Genap" if angka % 2 == 0 else "Ganjil"


def main():
    print("Program Pengecek Ganjil / Genap")
    try:
        input_user = input("Masukkan angka: ")
        angka = int(input_user)
        hasil = cek_ganjil_genap(angka)
        print(f"Angka {angka} adalah {hasil}")
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

