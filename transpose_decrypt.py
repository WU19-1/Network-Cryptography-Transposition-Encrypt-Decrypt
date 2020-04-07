import math
key = 8

def decrypt(string):
    global key
    string_length = math.ceil(len(string) / key)
    final_string = ""
    
    empty_box = key * string_length - len(string)


    grid = [["" for i in range(string_length)]for j in range(key)]

    x = 0
    for i in range(key):
        nums = 0
        if i >= (key - empty_box):
            nums = string_length - 1
        else:
            nums = string_length
        for j in range(nums):
            try:
                grid[i][j] = string[x]
                x += 1
            except IndexError as identifier:
                pass
        print(grid[i])

    for i in range(string_length):
        for j in range(key):
            final_string += grid[j][i]
            
    return final_string

def main():
    msg = decrypt("Cenoonommstmme oo snnio. s s c")
    print(msg)
main()