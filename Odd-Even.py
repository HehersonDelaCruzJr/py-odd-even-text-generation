# Opening the Text file
file = open("Integers.txt", "rt")
for i in file:
    if i.strip:
        num = int(i)
        
        #Segregate the numbers in the "Integers.txt" 
        # if it's even or odd then will create a file for even and odd numbers
        if (num % 2 == 0):
            even = open("even.txt", "a")
            even.write(str(num))
            even.write("\n")
        else:
            odd = open("odd.txt", "a")
            odd.write(str(num))
            odd.write("\n")

