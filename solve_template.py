def solve(ciphertext):
    """
    Given ECB ciphertext, recover the password
    """
    

    with open(ciphertext, "rb") as f:
        data = f.read()

    if len(data) % 16 != 0:
        data += "00" * (16 - (len(data) % 16))


    chunks = [data[i:i+16].hex() for i in range(0,len(data), 16)]

    unique = []
    repeat = []

    for i in range(len(chunks)):
        if (chunks[i] not in unique):
            unique.append(chunks[i])
        elif (chunks[i] not in repeat):
            repeat.append(chunks[i])
    
    for i in range(len(repeat)):
        if (repeat[i] in unique ):
            unique.remove(repeat[i])
    
    print("Unique: ")
    for i in range(len(unique)):
        print(unique[i] + " ")


    print("Repeating: ")
    for i in range(len(repeat)):
        print(repeat[i] + " ")

#solve(input("Enter in the ciphertext: "))

solve("challenge.bin")
