import sys
import numpy as np


class Theater:
    def __init__(self):
        self.seats = np.empty([10, 20], dtype=object)

    def parse_file(self, content):
        print(content[4:])
        return content[4:]

    def find_seat(self, char_seats):
        num_seats = int(char_seats)

        found_seats = []
        counter = 0
        for row in range(0, len(self.seats)):
            for seat in range(0, len(self.seats[row])):
                if (counter != seat):
                    found_seats = []
                    counter = seat + 1
                    continue
                if (len(found_seats) >= num_seats):
                    return found_seats
                if (self.seats[row][seat] == None):
                    found_seats.append([row, seat])
                    counter += 1
            counter = 0
        return []

    def buy_seat(self, num_seats):
        booked = self.find_seat(num_seats)
        if (booked == []):
            return []
        first = booked[0]
        last = booked[-1]
        return [first, last]


theater = Theater()
theater.seats[0][1] = "hi"
print(theater.seats)

filepath = sys.argv[1]

with open(filepath) as fp:
    line = fp.readline()
    while line:
        num_tix = theater.parse_file(line.strip())
        final_seats = theater.buy_seat(num_tix)
        print(final_seats)
        line = fp.readline()
