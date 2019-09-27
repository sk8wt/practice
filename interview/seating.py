import sys
import numpy as np


class Theater:
    def __init__(self):
        self.seats = np.empty([10, 20], dtype=object)
        self.seats_left = [20] * 10

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
                if (len(found_seats) == num_seats):
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
        row = booked[0][0]
        first = booked[0][1]
        last = booked[-1][-1]

        self.seats[row][first:last+1] = 1
        return [row, first, last]

    def output_file(self, reservation, purchases):
        f = open("output.txt", "a+")
        row = row_dict[purchases[0]]
        cur_seat = purchases[1]
        next_seat = purchases[2]

        f.write("%s" % (reservation))
        while (cur_seat <= next_seat):
            f.write(" %s%s," % (row, cur_seat))
            cur_seat += 1
        f.write("\n")
        f.close()
        return


theater = Theater()
theater.seats[0][1] = "hi"
print(theater.seats)

filepath = sys.argv[1]

row_dict = {0: "A", 1: "B", 2: "C", 3: "D",
            4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}

with open(filepath) as fp:
    line = fp.readline()
    while line:
        num_tix = theater.parse_file(line.strip())
        final_seats = theater.buy_seat(num_tix)
        if (final_seats == []):
            print("No seats found!")
        else:
            theater.output_file(line.strip(), final_seats)
            print(final_seats)
        line = fp.readline()
    fp.close()
theater.seats_left[0] = 4
print(theater.seats_left)
