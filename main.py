import Equation

width = input("Width")
if width == "":
    print("try a number")
    input()
else:
    length = input("length")
    if length == "":
        print("try a number")
        input()
    else:
        turns = input("Number of turns")


width = int(width)
length = int(length)
turns = int(turns)

if length > turns*3.1416*width:
    result = turns*((((length/turns)**2)-((3.1416*width)**2))**(.5))

    result = round(result, 2)

    print(result)
    input()
else:
    print("Doesnt math... try a length bigger than the number of turns times pi times the width")
    print("A length too close to this value (turns*pi*width) will result in a crash")
    input()