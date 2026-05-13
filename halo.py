harga_input = input('Berapa harga XAU/USD sekarang? ')
harga = float(harga_input)
if harga >4715:
    print ('Saran AI : Harga sudah terlalu tinggi, jangan beli sekarang!')
elif harga <4650:
    print ('Saran AI : Harga sedang murah , peluang bagus untuk beli')
else:
    print ('Saran AI : Harga masih stabil, sebaiknya pantau dulu ya')