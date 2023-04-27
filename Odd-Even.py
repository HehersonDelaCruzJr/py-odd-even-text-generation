# Opening the Text file
file = open("Integers.txt", "rt")
for i in file:
    if i.strip:
        num = int(i)

        # print numbers
        print(num)
