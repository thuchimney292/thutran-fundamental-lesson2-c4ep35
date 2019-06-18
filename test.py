# text = 'hello'
# t = len(text) == 5
# print(t)
# n = int (input("nhap so n: "))
# year=int(input("nhap nam sinh: "))
# age=2019-year
# if age>=18:
#     print("adult")
# elif age<=12:
#     print('baby')
# else:
#     print("teenager")
#i=1
# import time
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             print(i,j,k)
#             time.sleep(1)
# for i in range(1,101):
#     print(i,end=' ')
# print()
# for i in range(100,106):
#     print(i,end=' ')
# print()
n=int(input('nhap n='))
s=0
for i in range(1,n+1):
    s=s+1/i
print(s)
s=1
gt=1
for i in range(1,n+1):
    gt=gt*i
    s=s+1/(gt)
print(s)

