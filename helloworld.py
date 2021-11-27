def print2(word, num=1):
    for x in range(num):
        print(f"{word} 2")


def pyramid(num=3):
    for x in range(num):
        row = ""
        while len(row) != int(x+1):
            row += "x"
        print(f"row {x+1}: {row}")
    for y in range(0, num-1):
        row = ""
        while len(row) != int(num - (y+1)):
            row += "x"
        print(f"row {num+y}: {row}")


print2("hello world", 5)

pyramid(5)
