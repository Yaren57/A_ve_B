#union birleşim
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)
#ortak olan rakamları tekrar yazmadan birleştirir
print(setA.union(setB))
#bu şekilde de yazılır
print(setB.union(setA))
#aynı sonucu verir


#intersection kesişim
print(setA & setB)
#kesişim kümesini yazar
print(setA.intersection(setB))
print(setB.intersection(setA))
#bu iki şekilde de yazılabilir


#set difference
#A'nın B'den farkı ya da tam tersi
print(setA - setB) #A'da olup B'de olmayanlar
print(setB - setA) #B'nin A'dan farkı
print(setA.difference(setB))
print(setB.difference(setA))


#symmetric difference
#A'nın B'den farkıyla B'nin A'dan farkını birleştirir
#Yani tüm kümeden kesişim kısmı çıkarır
print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
