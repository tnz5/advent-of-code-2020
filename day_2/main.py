# Day 2: Password Philosophy


RANGE_POS = 0
LETTER_POS = 1
PWORD_POS = 2
MIN_INDEX = 0
MAX_INDEX = 1


def parse_input(pw_list):
    pw_dicts = []
    for pw in pw_list:
        pw_dict = {}
        r = pw[RANGE_POS].split('-')
        pw_dict['min'] = int(r[MIN_INDEX])
        pw_dict['max'] = int(r[MAX_INDEX])
        pw_dict['letter'] = pw[1][0]
        pw_dict['password'] = pw[PWORD_POS]
        pw_dicts.append(pw_dict)
    return pw_dicts


def read_input():
    with open('input.txt', 'r') as f:
        input = f.readlines()
        pw = [x.strip() for x in input]
        pw_list = [y.split() for y in pw]
        return pw_list


def is_valid_password(pw_dict):
    num_letter = 0
    for ch in pw_dict['password']:
        if ch == pw_dict['letter']:
            num_letter += 1
    if num_letter >= pw_dict['min'] and num_letter <= pw_dict['max']:
        return True
    return False


def is_valid_password_part_2(pw_dict):
    in_1 = pw_dict['min'] - 1
    in_2 = pw_dict['max']- 1
    letter = pw_dict['letter']
    pw = pw_dict['password']
    if (pw[in_1] == letter and list[in_2] != letter) or (pw[in_1] != letter and pw[in_2] == letter):
        return True
    return False

def main():

    input_pw = read_input()
    parsed = parse_input(input_pw)

    num_valid_pw = 0
    num_valid_pw_part_2 = 0
    for k in parsed:
        if is_valid_password(k):
            num_valid_pw += 1
        if is_valid_password_part_2(k):
            num_valid_pw_part_2 += 1
    print(num_valid_pw)
    print(num_valid_pw_part_2)


if __name__ == '__main__':
    main()
