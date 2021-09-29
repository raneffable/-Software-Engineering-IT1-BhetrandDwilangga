#List
print("Ini List :")
contoh_list =["Alvin",12,12.0,[1,2,3],{},{},True]
print(contoh_list[0])
print(contoh_list[-4])
contoh_list.append("David")
contoh_list.insert(3,"Dian")
print(contoh_list)
print("SortData : ")
list_angka = [1,4,7,9,8]
list_angka.sort() #besar ke kecil
print(list_angka)
list_angka.sort(reverse = True ) #kecil ke besar
print(list_angka)
list_angka.pop() #hilang yg plg blakang
print(list_angka)
list_angka.remove(7) #hilangin 7
print(list_angka)
#Dictionary
print("\nIni dictionary :")
contoh_dictionary = {1:"Alvin","hai":12, False:12.0, 2:[1,2,3], 20.1:{},20.2:(),"hoho":True}
print(contoh_dictionary[1])
print(contoh_dictionary[20.1])
print(contoh_dictionary["hoho"])
print(contoh_dictionary.keys())

#Operator
print("\n Ini Operator ngab :")
a=5
b=2
print("Operator :")
print(a+b)
print(a-b)
print(a*b)
print(a/b) #float  division
print(a//b) #integer division
print(a**b) #pangkat
print(a%b)
#Conditional Statement
print("\nIni Conditional ngab :")
print(a<b)
print(a>=b)
print(a==b)
print(a!=b)
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print("\nIF ini ngab :")
c = 10
d = 5
e = 7
if c>d and c>e :
    print("C nilai terbesar")
elif d>c and d>e :
    print("D nilai terbesar")
elif e>d and e>c :
    print("E nilai terbesar")
else :
    print("semua nilai sama")

#Looping
print("\nLooping nehh")
a=6
b=3
while b<a :
    print("b akan tambah 1 teros sampe sama kek a")
    print("b")
    b += 1
#ini buat user input
# while True:
#     umur = int(input("Masukan umur kao:"))
#     if umur <20:
#         break

for i in range(2):
    print(i)
print("-----")
for i in range(3,11,2):
    print(i)
    if i == 4:
        break
else:
    print("uda sampe 11, 11 nya ke else")