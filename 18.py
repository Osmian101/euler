input = [75], [95], [64], [17], [47], [82], [18], [35], [87], [10],[20], [4], [82], [47], [65], [19], [1], [23], [75], [3], [34], [88], [2], [77], [73], [7], [63], [67], [99], [65], [4], [28], [6], [16], [70], [92], [41], [41], [26], [56], [83], [40], [80], [70], [33], [41], [48], [72], [33], [47], [32], [37], [16], [94], [29], [53], [71], [44], [65], [25], [43], [91], [52], [97], [51], [14], [70], [11], [33], [28], [77], [73], [17], [78], [39], [68], [17], [57], [91], [71], [52], [38], [17], [14], [91], [43], [58], [50], [27], [29], [48], [63], [66], [4], [68], [89], [53], [67], [30], [73], [16], [69], [87], [40], [31], [4], [62], [98], [27], [23], [9], [70], [98], [73], [93], [38], [53], [60], [4], [23]

def main():
    pyramid_print(input)
    traverse(input)

    print("row = x, y =") 

def traverse(input):
    y = -2 
    # y = 0  -> left side
    # y = -1 -> right side (with offset that wont matter)
    # y = 1  -> left side +1 (not perfect)
    # y = -2 -> right side -1 (capturing the end of input with
    #   negative indicies at first
    mult = 0

    # x = 1 -> left side
    # x = 2 -> center
    # x = 3 -> right side
    for x in range(1, len(input)):
        x = x * mult
        
        if x == len(input):
            print("end of line")
            return 1
        elif x > len(input):
            print("missed final entry")
            return 0
        else:
            print(int(x), ': ', input[int(x) + y])
        mult = mult + .5


def pyramid_print(input):
    i = 0
    x = 0
    for num in input:
        print(num, end=" ")
        if (x == i):
            print("")
            x = 0
            i = i + 1
        else:
            x = x + 1

main()
