import math

key = 8

def encrypt(string):
    global key
    string_length = math.ceil(len(string) / key)
    encrypted_message = [["" for i in range(key)]for j in range(key)]
    for i in range(string_length):
        for j in range(key):
            if (((i * key) + j) % 8) == 0:
                encrypted_message[i][j] = string[i*key]
            else:
                if (i * key) + j < len(string):
                    encrypted_message[i][j] = string[j+(i*key)]
                else:
                    continue
        print(encrypted_message[i])
    final_message = ""
    for i in range(key):
        for j in range(string_length):
            final_message += encrypted_message[j][i]
    return final_message

def main():
    msg = encrypt("Common sense is not so common.")
    print("Encrypted message :",msg)

main()