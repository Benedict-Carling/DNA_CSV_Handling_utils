import pandas

def partslinkers_to_platemap_csv(filepath):
    read = pandas.read_csv(filepath_or_buffer=filepath)
    process = lambda column : [column[0],column[1][0],column[1][1:]]
    output = list(map(process,read.values))
    output.sort()
    perfect_format = []
    for i in range(len(output)//12+1):
        row_width = []
        print(i)
        for j in range(12):
            if i*12+j+1 > len(output):
                break
            else:
                print(i*12+j)
                row_width.append(output[i*12+j][0])
        perfect_format.append(row_width)
    df = pandas.DataFrame(perfect_format)
    df.to_csv(filepath,header=None,index=False)




