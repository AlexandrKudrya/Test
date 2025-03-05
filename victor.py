import curses
import random
import time
import os
import subprocess

# Большая база вопросов (100+ вопросов из предыдущего ответа)
questions = [
    {"q": "Какой тип данных используется для целых чисел?", "a": "int"},
    {"q": "Какой тип данных используется для чисел с плавающей точкой?", "a": "float"},
    {"q": "Какой тип данных используется для строк?", "a": "str"},
    {"q": "Как обозначается комментарий в Python?", "a": "#"},
    {"q": "Какой оператор используется для присваивания?", "a": "="},
    {"q": "Какой оператор проверяет равенство значений?", "a": "=="},
    {"q": "Какой оператор проверяет неравенство?", "a": "!="},
    {"q": "Какой тип данных используется для логических значений?", "a": "bool"},
    {"q": "Какое значение обозначает истину в Python?", "a": "True"},
    {"q": "Какое значение обозначает ложь в Python?", "a": "False"},
    {"q": "Какой символ используется для обозначения отступа в коде?", "a": "пробел"},
    {"q": "Сколько пробелов обычно используется для отступа?", "a": "4"},
    {"q": "Как называется структура для выбора одного из вариантов?", "a": "if"},
    {"q": "Какой оператор используется для 'иначе' в ветвлении?", "a": "else"},
    {"q": "Какой оператор используется для дополнительных условий?", "a": "elif"},
    {"q": "Какой цикл используется для определенного числа итераций?", "a": "for"},
    {"q": "Какой цикл используется для выполнения до условия?", "a": "while"},
    {"q": "Какой оператор прерывает цикл?", "a": "break"},
    {"q": "Какой оператор пропускает текущую итерацию цикла?", "a": "continue"},
    {"q": "Как обозначается начало блока кода в Python?", "a": ":"},
    {"q": "Какой тип данных является неизменяемым?", "a": "tuple"},
    {"q": "Какой тип данных используется для списков?", "a": "list"},
    {"q": "Какой тип данных используется для словарей?", "a": "dict"},
    {"q": "Какой тип данных используется для множеств?", "a": "set"},
    {"q": "Какой оператор используется для возведения в степень?", "a": "**"},
    {"q": "Какой оператор возвращает остаток от деления?", "a": "%"},
    {"q": "Какой оператор выполняет целочисленное деление?", "a": "//"},
    {"q": "Как называется преобразование строки в число?", "a": "int"},
    {"q": "Как называется преобразование числа в строку?", "a": "str"},
    {"q": "Какой метод используется для ввода данных?", "a": "input"},
    {"q": "Как называется операция сложения строк?", "a": "конкатенация"},
    {"q": "Какой символ используется для новой строки?", "a": "\\n"},
    {"q": "Какой символ используется для табуляции?", "a": "\\t"},
    {"q": "Какой оператор проверяет больше или равно?", "a": ">="},
    {"q": "Какой оператор проверяет меньше или равно?", "a": "<="},
    {"q": "Как обозначается логическое 'и'?", "a": "and"},
    {"q": "Как обозначается логическое 'или'?", "a": "or"},
    {"q": "Как обозначается логическое 'не'?", "a": "not"},
    {"q": "Какой тип данных возвращает input() по умолчанию?", "a": "str"},
    {"q": "Как называется минимальная единица кода в Python?", "a": "оператор"},
    {"q": "Какой символ используется для экранирования?", "a": "\\"},
    {"q": "Какой тип данных не поддерживает индексацию?", "a": "set"},
    {"q": "Какой метод добавляет элемент в конец списка?", "a": "append"},
    {"q": "Какой метод удаляет элемент из списка по индексу?", "a": "pop"},
    {"q": "Как называется пустое значение в Python?", "a": "None"},
    {"q": "Какой оператор используется для умножения?", "a": "*"},
    {"q": "Какой оператор используется для деления?", "a": "/"},
    {"q": "Какой оператор используется для сложения?", "a": "+"},
    {"q": "Какой оператор используется для вычитания?", "a": "-"},
    {"q": "Как проверить тип переменной?", "a": "type"},
    {"q": "Какой символ обозначает начало строки?", "a": "\""},
    {"q": "Какой цикл повторяет блок кода n раз?", "a": "for"},
    {"q": "Какой метод считает длину списка?", "a": "len"},
    {"q": "Какой тип данных изменяемый?", "a": "list"},
    {"q": "Какой тип данных хранит пары ключ-значение?", "a": "dict"},
    {"q": "Какой метод очищает список?", "a": "clear"},
    {"q": "Какой метод возвращает индекс элемента в списке?", "a": "index"},
    {"q": "Как проверить наличие элемента в списке?", "a": "in"},
    {"q": "Какой оператор объединяет условия?", "a": "and"},
    {"q": "Какой цикл бесконечный без break?", "a": "while"},
    {"q": "Какой метод сортирует список?", "a": "sort"},
    {"q": "Какой метод переворачивает список?", "a": "reverse"},
    {"q": "Какой символ обозначает конец строки кода?", "a": "не нужен"},
    {"q": "Какой тип данных хранит только уникальные элементы?", "a": "set"},
    {"q": "Какой метод добавляет элемент в множество?", "a": "add"},
    {"q": "Какой метод удаляет элемент из множества?", "a": "remove"},
    {"q": "Какой тип данных используется для кортежей?", "a": "tuple"},
    {"q": "Какой символ используется для кортежа?", "a": "()"},
    {"q": "Какой символ используется для списка?", "a": "[]"},
    {"q": "Какой символ используется для словаря?", "a": "{}"},
    {"q": "Какой метод возвращает ключи словаря?", "a": "keys"},
    {"q": "Какой метод возвращает значения словаря?", "a": "values"},
    {"q": "Какой метод возвращает пары ключ-значение словаря?", "a": "items"},
    {"q": "Какой цикл удобен для перебора списка?", "a": "for"},
    {"q": "Какой оператор увеличивает переменную на 1?", "a": "+="},
    {"q": "Какой тип данных не поддерживает повторяющиеся элементы?", "a": "set"},
    {"q": "Какой метод копирует список?", "a": "copy"},
    {"q": "Какой оператор используется для проверки условия?", "a": "if"},
    {"q": "Какой символ используется для разделения элементов в списке?", "a": ","},
    {"q": "Как называется ошибка при неверном отступе?", "a": "IndentationError"},
    {"q": "Какой тип ошибки возникает при делении на ноль?", "a": "ZeroDivisionError"},
    {"q": "Как называется преобразование типов данных?", "a": "кастинг"},
    {"q": "Какой метод считает количество элементов в списке?", "a": "count"},
    {"q": "Какой оператор используется для проверки условия 'меньше'?", "a": "<"},
    {"q": "Какой оператор используется для проверки условия 'больше'?", "a": ">"},
    {"q": "Какой метод вставляет элемент в список по индексу?", "a": "insert"},
    {"q": "Какой цикл может быть прерван условием?", "a": "while"},
    {"q": "Какой тип данных обозначает отсутствие значения?", "a": "NoneType"},
    {"q": "Какой метод удаляет последний элемент списка?", "a": "pop"},
    {"q": "Какой символ используется для многострочного комментария?", "a": "нет такого"},
    {"q": "Как называется переменная, которая не меняется?", "a": "константа"},
    {"q": "Какой тип данных хранит упорядоченную последовательность?", "a": "list"},
    {"q": "Какой метод возвращает максимальное значение в списке?", "a": "max"},
    {"q": "Какой метод возвращает минимальное значение в списке?", "a": "min"},
    {"q": "Какой оператор используется для повторения строки?", "a": "*"},
    {"q": "Какой метод объединяет элементы списка в строку?", "a": "join"},
    {"q": "Какой тип данных хранит неупорядоченные уникальные элементы?", "a": "set"},
    {"q": "Какой метод проверяет наличие ключа в словаре?", "a": "in"},
    {"q": "Как называется процесс выполнения кода построчно?", "a": "интерпретация"},
    {"q": "Какой символ обозначает начало и конец строки?", "a": "'"}
]

