# Запуск модулей:
import json
import os


# Импорт JSON архива:
def translator(data):
    """Функция перевода архива JSON"""
    operations_pach = os.path.join('..', 'data', 'operations.json')
    with open(operations_pach, 'r', encoding='utf-8') as file:
        operations_list = json.load(file)
    return operations_list


def filter_and_sorted(data):
    """Функция фильтрации и сортировки по дате"""
    item = [item for item in translator(data) if item.get('state') == 'EXECUTED']
    item.sort(key=lambda x: x.get('date'), reverse=True)
    return item[0:5]


def get_date(date):
    """Функция перевода даты в формат дд/мм/гггг"""
    dt = date[0:10].split(sep='-')
    dt_reverse = '.'.join(reversed(dt))
    return dt_reverse


def mask_account_num(date):
    """Функция маскирующая номер счета"""
    return 'Счет **' + date[-4:]


def mask_card_num(date):
    """Функция маскирующая номер карты"""
    cd_name = ""
    cd_num = ""
    for name in date:
        if not name.isnumeric():
            cd_name += name
        else:
            cd_num += name
    cd_num_mask = cd_num[0:4] + " " + cd_num[4:6] + "** ****" + " " + cd_num[12:]
    return cd_name + cd_num_mask


def final_mask(date):
    """Функция выводит либо номер карты либо номер счета в зависимости от первой буквы"""
    if date[0] == "С":
        return mask_account_num(date)
    else:
        return mask_card_num(date)
    