def cop(in_file, out_file, start=0, end=len(in_file)):
    with open(in_file, 'a') as o:
        with open(out_file, 'r') as i:
            for j in range(end - 1):
                r = i.readline()
                if j >= start - 1:
                    o.writelines(r)
