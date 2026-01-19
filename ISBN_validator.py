def validate_isbn(isbn, length):
    # Requirement 8 & 14: Check for non-numeric characters (except 'X' in ISBN-10)
    # The first (length-1) characters must always be digits
    main_part = isbn[:length - 1]
    last_char = isbn[-1:] if len(isbn) > 0 else ""

    if not main_part.isdigit():
        print('Invalid character was found.')
        return

    # Check the last character (can be X for ISBN-10)
    if length == 10:
        if not (last_char.isdigit() or last_char.upper() == 'X'):
            print('Invalid character was found.')
            return
    else:
        if not last_char.isdigit():
            print('Invalid character was found.')
            return

    # Requirement 12 & 13: Check length matches
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Slicing logic:
    # For ISBN-10, main_digits are the first 9. For ISBN-13, the first 12.
    main_digits = isbn[0:length - 1]
    given_check_digit = isbn[length - 1].upper()
    main_digits_list = [int(digit) for digit in main_digits]

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - (digits_sum % 11)
    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    result = 10 - (digits_sum % 10)
    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    # Requirement 6 & 17: Check for comma
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')
    isbn = values[0].strip()

    # Requirement 7 & 16: Check if length is a number
    try:
        length = int(values[1].strip())
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

main()