def draw_border(stdscr, y, x, height, width):
    """Рисуем рамку вокруг области"""
    stdscr.attron(curses.color_pair(1))
    stdscr.border(0)
    stdscr.attroff(curses.color_pair(1))

def animate_text(stdscr, y, x, text, delay=0.05):
    """Анимация появления текста"""
    for i, char in enumerate(text):
        stdscr.addstr(y, x + i, char)
        stdscr.refresh()
        time.sleep(delay)

def fireworks(stdscr):
    """Фейерверк при правильном ответе"""
    stdscr.clear()
    colors = [curses.COLOR_YELLOW, curses.COLOR_MAGENTA, curses.COLOR_CYAN, curses.COLOR_WHITE]
    for _ in range(10):  # 10 взрывов
        y, x = random.randint(2, curses.LINES - 3), random.randint(2, curses.COLS - 3)
        color = random.choice(colors)
        curses.init_pair(4, color, curses.COLOR_BLACK)
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(y, x, "*")
        stdscr.refresh()
        time.sleep(0.1)
        # Расширение взрыва
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if 0 < y + dy < curses.LINES - 1 and 0 < x + dx < curses.COLS - 1:
                stdscr.addstr(y + dy, x + dx, "+")
        stdscr.refresh()
        time.sleep(0.2)
    stdscr.attroff(curses.color_pair(4))
    stdscr.clear()

def red_fill(stdscr):
    """Заливка экрана красным при ошибке"""
    stdscr.attron(curses.color_pair(3))
    for y in range(curses.LINES - 1):
        for x in range(curses.COLS - 1):
            stdscr.addstr(y, x, "▇")
        stdscr.refresh()
        time.sleep(0.02)
    stdscr.attroff(curses.color_pair(3))
    time.sleep(0.5)
    stdscr.clear()

