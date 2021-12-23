# n = int(input("How many elements?"))
# x =[]
# for i in range(n):
#     x.append(int(input()))
# x.sort()  
# x.sort(reverse=True)  
# print(x)

# #count
# ls4 =[1,1,1,1,1,1,1,6,4,5]
# n = ls4.count(1)
# print(n)
#  #nested list
# ls2 =[12,36,[15,65]]
matrix = [[1,2,3],[4,5,6], [8,5,2]]

for r in matrix:
    for c in r:
        print(c, end='  ')
    print()    