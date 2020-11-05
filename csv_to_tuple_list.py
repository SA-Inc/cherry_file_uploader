from csv import reader

with open('MAGNUM.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
    print(list_of_rows)