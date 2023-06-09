# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):

    def __str__(self):
        return 'Поле Имя содержит символы, отличные от букв'


class NotEmailError(Exception):

    def __str__(self):
        return 'Email не содержит обязательных символов из набора (@, точка)'


class StringValidator:

    def __init__(self, line_input):
        self.line = line_input
        self.user_data = self.line.split()
        self.print_on = True

    def print_glob(self, text):
        if self.print_on:
            print(text)

    def is_line_correct(self):
        are_not_errors = True
        if len(self.user_data) != 3:
            self.print_glob(f'В строке <{line[:-1]:^35}> не хватает данных')
            are_not_errors = False
            raise ValueError('Данные не соответствуют форме')
        else:
            name, email, age = self.user_data

            if not name.isalpha():
                self.print_glob(f'В строке <{line[:-1]:^35}> некорректно значение <  {name:^15} >')
                are_not_errors = False
                raise NotNameError()

            if '.' not in email or '@' not in email:
                self.print_glob(f'В строке <{line[:-1]:^35}> некорректно значение < {email:^15} >')
                are_not_errors = False
                raise NotEmailError()

            # Считаем, что age всегда число и int(age) не вызовет ошибку типа:
            if not 10 < int(age) < 99:
                self.print_glob(f'В строке <{line[:-1]:^35}> некорректно значение < {age:^15} >')
                are_not_errors = False
                raise ValueError('Указанный возраст не входит в диапазон')


        return are_not_errors


good_log = 'registrations_good.log'
bad_log = 'registrations_bad.log'

with open('registrations.txt', 'r', encoding='utf-8') as log_file:
    for line in log_file:
        check = StringValidator(line_input=line)

        record_is_good = False
        try:
            record_is_good = check.is_line_correct()
        except ValueError as e:
            check.print_glob(text=f'__str__ исключения: {e}\n')
        except NotNameError as e:
            check.print_glob(text=f'__str__ исключения: {e}\n')
        except NotEmailError as e:
            check.print_glob(text=f'__str__ исключения: {e}\n')

        if record_is_good:
            with open(good_log, 'a') as log:
                log.write(line)
        else:
            with open(bad_log, 'a') as log:
                log.write(line)

