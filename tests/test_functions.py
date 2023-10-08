
# Импорт функций:
from src.functions import translator, filter_and_sorted, get_date, mask_account_num, mask_card_num, final_mask
import os.path

test_json_path = os.path.join('..', 'data', 'operations.json')


def test_translator(data):
    actual_data = translator(test_json_path)
    assert isinstance(actual_data, list)


def test_filter_and_sorted():
    data = [{'date': '2019-01-05', 'state': 'EXECUTED'},
            {'date': '2019-07-13', 'state': 'EXECUTED'},
            {'date': '2018-06-30', 'state': 'CANCELED'}]
    result = filter_and_sorted(data)
    assert len(result) == 2
    assert result[0]['date'] == '2019-07-13'


def test_get_date():
    test_date = {"date": "2019-07-13T18:51:29.313309"}
    assert get_date(test_date) == '13.07.2019'


def test_mask_account_num():
    input_data = '35383033474447895560'
    expected = 'Счет **5560'
    assert mask_account_num(input_data) == expected


def test_mask_card_num():
    card_number_from = '7158300734726758'
    expected = '7158 30** **** 6758'
    assert mask_card_num(card_number_from) == expected


def test_final_mask():
    account = 'Счет **5560'
    card = '715830******6758'
    assert final_mask(account) == mask_account_num(account)
    assert final_mask(card) == mask_card_num(card)
