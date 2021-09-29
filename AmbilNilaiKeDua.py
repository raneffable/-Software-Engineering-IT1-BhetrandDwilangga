print("Helow welcome to mesin penghitung bilangan prima")
angka1= int(input("\nDari berapa ? :"))
angka2= int(input("Sampai berapa? :"))
angkaprima=[]

for i in range (angka1+1,angka2): #ditambah 1 biar angka1  gak masuk
    for j in range(2,i): #start dari 2 ,karna kalo dari 1 bakalan ga jalan.
        if (i % j) == 0: # ini buat ngecek prima, karna kalo ada yg %==0 brarti ga prima
            break
    else: #abis di cek di append ke list angkaprima
        angkaprima.append(i)
else: #akan stop ketika i dah menjadi angka2
    print("Angka Primanya Ini : ",angkaprima)






