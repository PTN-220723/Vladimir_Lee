# 1) В задании создан словарь, с информацией о разных устройствах.
# Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести информацию
# о соответствующем устройстве
# devices = {
#    'r1': {
#        'location': 'Bukhara',
#        'vendor': 'Cisco',
#        'model': '4451',
#        'ios': '15.4',
#        'ip': '10.255.0.1'
#    },
#    'r2': {
#        'location': 'Samarkand',
#        'vendor': 'Cisco',
#        'model': '4451',
#        'ios': '15.4',
#        'ip': '10.255.0.2'
#    },
#    'sw1': {
#        'location': 'Tashkent',
#        'vendor': 'Cisco',
#        'model': '3850',
#        'ios': '3.6.XE',
#        'ip': '10.255.0.101',
#        'vlans': '10,20,30',
#        'routing': True
#    }
#}

devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

device = input('Введите название устройства [г1/г2/swi]: ')
print(devices[device])

#2) Есть словарь кодов товаров и словарь количества товара на складе, задача сопоставить два словаря
# и высчитать общее количество.
# goods = {
# 'Лампа': '12345',
# 'Стол': '23456',
# 'Диван': '34567',
# 'Стул': '45678',
#}
#store = {
# '12345': [
#  {
#   'quantity': 27,
#   'price': 42
#  },
# ],
# '23456': [
#  {
#   'quantity': 22,
#   'price': 510
#  },
#  {
#   'quantity': 32,
#   'price': 520
#  },
#],
# '34567': [
#  {
#   'quantity': 2,
#   'price': 1200
#  },
#  {
#   'quantity': 1,
#    'price': 1150
#  },
# ],
# '45678': [
#  {
#   'quantity': 50,
#   'price': 100
#  },
#  {
#   'quantity': 12,
#   'price': 95
#  },
#  {
#   'quantity': 43,
#   'price': 97
#  },
# ],
#}


