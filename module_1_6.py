my_dict={'Aleksey': 1988, 'Mariana':2016,'Mark':2024}
print(my_dict)
print(my_dict['Mark'])
print(my_dict.get('Den'),': Такого Имени нет!')
my_dict.update({'Alena':1988,
               'Vlad':2014})
Year_birth=my_dict.pop('Vlad')
print(Year_birth)
print(my_dict)
my_set={1,1,23,"Яблоко",23,42.21,"Вишня",2,3,2,16,23,48}
print(my_set)
my_set.add(78)
my_set.add(66)
my_set.discard(21)
print(my_set)