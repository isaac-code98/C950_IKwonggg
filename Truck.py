# Class Truck and all of its respective properties
class Truck:
    def __init__(self, max_speed, miles_traveled, max_load, packages, address, depart_time, is_finished):
        self.max_speed = max_speed
        self.miles_traveled = miles_traveled
        self.max_load = max_load
        self.packages = packages
        self.address = address
        self.depart_time = depart_time
        self.is_finished = is_finished
        self.trip_time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s," % (self.max_speed, self.miles_traveled, self.max_load, self.packages,
                                                self.address, self.depart_time, self.is_finished)
