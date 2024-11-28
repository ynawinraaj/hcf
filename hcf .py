#find hcf or gcd
#enter two number
num_large=int(input("enter the large number: "))
num_small=int(input("enter a small number: "))

#using eucliden algorithum
while(num_small):
    numberstore=num_small
    num_small=num_large % num_small
    num_large=numberstore
print("HCF of the given numbers is :",num_large)