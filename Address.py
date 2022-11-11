import csv

# Open and read address file and assign to respective variable
with open("csv/AddressFile.csv") as csvfile1:
    csv_address = list(csv.reader(csvfile1))


# Method to get address number from string literal of address
def get_address(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])
