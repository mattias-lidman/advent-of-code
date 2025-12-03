total = 0

with open('input', 'r') as file:
    for bank in file.readlines():
        first = 1
        first_i = 0
        second = 1
        second_i = 1
        length = len(bank.strip())
        for i in range(length - 1):
            if int(bank[i]) > first:
                first = int(bank[i])
                first_i = i
            if first_i >= second_i:
                second = 1
                second_i = first_i + 1
            if int(bank[i + 1]) > second:
                second = int(bank[i + 1])
                second_i = i + 1
        total += int(f"{first}{second}")

print(total)
