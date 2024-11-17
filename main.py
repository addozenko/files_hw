from pprint import pprint

#Задача №1
with open('recipes.txt', encoding='utf-8') as f:
    output = f.readlines()

cook_book = {}
for _ in list(output):
    row = _.split()
    if '|' not in row and len(row) > 0 and not row[0].isdigit():
        dish = ' '.join(row)
        cook_book[dish] = []
    elif'|' in row:
        keys = ['ingredient_name', 'quantity', 'measure']
        values = ''.join(row).split('|')
        dish_dict = dict(zip(keys, values))
        cook_book[dish].append(dish_dict)

pprint(cook_book)

#Задача №2
def get_shop_list_by_dishes(dishes_list, number_of_persons):
    result = {}
    for dish in dishes_list:
        for ingredients in cook_book[dish]:
            ingredient_name = ingredients.pop('ingredient_name')
            new_quantity = lambda quantity: quantity * number_of_persons
            ingredients['quantity'] = new_quantity(int(ingredients['quantity']))
            result[ingredient_name] = ingredients
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

#Задача №3
files_names_list = ['1.txt', '2.txt', '3.txt']
files_dict = {}
for file_name in files_names_list:
    with open(file_name, encoding='utf-8') as f:
        output = f.readlines()
        files_dict[file_name] = output

sorted_files_dict = sorted(files_dict.items(), key= lambda item: item[1], reverse=True)
with open('123.txt', 'w') as f:
    for file_data in sorted_files_dict:
        f.write(f'{file_data[0]}\n')
        f.write(f'{len(file_data[1])}\n')
        f.write(f'{"".join(file_data[1])}\n')
