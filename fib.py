natural_number = input("Please specify a natural number for the range: ")

n = int(natural_number)

i = 0
j = 1

with open("fibonacci.txt", "w") as f:
    
    f.write("{}\n{}\n".format(i,j))

    while i+j <= n:
        z = i + j
        f.write("{}\n".format(z))
        i = j
        j = z