def quiz(stdscr):
    # Инициализация цветов
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Рамка
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Правильный ответ
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # Неправильный ответ

    correct_answers = 0
    asked_questions = set()
    stdscr.clear()

    # Приветственное сообщение
    stdscr.attron(curses.A_BOLD)
    animate_text(stdscr, 2, 2, "Добро пожаловать в Python-викторину!")
    stdscr.attroff(curses.A_BOLD)
    animate_text(stdscr, 4, 2, "Ответьте правильно на 3 вопроса!")
    stdscr.addstr(6, 2, "Нажмите любую клавишу для старта...")
    stdscr.refresh()
    stdscr.getch()

    while correct_answers < 3:
        stdscr.clear()
        draw_border(stdscr, 0, 0, curses.LINES - 1, curses.COLS - 1)

        # Выбираем случайный вопрос
        available_questions = [q for i, q in enumerate(questions) if i not in asked_questions]
        if not available_questions:
            break
        q_data = random.choice(available_questions)
        question = q_data["q"]
        correct_answer = q_data["a"]
        asked_questions.add(questions.index(q_data))

        # Выводим прогресс
        stdscr.addstr(1, 2, f"Верных ответов: {correct_answers}/3", curses.color_pair(2))

        # Выводим вопрос с анимацией
        animate_text(stdscr, 3, 2, f"Вопрос: {question}")
        stdscr.addstr(5, 2, "Ваш ответ: ")

        # Получаем ответ пользователя
        curses.echo()
        answer = stdscr.getstr(5, 12).decode().strip().lower()
        curses.noecho()

        # Проверяем ответ
        if answer == correct_answer:
            correct_answers += 1
            stdscr.attron(curses.color_pair(2))
            animate_text(stdscr, 7, 2, "Правильно!")
            stdscr.attroff(curses.color_pair(2))
            fireworks(stdscr)  # Запускаем фейерверк
        else:
            red_fill(stdscr)  # Заливаем экран красным
            stdscr.attron(curses.color_pair(3))
            animate_text(stdscr, 7, 2, f"Неправильно! Правильный ответ: {correct_answer}")
            stdscr.attroff(curses.color_pair(3))

        stdscr.addstr(9, 2, "Нажмите любую клавишу для продолжения...")
        stdscr.refresh()
        stdscr.getch()

    # Завершение викторины
    stdscr.clear()
    draw_border(stdscr, 0, 0, curses.LINES - 1, curses.COLS - 1)
    stdscr.attron(curses.A_BOLD | curses.color_pair(2))
    animate_text(stdscr, 2, 2, "Поздравляем! Викторина завершена!")
    stdscr.attroff(curses.A_BOLD | curses.color_pair(2))
    animate_text(stdscr, 4, 2, "Теперь решите задачи в файлах taskX.py")
    stdscr.addstr(6, 2, "Нажмите любую клавишу для выхода...")
    stdscr.refresh()
    stdscr.getch()

# Создание файлов с задачами (без изменений)
def create_tasks():
    tasks = [
        '''# Задача 1: Четное или нечетное
# Напишите программу, которая принимает число n и выводит "Even", если оно четное, и "Odd", если нечетное.
n = int(input())
''',
        '''# Задача 2: Сумма чисел
# Напишите программу, которая принимает число n и выводит сумму всех чисел от 1 до n.
n = int(input())
''',
        '''# Задача 3: Уникальные слова
# Напишите программу, которая принимает строку текста и выводит количество уникальных слов в ней.
# Слова разделены пробелами, знаки препинания отсутствуют.
text = input()
'''
    ]
    for i, task in enumerate(tasks, 1):
        with open(f"task{i}.py", "w", encoding="utf-8") as f:
            f.write(task)

# Создание тестов (без изменений)
def create_tests():
    tests = [
        '''import subprocess
input_data = "4\\n"
process = subprocess.run(["python", "task1.py"], input=input_data, text=True, capture_output=True)
assert process.stdout.strip() == "Even", f"Ожидалось 'Even', получено '{process.stdout.strip()}'"
print("Тест для задачи 1 пройден!")
''',
        '''import subprocess
input_data = "5\\n"
process = subprocess.run(["python", "task2.py"], input=input_data, text=True, capture_output=True)
assert process.stdout.strip() == "15", f"Ожидалось '15', получено '{process.stdout.strip()}'"
print("Тест для задачи 2 пройден!")
''',
        '''import subprocess
input_data = "hello world hello python\\n"
process = subprocess.run(["python", "task3.py"], input=input_data, text=True, capture_output=True)
assert process.stdout.strip() == "4", f"Ожидалось '4', получено '{process.stdout.strip()}'"
print("Тест для задачи 3 пройден!")
'''
    ]
    for i, test in enumerate(tests, 1):
        with open(f"test_task{i}.py", "w", encoding="utf-8") as f:
            f.write(test)

def main():
    curses.wrapper(quiz)
    create_tasks()
    print("Файлы задач созданы: task1.py, task2.py, task3.py")
    create_tests()
    print("Файлы тестов созданы: test_task1.py, test_task2.py, test_task3.py")
    print("Решите задачи, затем запустите тесты командой: python test_taskX.py")

if __name__ == "__main__":
    main()
