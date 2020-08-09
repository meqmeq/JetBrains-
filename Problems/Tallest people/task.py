def tallest_people(**kwargs):
    tall_dict = {**kwargs}
    max_value = max(tall_dict.values())
    max_keys = [key for key, value in tall_dict.items() if value == max_value]

    for keys in sorted(max_keys):
        print(f'{keys} : {max_value}')

