total = 0

with open('input', 'r') as file:
    for bank in file.readlines():
        n = 0  # The digit we're looking for
        n_digits = 12
        digits = [1]
        length = len(bank.strip())
        i = 0
        current_digit_i = 0
        while n < n_digits:
            if int(bank[i]) > digits[n]:
                digits[n] = int(bank[i])
                current_digit_i = i
            i += 1
            if i + n_digits - n > length:
                # No more space to look for digit n -- reset to start looking for n + 1
                if n + 1 == n_digits:
                    break
                n += 1
                digits.append(1)
                i = current_digit_i + 1

        total += int(''.join(str(d) for d in digits))

print(total)
