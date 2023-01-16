from random import randint


def game():
    print("Вітаю тебе в грі відгадай число \N{grinning face}")
    names = input("І так, як тебе звати?")
    print("Супер ", names, "твоє завдання відгадати число від 1 до 100 за най менше спроб")
    while True:
        print("Що ж поїхали? - 1 \n Не хочу грати - 2 ")
        n = input("Вибирай що ти хочеш")
        if n == "1":
            number = randint(1, 101)
            your_number = int(input("Введіть число ---"))
            y = 1
            while True:
                if number > your_number:
                    print("Більше")
                    y += 1
                    your_number = int(input("Введіть число ---"))
                elif number < your_number:
                    print("Менше")
                    y += 1
                    your_number = int(input("Введіть число ---"))
                elif number == your_number:
                    print("Супер це дійсно \"", your_number, "\" тобі знадобилось", y, "спроб \N{grinning face}")
                    break
        elif n == "2":
            break
        else:
            print("По моєму я чітко написав які є варіанти, повтори введення ")
