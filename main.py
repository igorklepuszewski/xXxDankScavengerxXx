
def calculate(usb_size, memes):
    # conversion to MiB
    usb_size *= 1024
    # array usb_size x len(memes)
    sub_solutions = [[0 for w in range(usb_size + 1)]
                     for i in range(len(memes) + 1)]
    # checking first i-th elements
    for i in range(len(memes)+1):
        for w in range(usb_size+1):
            if i == 0 or w == 0:
                sub_solutions[i][w] = 0
            # checking if i-th element fits into usb_drive
            elif memes[i-1][1] <= w:
                # choosing the best way to fill the drive of size w
                sub_solutions[i][w] = max(
                    memes[i-1][2]+sub_solutions[i-1][w-memes[i-1][1]], sub_solutions[i-1][w])
            else:
                sub_solutions[i][w] = sub_solutions[i-1][w]

    # retriving the max worth of memes that can fit into the usb_drive
    max_value = sub_solutions[len(memes)][usb_size]

    # generating the set of memes to upload to usb_drive
    output_memes = set()
    result = max_value
    capacity = usb_size
    for i in range(len(memes), 0, -1):
        # there is no memes that their size is less or equal 0, so break the loop
        if result <= 0:
            break
        # the result is included only when it comes from "memes[i-1][2]+sub_solutions[i-1][w-memes[i-1][1]]"
        if result == sub_solutions[i-1][w]:
            continue
        else:
            # adding the name of meme to output_memes
            output_memes.add(memes[i-1][0])
            # decrementing the result by the price of meme that was added to output_memes
            result -= memes[i-1][2]
            # decrementing the capacity by the size of meme that was added to output_memes
            capacity -= memes[i-1][1]

    # generating output list
    output = (max_value, output_memes)
    # returning output
    return output
