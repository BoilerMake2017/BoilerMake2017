import csv


def split_file(file):
    reader = csv.reader(file)
    for row_num, row in enumerate(reader, 1):
        if (row_num % 2 != 0) {
            last_line_1 = open('cad_1.csv', 'a')
            last_line_1.write(row)
        } else {
            last_line_2 = open('cad_2.csv', 'a')
            last_line_2.write(row)
        }

# def csv_writer(data, file):
#     last_line = open(file_name, 'a'):
#         write = csv.writer(csv_file, delimiter=',')
#         reader = csv.reader(file)
#         for row_num, row in enumerate(reader):
#             writer.writerow(row)
#             row_num = row_num + 2


with open("cad.csv", "rb") as f_obj:
    split_file(f_obj)
