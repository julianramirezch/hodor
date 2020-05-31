#!/usr/bin/python3
""" Program level 1"""

import requests


def cheat_votes():
    usr_id = 0
    usr_votes = 0
    votes = 0
    value = 0
    set_cookie = ''
    data_list = []
    data_list = usr_input(usr_id, usr_votes, set_cookie, value)
    dict_entry = ['id', data_list[0], 'holdthedoor', 'Submit', 'key', data_list[3]]
    cookies_list = [data_list[2], data_list[3]]

    data_input = list_dict(dict_entry)
    cookies = list_dict(cookies_list)
    total_votes = int(data_list[1])

    try:
        for i in range(total_votes):
            r = requests.post("http://158.69.76.135/level1.php", data=data_input, cookies=cookies)
            print('Vote O.K: {}'.format(i + 1))
            votes += 1
    except Exception as error:
        print(error)

    return(votes)


def check_is_number(number, message):
    while not number.isnumeric():
        number = input(message)
    return number


def usr_input(usr_id, usr_votes, set_cookie, value):
    valid_number = 'Please valid id: '
    usr_id = 0
    usr_votes = 0
    print('HODOR CHEAT VOTES')

    usr_id = check_is_number(input('id: '), valid_number)
    usr_votes = check_is_number(input('votes: '), valid_number)
    set_cookie = input('Set-Cookie: ')
    set_key_value = check_is_number(input('Key value: '), valid_number)
    return usr_id, usr_votes, set_cookie, set_key_value


def list_dict(lst):
    it = iter(lst)
    res_dct = dict(zip(it, it))
    return res_dct


if __name__ == "__main__":
    votes = cheat_votes()
    print('Total success votes: {}'.format(votes))
