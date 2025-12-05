fresh_ranges = []

with open('input', 'r') as file:
    while True:
        line = file.readline().strip()
        if not line:
            break
        fresh_ranges.append([int(x) for x in line.split('-')])
    
    fresh_ranges.sort(key=lambda x: x[0])
    n_ranges = len(fresh_ranges)
    i = 0
    while i < n_ranges - 1:
        while n_ranges > i + 1 and fresh_ranges[i][1] >= fresh_ranges[i + 1][0]:
            fresh_ranges[i][1] = max(fresh_ranges[i][1], fresh_ranges[i + 1][1])
            fresh_ranges.pop(i + 1)
            n_ranges -= 1
        i += 1

print(sum([r[1] - r[0] + 1 for r in fresh_ranges]))
