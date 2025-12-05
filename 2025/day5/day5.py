fresh_ranges = []
fresh_count = 0

with open('input', 'r') as file:
    while True:
        line = file.readline().strip()
        if not line:
            break
        fresh_ranges.append([int(x) for x in line.split('-')])

    for line in file.readlines():
        id = line.strip()
        for range in fresh_ranges:
            if range[0] <= int(id) <= range[1]:
                fresh_count += 1
                break

print(fresh_count)
