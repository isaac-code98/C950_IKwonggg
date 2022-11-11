import csv
import datetime
import Truck
from Package import Package
from CreateHashTable import CreateHashTable

# Initialize a new hash table that will contain all of our packages
package_hashtable = CreateHashTable()

# Initialize separate arrays pertaining to each truck that will hold its respective packages
first_truck_packages = []
second_truck_packages = []
third_truck_packages = []

# Reader that will parse and feed the data from the package_file
# Time complexity: O(n)
# Space complexity: O(n)
with open("csv/PackageFile.csv") as package_file:
    package_data = csv.reader(package_file, delimiter=',')
    for package in package_data:
        p_id = int(package[0])
        p_address = package[1]
        p_city = package[2]
        p_state = package[3]
        p_zip = package[4]
        p_cutoff = package[5]
        p_mass = package[6]
        p_notes = package[7]
        if package[7] == '':
            p_notes = "No special requirements/notes"
        else:
            p_notes = package[7]
        p_position = "Package is at WGUPS."

        package_object = Package(p_id, p_address, p_city, p_state, p_zip, p_cutoff, p_mass, p_notes, p_position)

        # ** REVISION I2/K1 **
        # As the algorithm was sufficient and competent, I have simply changed how we will sort the packages into each
        # truck to satisfy the correct delivery times for packages 25, 34, 37, 40.

        # If statement to first check we aren't exceeding the truck's max load
        if len(first_truck_packages) < 16:
            # Re-implemented a new if-else statement because I only want packages that have a cut-off time of 9:00
            # or 10:30 and also who's flights are not delayed. Packages 13, 14, 15, 16, and 20 all have a cutoff
            # time of 9:00 - 10:30, however package 19 is EOD, but I still want it included within these big bundle of
            # packages, so I add that specific ID to the truck as well
            if package_object.cutoff_time == "10:30 AM" and \
                    package_object.notes != "'Delayed on flight---will not arrive to depot until 9:05 am'":
                first_truck_packages.append(package_object.pkg_id)
            elif package_object.pkg_id == 19:
                first_truck_packages.append(package_object.pkg_id)
            elif package_object.cutoff_time == "9:00 AM":
                first_truck_packages.append(package_object.pkg_id)

        # If statement to first check we aren't exceeding the truck's max load
        if len(second_truck_packages) < 16:
            # This if one giant if-else statement is a bit convoluted in the sense that I want as many EOD packages as
            # I can fit into truck 2 but also preserve some space while looping to allocate those spots to respective
            # packages 36 and 38 which need to be on truck 2. So within this loop, packages 4, 5, 6, 8, 11, 12 would be
            # added on truck 3 per it's multi-level if-else statement to make room for 36 and 38

            # Also, we are excluding any of the packages on delayed flights since I want these to be on truck 2 with a
            # departure time of 9:05, also we want to add the respective "truck 2" packages onto the truck and also
            # since it will be 10:20 at the earliest when this truck can depart we can respectively update the wrong
            # address to the correct one once it leaves.

            if package_object.cutoff_time == "EOD" and \
               package_object.notes != "'Delayed on flight---will not arrive to depot until 9:05 am'" and \
               package_object.notes != "'Wrong address listed'" and \
               package_object.pkg_id != 4 and \
               package_object.pkg_id != 5 and \
               package_object.pkg_id != 7 and \
               package_object.pkg_id != 8 and \
               package_object.pkg_id != 11 and \
               package_object.pkg_id != 12 and \
               package_object.pkg_id != 19:
                second_truck_packages.append(package_object.pkg_id)
            elif package_object.notes == "'Wrong address listed'":
                package_object.address = "410 S State St"
                package_object.city = "Salt Lake City"
                package_object.state = "UT"
                package_object.zipcode = "84111"
                second_truck_packages.append(package_object.pkg_id)
            elif package_object.notes == "'Can only be on truck 2'":
                second_truck_packages.append(package_object.pkg_id)

        # If statement to first check we aren't exceeding the truck's max load
        if len(third_truck_packages) < 16:
            # I've condensed and limited the scope of the multi-level if statement that was here before and opted
            # to simply include those packages which will not arrive to WGUPS until 9:05 AM which will ultimately depart
            # at earliest time 9:05. And since the overall balance of the pre-sorted packages was weighed heavily
            # towards truck 1 and 2 I opted to place any remaining packages into truck 3, so for the messiness that
            # we incur in the looping of truck 2, this is where we save a bit of code and mess as we'll be able to add
            # those excluded IDs in truck 2 to truck 3

            if package_object.notes == "'Delayed on flight---will not arrive to depot until 9:05 am'":
                third_truck_packages.append(package_object.pkg_id)
            elif package_object.pkg_id not in first_truck_packages:
                if package_object.pkg_id not in second_truck_packages:
                    third_truck_packages.append(package_object.pkg_id)

        package_hashtable.insert(p_id, package_object)

# Create instance of Truck class, load respective packages, and set respective departure times
first_truck = Truck.Truck(18, 0.0, 16, first_truck_packages, "4001 South 700 East",
                          datetime.timedelta(hours=8, minutes=0, seconds=0), False)

# Create instance of Truck class, load respective packages, and set respective departure times
# I have also now set the departure time of truck 2 to 10:20:00
second_truck = Truck.Truck(18, 0.0, 16, second_truck_packages, "4001 South 700 East",
                           datetime.timedelta(hours=10, minutes=20, seconds=0), False)

# Create instance of Truck class, load respective packages, and set respective departure times
# I have also now set the departure time of truck 3 to 09:05:00
third_truck = Truck.Truck(18, 0.0, 16, third_truck_packages, "4001 South 700 East",
                          datetime.timedelta(hours=9, minutes=5, seconds=0), False)
