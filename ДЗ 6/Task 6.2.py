def cop(in_file, out_file, number_of_lines):
    r =''
    o = open(in_file, 'a')
    with open(out_file, 'r') as i:
        for j in range(number_of_lines):
            r += i.readline()
    print(r)
    o.writelines(r)
    o.close()
