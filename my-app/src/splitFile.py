import csv
import pandas as pd


def split_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row_num, row in enumerate(reader, 1):
            row_str = (','.join(map(str, row)))

            row_str = row_str.replace('\t', ',')
            row_str = row_str.replace('  ', ',')
            row_str = row_str.replace(' ', ',')
            if row_num % 2 != 0:
                last_line_1 = open('cad_1.csv', 'a')
                last_line_1.write(row_str + "\n")
            else:
                last_line_2 = open('cad_2.csv', 'a')
                last_line_2.write(row_str + "\n")
            # if row_num >= 10:
            #     break


split_file("cad.csv")
train = pd.read_csv('cad_1.csv')

# cad_1.csv comes with column titles, cad_2.csv does not
