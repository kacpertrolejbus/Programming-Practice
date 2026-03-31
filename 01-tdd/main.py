def Add(number):
    if number == "":
        return 0
    else:
        n = number.replace("\n", ",").split(",")
        print(n)
        sum = 0
        for i in n:
            sum += int(i)
        print(sum)
        return sum

Add("1, 2")