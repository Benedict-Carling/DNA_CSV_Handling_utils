import pandas

read = pandas.read_csv(filepath_or_buffer='basic_parts_linkers.csv')
#print('data frame head\n')
#print(read.head())
#print('data frame index\n')
#print(read.index)
#print('data frame columns\n')
#print(read.columns)
print('data frame values\n')
print(read.values)

#for input in read.values:
#    print(input)
print('data frame values 1\n')
print(read.values[0])

def process(column):
    return [column[0],location[0],location[1:]]

process(read.values[0])
output = list(map(process,read.values))
print(output)




