import sys


class Theater:
    def __init__(self):
        self.seat = [None] * 20
        self.row = [self.seat] * 10

    def parse_file(self, content):
        print(content[4:])
        return content[4:]

    def buy_seat(self, seats):
        return


theater = Theater()
print(theater.row)

filepath = sys.argv[1]

with open(filepath) as fp:
    line = fp.readline()
    while line:
        num_tix = theater.parse_file(line.strip())
        theater.buy_seat(num_tix)
        line = fp.readline()

#
