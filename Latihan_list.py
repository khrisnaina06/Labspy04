list=["a", "b", "c", "d", "e"]


print("Tampilkan Element ke 3:", list[2])
print("ambil Element ke 2 sampai 4:", list[1:4]) 
print("ambil elemen terakhir:", list[5-1])


# Merubah elemen ke-4 dengan nilai lain
list[3] = "f"
print("merubah elemen ke 4 dengan nilai lain:", list)
list[3:] = "f", "g" 
print("merubah elemen ke 4 sampai elemen terakhir:", list)



# Tambah elemen list
a=[1,2,3,4,5]
b=[6,7,8,9,10]

# Ambil 2 bagian list A ke list B
b.append(a[1:3])
print("2 bagian List A dijadikan List B:", b)

# Tambah list B dengan string
b.append("saya")
print("Tambah B dengan Sring:", b)

# Tambah list B dengan 3 nilai
print("Tambah list b dengan 3 nilai:", b+[11,12,13])
c=b+a

# Gabungan list B dan A 
print("Gabungan list B dan A:", c)
c=b+a
print("Gabungan list B dan A:", c)








