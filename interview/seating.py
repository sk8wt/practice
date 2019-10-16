import sys
import os
import numpy as np


class Theater:
    def __init__(self):
        self.seats = np.empty([10, 20], dtype=object)
        self.seats_left = [20] * 10

    def parse_file(self, content):
        return content[4:]

    def find_seat(self, char_seats):
        num_seats = int(char_seats)
        found_seats = []

        for row in range(0, len(self.seats)):
            # checking that there's an adequate number of seats
            print("cur row", row, " left: ", self.seats_left[row])
            if (self.seats_left[row] >= num_seats):
                for seat in range(0, len(self.seats[row])):
                    if (len(found_seats) == num_seats):
                        self.seats_left[row] -= num_seats
                        return found_seats
                    if (self.seats[row][seat] == None):
                        found_seats.append([row, seat])
                    else:
                        found_seats = []
                        continue
        return []

    def buy_seat(self, num_seats):
        booked = self.find_seat(num_seats)
        if (booked == []):
            return []
        row = booked[0][0]
        first = booked[0][1]
        last = booked[-1][-1]

        self.seats[row][first: last+1] = 1
        return [row, first, last]

    def output_file(self, reservation, purchases):
        f = open("output.txt", "a+")
        row = row_dict[purchases[0]]
        cur_seat = purchases[1]
        next_seat = purchases[2]

        f.write("%s " % (reservation[0: 4]))
        while (cur_seat <= next_seat):
            f.write("%s%s," % (row, cur_seat))
            cur_seat += 1

            if (cur_seat == next_seat):
                f.write("%s%s" % (row, cur_seat))
                cur_seat += 1
        f.write("\n")
        f.close()
        return


theater = Theater()
filepath = sys.argv[1]

row_dict = {0: "A", 1: "B", 2: "C", 3: "D",
            4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}

with open(filepath) as fp:
    line = fp.readline()
    while line:
        num_tix = theater.parse_file(line.strip())
        final_seats = theater.buy_seat(num_tix)
        if (final_seats == []):
            print("No seats found for reservation %s!" % line[0:4])
        else:
            theater.output_file(line.strip(), final_seats)
        line = fp.readline()
    fp.close()

path = os.getcwd() + "/output.txt"
print(path)
