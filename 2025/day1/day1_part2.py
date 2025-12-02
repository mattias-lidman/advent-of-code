
dial = 50
zeroes = 0

with open('input', 'r') as file:
    for line in file:
        if line[0] == 'L':
            passes = (dial - int(line[1:])) // 100
            if dial == 0:
                passes += 1  # Cancel out the zero crossing if starting at zero
            dial = (dial - int(line[1:])) % 100
            zeroes += abs(passes)
            if dial == 0:
                zeroes += 1
            print(f"Line: {line}, Dial: {dial}, Passes: {passes}, Zeroes: {zeroes}")
        elif line[0] == 'R':
            passes = (dial + int(line[1:])) // 100
            dial = (dial + int(line[1:])) % 100
            zeroes += abs(passes)
            print(f"Line: {line}, Dial: {dial}, Passes: {passes}, Zeroes: {zeroes}")

print(zeroes)
