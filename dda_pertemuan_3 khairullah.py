# -*- coding: utf-8 -*-
"""DDA pertemuan 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M52-6XgGgTOEgc7HtYzIAPH0C67WeXxe
"""

aList = ["Kay", 19,"Serpong", True]
print (aList)

"""Latihan 1"""

DataMahasiswa = ["Khairullah Nurfitri Ramadhan", 2021071009,"INFORMATIKA","Desain dan Analisis Algoritma", "14/09/2022","Universitas Pembangunan Jaya", True]
print ("Mahasiswa = ",DataMahasiswa)

"""Contoh Colors"""

bin_Colors=['Red','Green','Blue','Yellow']
bin_Colors[3]

"""Latihan 2"""

DataMahasiswa[1]

"""Latihan 3"""

DataMahasiswa[5]

"""kalo misalnya mau mengambil 4 warna maka harus mencetak[0:4] , 0 itu dihitung dari indek 0,1,2,3 kalo misalnya 4 itu jumlah warnanya dimulai dari 1 = red"""

bin_Colors=['Red','Green','Blue','Yellow']
bin_Colors[2:4]

"""Latihan 4"""

DataMahasiswa [1:3]

"""contoh color forloop"""

bin_Colors=['Red','Green','Blue','Yellow']
for aColor in bin_Colors:
  print(aColor + " Square")

"""Latihan 5"""

bin_List=["UPJ"]
for namakampus in bin_List:
  print(namakampus + " Mahasiswa")
  print(namakampus + " bintaro")

"""tuples"""

bin_colors=('Red','Green','Blue','Yellow')
bin_colors[1]

bin_colors[2:]

"""Latihan 6"""

bin_List=('UPJ','Universitas','Pembangunan','Jaya')
bin_List[:4]

"""Latihan 7"""

nested_tuple=(100,(200,400,600),(300),(400,800))
print(nested_tuple)

"""dictionary"""

bin_colors ={"Manual Color":"Yellow","Approved Color":"Green","Refused_color":"Red"}
print(bin_colors)

bin_colors ={"Approved_Color":"Green"}
bin_colors.get("Approved_Color")
bin_colors["Approved_Color"]

bin_colors["Approved_Color"]="Purple"
print(bin_colors)
{"Manual_Color":"Yellow",
 "Approved_Color":"Purple",
 "Refused_Color":"Red"}

"""Latihan 8"""

Datamahasiswa={
    "Nama" : "Khairullah Nurfitri Ramadhan",
    "NIM"  : "2021071009",
    "Prodi" : "Informatika",
    "Universitas" : "UPJ"
}
print(Datamahasiswa)

green = {"grass","leaves"}
print(green)

saya = {"pulang","pengen","pengen"}
print(saya)

"""Latihan 9"""

yellow = {"dandelions","fire hydrant","blood","rose","leaves"}
red = {"fire hydrant"}

yellow|red
yellow&red

"""dataframe"""

import pandas as pd
df = pd.DataFrame([
    ["1","Fares",32,True],
    ["2","Elena",23,False],
    ["3","Steven",40,True]])

df.columns = ["id","name","age","decision"]
df

"""matrix"""

myMatrix=np.array([[11,12,13],[21,22,23],[31,32,33]])
print(myMatrix)