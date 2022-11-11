import csv
from Address import get_address

# Read and open the file of distance information
with open("csv/DistanceFile.csv") as csvfile:
    csv_distance = list(csv.reader(csvfile))


# Function for getting the distance between to addresses from the distance table/file
def get_dist_between(row, col):
    distance = csv_distance[row][col]
    if distance == '':
        distance = csv_distance[col][row]

    return float(distance)


# Function for retrieving the distance between the address of a truck and the address of a package
def get_dist_between_truck_and_package(truck_addy, package_addy):
    return get_dist_between(get_address(truck_addy), get_address(package_addy))
