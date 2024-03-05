def extract_digits_from_tuples(tuples_list):
    digits_list = []

    for tup in tuples_list:
        for element in tup:
            if isinstance(element, int) or str(element).isdigit():
                if isinstance(element, int):
                    digits_list.extend([int(digit) for digit in str(element)])
                else:
                    digits_list.extend([int(digit) for digit in str(element) if digit.isdigit()])

    return digits_list

tuples_list = [(1, 'abc', 23), ('x', 45, 'yz'), ('pqr', 67.89, 'stu')]
digits = extract_digits_from_tuples(tuples_list)
print("Digits extracted from tuples:", digits)