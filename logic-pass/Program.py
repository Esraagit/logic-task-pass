print('Enter the range of number')
start=int(input("start="))
end=int(input("End="))
print("Prime numbers: ")
prime=[]
if start==1:
    start=2
for num in range(start,end):
    check=True
    for i in range(2,num):
        if num%i==0:
            check=False
    if check:
        prime.append(num)

print(prime)
        

        

        
