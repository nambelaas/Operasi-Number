import numpy

arr_num = []

n = int(input("Masukkan jumlah elemen: "))

for i in range(0, n):
    ele = int(input())
    arr_num.append(ele)

print(arr_num)
print("\n")

s_num = sorted(arr_num)

print("Diurutkan menjadi: ")
print(s_num)

print("\n")
print("Median dari array diatas: ")

m_num = numpy.mean(s_num)
print(m_num)

print("\n")
print("Total array setelah dikalikan: ")

t_num = numpy.prod(s_num)
print(t_num)