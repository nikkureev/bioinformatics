def cop(in_file, out_file, start, end):
    with open(in_file, 'a') as o:
        with open(out_file, 'r') as i:
            for j in range(end):
                r = i.readline()
                if j >= start:
                    o.writelines(r)
