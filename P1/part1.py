'''
Source Problem:
https://adventofcode.com/2023/day/1

Part 1:

idea:
for each line, get first digit on each line and get last digit on each line (reverses line)
O(num_lines * (length_of_line + (length_of_line * length_of_line)))
'''


def get_first_digit(line) -> str:
    for elem in line:
        if elem.isdigit():
            return elem
    return None


def get_last_digit(line) -> str:
    new_line = reversed(line)
    return get_first_digit(new_line)


def main():
    sum = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            calibration_value = int(get_first_digit(line) + get_last_digit(line))
            sum += calibration_value
    print(sum)


if __name__ == '__main__':
    main()