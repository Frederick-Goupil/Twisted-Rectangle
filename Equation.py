def calculate():
    def equation(turns, length, width):

        result = turns*((((length/turns)**2)-((3.1416*width)**2))**(.5))
        return(result)
    x = 0
    t = 1
    i = 1
    
    dictionary = {}
    dictionary["x"] = range(0, 10000)
    while t <= 9:
        i = 1
        while i <= 9:
            j = 0
            mylist = []
            while j < 10000:
                num = equation(t, j, i*10)
                str_num = str(num)
                str_num = str_num[:7]
                str_num = str_num.replace('(', '')
                mylist.append(float(str_num))
                j = j + 1
                x += 1
            dictionary[str((i*10)+(t*100))] = mylist
            i += 1
        t += 1
    return dictionary
