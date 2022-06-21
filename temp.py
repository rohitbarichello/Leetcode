string = "1010011000101010010100001011010100"

bits = int(string, base=2)
print(bits)

count = 0 

while bits > 0:
    count += 1
    
    bits = bits & (bits - 1)

    print("Number: ", bits)

print("Count: ", count)