n = int(input("Enter the length of the sequence: ")) # Do not change this line
numer1 = 1
numer2 = 2
numer3 = 3
numer4 = 0
print(1)
print(2)
print(3)

for x in range(n-3):
    numer4 = numer2 + numer3 + numer1
    print(numer4)
    numer1 = numer2
    numer2 = numer3
    numer3 = numer4