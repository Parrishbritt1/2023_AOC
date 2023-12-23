'''
Source Problem:
https://adventofcode.com/2023/day/1

Part 2:
This solution is so hacky, I hate it.
'''

digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
          'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def get_first_digit(line) -> str:
    for i, elem in enumerate(line):
        if elem.isdigit():
            return (i, elem)
    return (None, None)


def get_last_digit(line):
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            return (i, line[i])
    return (None, None)


def get_first_digit_str(line):
    length_of_line = len(line)-1
    for i, elem in enumerate(line):
        # Window of 3
        if i+2 <= length_of_line:
            possible_digit_str = line[i] + line[i+1] + line[i+2]
            digit = digits.get(possible_digit_str)
            if digit != None:
                return (i, digit)
        else:
            break

        # Window of 4
        if i+3 <= length_of_line:
            possible_digit_str = line[i] + line[i+1] + line[i+2] + line[i+3]
            digit = digits.get(possible_digit_str)
            if digit != None:
                return (i, digit)
            
        # Window of 5
        if i+4 <= length_of_line:
            possible_digit_str = line[i] + line[i+1] + line[i+2] + line[i+3] + line[i+4]
            digit = digits.get(possible_digit_str)
            if digit != None:
                return (i, digit)
    return (None, None)


def get_last_digit_str(line):
    length_of_line = len(line)
    i = length_of_line-1
    while i-2 >= 0:
        if i-2 >= 0:
            possible_digit_str = line[i-2] + line[i-1] +line[i]
            digit = digits.get(possible_digit_str)
            if digit != None:
                return (i-2, digit)

        if i-3 >= 0:
            possible_digit_str = line[i-3] + line[i-2] + line[i-1] + line[i]
            digit = digits.get(possible_digit_str)
            if digit != None:
                return (i-3, digit)
            
        if i-4 >= 0:
            possible_digit_str = line[i-4] + line[i-3] + line[i-2] + line[i-1] + line[i]
            digit = digits.get(possible_digit_str)
            if digit != None:
                return (i-4, digit)
        i -= 1
    return (None, None)


def main():
    sum = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            s1, first_digit = get_first_digit(line)
            s2, first_digit_str = get_first_digit_str(line)
            if s1 is not None and s2 is not None:
                if s1 < s2:
                    first = first_digit
                else:
                    first = first_digit_str
            elif s1 is not None:
                first = first_digit
            elif s2 is not None:
                first = first_digit_str
            
            l1, last_digit = get_last_digit(line)
            l2, last_digit_str = get_last_digit_str(line)
            if l1 is not None and l2 is not None:
                if l1 > l2:
                    last = last_digit
                else:
                    last = last_digit_str
            elif l1 is not None:
                last = last_digit
            elif l2 is not None:
                last = last_digit_str

            calibration_value = int(first + last)
            sum += calibration_value

    print(sum)


if __name__ == '__main__':
    main()