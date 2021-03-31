

class PiDay:
    def __init__(self):
        self.months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sept", "Oct", "Nov", "Dev")
        self.day_of_the_month = range(0, 31)

    def find_pi_day(self, month, day):
        if month == self.months[2] and day == self.day_of_the_month[14]:
            print(f"piDay is {month} {day}!")

        else:
            return


Pi = PiDay()
Pi.find_pi_day("Mar", 14)


class BirthdayLocations:
    def __init__(self):
        self.locations = ("Lake", "House", "Vegas")
        self.future_locations = ("Beach", "Movie Theatre", "Dave n Busters")

    def add_locations(self):
        for location in self.locations:
            print(location)

        for future in self.future_locations:
            print(future)


locations = BirthdayLocations()
locations.add_locations()
