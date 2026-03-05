def solve(ciphertext):
    """
    Given ECB ciphertext, recover the password
    """
    

    with open(ciphertext, "rb") as f:
        data = f.read()

    chunks = [data[i:i+16].hex() for i in range(0,len(data), 16)]

    print(chunks)

solve(input("Enter in the ciphertext: "))
