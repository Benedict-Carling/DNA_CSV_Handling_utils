import pandas

def constructs_to_combinations(filepath):
    read = pandas.read_csv(filepath_or_buffer=filepath)
    df_list = [i for i in read.values[0] if list(read.values[0]).index(i)%2==0]
    df = pandas.DataFrame(df_list)
    df.to_csv(filepath,header=None,index=False)

constructs_to_combinations('e_o_basic_constructs copy.csv')