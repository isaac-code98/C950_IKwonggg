# Class Package and all the respective properties
class Package:
    def __init__(self, pkg_id, address, city, state, zipcode, cutoff_time, mass, notes, position):
        self.pkg_id = pkg_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.cutoff_time = cutoff_time
        self.mass = mass
        self.notes = notes
        self.delivery_time = None
        self.position = position
        self.depart_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.pkg_id, self.address, self.city, self.state,
                                                           self.zipcode, self.cutoff_time, self.mass, self.notes,
                                                           self.delivery_time, self.position)

    # Method to update the position of the package given a time to compare that is passed in as the parameter and its
    # current time whether the package has been delivered, en route, or at hub
    def set_position(self, time_to_compare):
        if self.depart_time > time_to_compare:
            self.position = "Package is en route."
        elif self.delivery_time < time_to_compare:
            self.position = "Package was delivered."
        else:
            self.position = "Package is at WGUPS."
