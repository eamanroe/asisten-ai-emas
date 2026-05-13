print("--- ASISTEN EMAS EA AKTIF ---")

while True:
    print("\n--- Cek Harga Baru ---")
    harga_input = input("Berapa harga XAU/USD sekarang? (atau ketik 'keluar' untuk berhenti): ")

    if harga_input.lower() == 'keluar':
        print("Asisten EA pamit. Selamat istirahat!")
        break

    harga = float(harga_input)
    if harga > 4715:
        print("Saran EA: Mahal banget, kawan! Tahan dulu BRoo.")
    elif harga < 4650:
        print("Saran EA: Murah nih! Gas POool?")
    else:
        print("Saran EA: Harga aman, pantau, jangan kasih kendor.")