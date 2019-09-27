import sys
import numpy as np


class Theater:
    def __init__(self):
        self.seats = np.empty([10, 20], dtype=object)

    def parse_file(self, content):
        print(content[4:])
        return content[4:]

    def find_seat(self, seats):
        return "hello"

    def buy_seat(self, seats):
        booked = self.find_seat(seats)
        first = booked[0]
        last = booked[-1]
        return


theater = Theater()
theater.seats[0][1] = "hi"
print(theater.seats)

filepath = sys.argv[1]

with open(filepath) as fp:
    line = fp.readline()
    while line:
        num_tix = theater.parse_file(line.strip())
        theater.buy_seat(num_tix)
        line = fp.readline()
