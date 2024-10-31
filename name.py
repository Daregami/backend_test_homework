"""Аннотируем параметр функции: "значение name должно быть типа str"""


def we_crash_all(name: str) -> str:
    """Выводит фразу с использованием имени"""
    return 'Привет, ' + name + ', мы всё сломали!'


print(we_crash_all('Практикум'))

print('Анотации функции:', we_crash_all.__annotations__)
