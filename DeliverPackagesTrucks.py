import datetime
from Distance import get_dist_between_truck_and_package
from SortAndLoadTrucks import package_hashtable
from SortAndLoadTrucks import first_truck
from SortAndLoadTrucks import second_truck
from SortAndLoadTrucks import third_truck

# Initialize arrays that will be used to store package objects from the hash table, respective to each truck
packages_tbd_1 = []
packages_tbd_2 = []
packages_tbd_3 = []


# Function which utilizes the packages to be delivered arrays as well as the trucks
# Time complexity: O(n)
# Space complexity: O(n)
def load_package_hash_table(truck, packages_to_be_delivered_arr):
    # Loop through each package id in the packages on the truck, grab each respective package from the hash table
    # and then append the entire package to the packages_to_be_delivered_arr
    for pkg_id in truck.packages:
        pkg = package_hashtable.search(pkg_id)
        packages_to_be_delivered_arr.append(pkg)


# Calling the functions above with each respective truck and each respective packages_tbd array
load_package_hash_table(first_truck, packages_tbd_1)
load_package_hash_table(second_truck, packages_tbd_2)
load_package_hash_table(third_truck, packages_tbd_3)


# ** REVISION B1: Additional comments can be found here **
# Function to deliver the packages given a truck and its respective packages to be delivered array
# Time complexity: O(n^2)
# Space complexity: O(n)
def deliver_packages(truck, packages_to_be_delivered):
    # Clear the respective truck's packages as the marker for if a package is actually delivered or not will be when
    # we add that package on to the truck and remove it from the packages_to_be_delivered array
    truck.packages.clear()

    # Implement a while loop that will only continue executing the following code whilst there are still packages to be
    # delivered in the packages_to_be_delivered array, if not, we can then say that the truck is finished delivering
    # all of its packages
    while len(packages_to_be_delivered) != 0:
        # Here we can initialize a placeholder closest_pkg and set it to none
        closest_pkg = None

        # Also initialize closest_address_distance and set it to an executable distance so that we can have a starting
        # point for the for loop to fire off
        closest_address_distance = 150

        # Loop through every package in the package_to_be_delivered array
        for each_pkg in packages_to_be_delivered:
            # If the distance between the truck's current address and the package's address is less than the closest
            # package's distance, we assign the new closest address distance to the distance between the truck and the
            # package, and assign the closest package to this current package within the for loop
            if get_dist_between_truck_and_package(truck.address, each_pkg.address) <= closest_address_distance:
                closest_pkg = each_pkg
                closest_address_distance = get_dist_between_truck_and_package(truck.address, each_pkg.address)

        # The following code will only execute once we have completed a full iteration of the for loop above, and we
        # have obtained the closest_pkg AKA the nearest neighbor package

        # Gets the distance traveled to this package and adds it to the respective truck's total miles traveled
        truck.miles_traveled = closest_address_distance + truck.miles_traveled

        # Here we set the trip time equal to the time it took for the specific truck to drive to the closest package
        # address that we specified
        truck.trip_time = datetime.timedelta(hours=closest_address_distance / 18) + truck.trip_time

        # Here we will simply set the current truck's address to the closest package to which it traveled to
        truck.address = closest_pkg.address

        # Appending the closest package id to the truck's package list (here, essentially marked as delivered)
        truck.packages.append(closest_pkg.pkg_id)

        # Here set the closest package's delivery time equal to the truck's trip time
        closest_pkg.delivery_time = truck.trip_time

        # Here we set the closest package's departure time to the truck's depart time
        closest_pkg.depart_time = truck.depart_time

        # Finally, we can remove the closest package from the packages_to_be_delivered list
        packages_to_be_delivered.remove(closest_pkg)

    # If statement that says the packages_to_be_delivered array is empty, we mark that truck is being finished with its
    # deliveries
    if len(packages_to_be_delivered) == 0:
        truck.is_finished = True


# Call the deliver_packages function with each respective truck and packages_tbd array, implement an if statement
# that only allows third truck to start delivering once either the first truck or second truck has finished delivering
# packages
deliver_packages(first_truck, packages_tbd_1)
deliver_packages(second_truck, packages_tbd_2)

if first_truck.is_finished is True or second_truck.is_finished is True:
    deliver_packages(third_truck, packages_tbd_3)

