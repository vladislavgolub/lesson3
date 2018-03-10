import csv

with open ('data-398-2018-02-13.csv', 'r', encoding='cp1251') as station_data:
    counter = 0
    fields = {}
    reader = csv.DictReader(station_data, delimiter=';')
    reader_1 = csv.reader(station_data, delimiter=';', quotechar='"')
    for station in reader_1:
        counter += 1
    for street in reader:
        fields[street['Street']] = fields.get(street['Street'],0) + 1
    print(fields)



print('Число остановок:', counter)
