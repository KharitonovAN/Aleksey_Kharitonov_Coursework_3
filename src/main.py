# Импорт функций:
from functions import translator, filter_and_sorted, get_date, mask_account_num, final_mask

# Основной код:
operations = filter_and_sorted(translator)
for i in operations:
    print(f"{get_date(i['date'])} {i['description']}")
    if "from" in i:
        print(f"""{final_mask(i["from"])} -> {mask_account_num(i["to"])}""")
    else:
        print(f"""Перевод на {mask_account_num(i["to"])} """)
    print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
    print()

# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.