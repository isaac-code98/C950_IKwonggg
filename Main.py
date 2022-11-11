# Author: Isaac Kwong
# Student ID: 001230140
# Title: C950 Data Structures and Algorithms II
import datetime
from DeliverPackagesTrucks import first_truck
from DeliverPackagesTrucks import second_truck
from DeliverPackagesTrucks import third_truck
from DeliverPackagesTrucks import package_hashtable

# OVERALL time complexity: O(n^2)
# OVERALL space complexity: O(n)
# These complexity values are derived from the worst case scenario time which is from the NN algorithm, and the space
# complexity from everywhere else


# Class Main that provides the user interface
class Main:
    print("Welcome to Western Governor's University Parcel Service (WGUPS)!")
    print("Pick a choice from all of our menu options:")
    print("1. Get the total mileage for the route")
    print("2. Print all packages status (assuming WGUPS just opened)")
    print("3. Get a single package status with ID (assuming WGUPS just opened)")
    print("4. Get all packages status according to time")
    print("5. Get a single package status according to time")
    print("Please enter your numerical option down below")
    user_num = input()
    if user_num == "1":
        print("The total mileage for the route calculated is:")
        # Print the total mileage traveled by all trucks
        print(round(first_truck.miles_traveled + second_truck.miles_traveled + third_truck.miles_traveled))
    elif user_num == "2":
        # Here we loop through each package id, and input them into the search function of the hash table, and print
        # out the respective packages
        for pkg_id in range(1, 41):
            all_package = package_hashtable.search(pkg_id)
            print(str(all_package))
    elif user_num == "3":
        print("Please enter the numeric ID for the package you'd like to search:")
        single_package_search = input()
        # Here we take the user's input ID and plug that in to the hash table's search method as an integer and print
        # the respective package found
        single_package_found = package_hashtable.search(int(single_package_search))
        print(str(single_package_found))
    elif user_num == "4":
        print("Please enter a time at which to check the status of all packages. Use the time format of (HH:MM:SS)")
        all_package_time = input()
        hours, minutes, seconds = all_package_time.split(":")
        time_to_compare = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        # Here we take the user's inputted time and split into respective field times to loop through all the packages
        # whist updating each package's position by comparing the user's input time to either the package's departure or
        # delivery time, and then print out all the respective packages
        for pkg_id in range(1, 41):
            all_package = package_hashtable.search(pkg_id)
            all_package.set_position(time_to_compare)
            print(str(all_package))
    elif user_num == "5":
        print("Please enter the package ID to search for")
        single_package_search = input()
        print("Please enter a time at which to check the status of all packages. Use the time format of (HH:MM:SS)")
        single_package_time = input()
        # Here is essentially the same method as above except for the fact that we don't have to loop, we can just take
        # the user's input package id as well as the time, set the position of that package by comparison, and then
        # print out the respective package
        package = package_hashtable.search(int(single_package_search))
        hours, minutes, seconds = single_package_time.split(":")
        time_to_compare = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        package.set_position(time_to_compare)
        print(str(package))
