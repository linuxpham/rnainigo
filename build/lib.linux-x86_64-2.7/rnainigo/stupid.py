import sys

data = {}

line = sys.stdin.readline()
while line:
        if line[0] == "@":
                line = sys.stdin.readline()

        #DO STUFF
        record = line.split()
        data.setdefault(record[2], 0)
        data[record[2]] += 1

        #END STUFF
        line = sys.stdin.readline()

#PRINT OUTPUT

for key, value in data.items():
        print key, value

