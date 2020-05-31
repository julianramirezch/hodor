#!/usr/bin/python3
""" Pgogram level 0"""

import requests


def cheat_votes():
    usr_id = 0
    usr_votes = 0
    votes = 0
    usr_inputs_list = []
    usr_inputs_list = usr_input(usr_id, usr_votes)
    dict_entry = ['id', usr_inputs_list[0], 'holdthedoor', 'Submit']

    data_input = list_dict(dict_entry)
    total_votes = int(usr_inputs_list[1])

    try:
        for i in range(total_votes):
            r = requests.post("http://158.69.76.135/level0.php", data=data_input)
            print('Vote O.K: {}'.format(i + 1))
            votes += 1
    except Exception as error:
        print(error)

    return(votes)


def check_is_number(number, message):
    while not number.isnumeric():
        number = input(message)
    return number


def usr_input(usr_id, usr_votes):
    valid_number = 'Please valid id: '
    valid_votes = 'Please valid number: '
    usr_id = 0
    usr_votes = 0
    print('HODOR CHEAT VOTES')

    usr_id = check_is_number(input('id: '), valid_number)
    usr_votes = check_is_number(input('votes: '), valid_votes)
    return usr_id, usr_votes


def list_dict(lst):
    it = iter(lst)
    res_dct = dict(zip(it, it))
    return res_dct


if __name__ == "__main__":
    votes = cheat_votes()
    print('Total success votes: {}'.format(votes))
