import sys
import csv
from idgenerator import IdGenerator


def usage():
    print('python3 make_a_csv.py file_name id_num')


if len(sys.argv) < 3:
    usage()
    sys.exit(1)

file_name = sys.argv[1]
id_num = int(sys.argv[2])
id_generator = IdGenerator()
with open(file_name, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for _ in range(id_num):
        writer.writerow([id_generator.generate(['L'])])

