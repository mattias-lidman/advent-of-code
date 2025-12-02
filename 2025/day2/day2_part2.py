invalid_sum = 0

with open('input', 'r') as file:
    line = file.readlines()[0].strip()  # All input on a single line

ranges = line.split(',')


def is_invalid(id):
    id = str(id)
    # For each prime number up to len(id):
    if len(id) > 31:
        print("Need more primes!")
        exit(1)
    for prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if prime > len(id):
            return False
        l = len(id)
        # Check if id length is divisible by prime
        if l % prime != 0:
            continue
        # Check if id is equal to `prime` repetitions of the first `prime` digits
        segment = id[0:l // prime]
        if segment * prime == id:
            return True
    return False


for r in ranges:
    start, end = map(int, r.split('-'))
    for id in range(start, end + 1):
        if is_invalid(id):
            invalid_sum += id

print(invalid_sum)
