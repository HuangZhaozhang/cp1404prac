import csv
with open("countries.csv") as in_file:
    reader = csv.reader(in_file)
    header = next(reader)
    sorted_records = sorted(reader,key=lambda record: record[0])
    for record in sorted_records:
        country = record[0]
        capital = record[1]
        population = f"{int(record[2]):,}"
        percentage = record[3]
        print(f"{country:<15}-{capital:<10},{population:>15},{percentage:>3}%")