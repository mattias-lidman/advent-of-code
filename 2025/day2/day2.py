invalid_sum = 0

with open('input', 'r') as file:
    line = file.readlines()[0].strip()  # All input on a single line

ranges = line.split(',')


def is_valid(id):
    id = str(id)
    if len(id) / 2 != len(id) // 2:
        return True
    # Check if second half is identical to first half
    half = len(id) // 2
    if id[:half] == id[half:]:
        return False
    return True


for r in ranges:
    start, end = map(int, r.split('-'))
    for id in range(start, end + 1):
        if not is_valid(id):
            invalid_sum += id

print(invalid_sum)
