def fiboncci(number):
    counter = 0
    count = [0, 1]
    if number == 0:
        print(0)
    else:
        while counter < number - 1:
            n = count[-1] + count[-2]
            count.append(n)
            counter += 1
        print(count[-1])
