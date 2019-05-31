

def calculate(usb_size, memes):
    # conversion to MiB
    usb_size *= 1024
    # array usb_size x len(memes)
    a = [[0]*usb_size for i in range(len(memes))]
    # declaration of set that will have set of memes to load into usb-drive
    set_of_memes = set()

    # checking first i elements
    for i in range(len(memes)):
        for j in range(usb_size):
            # checking if i-th element can be packed into the usb-drive of size j
            if(memes[i][1] > j):
                a[i][j] = a[i-1][j]
                set_of_memes.add(memes[i][0])
            else:
                a[i][j] = max(a[i-1][j], a[i-1][j-memes[i][1]]+memes[i][2])
    output = (a[len(memes)-1][usb_size-1], set_of_memes)
    return output


#name, size, price
memes = [
    ('rollsafe.jpg', 205, 6),
    ('sad_pepe_compilation.gif', 410, 10),
    ('yodeling_kid.avi', 605, 12)
]
usb_size = 20
print(calculate(usb_size, memes))
