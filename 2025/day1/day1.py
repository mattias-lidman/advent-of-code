dial = 50
zeroes = 0

with open('input', 'r') as file:
    for line in file:
        if line[0] == 'L':
            dial = (dial - int(line[1:])) % 100
        elif line[0] == 'R':
            dial = (dial + int(line[1:])) % 100
        if dial == 0:
            zeroes += 1

print(zeroes)
