# byRest
# Encrypter, версия 0.1
# Это программа было полностью написана Rest(К.К.), вы можете делать с ней всё, что хотите.
# Не забудьте указать авторство!

def main():
    about()
    n = 0
    while int(n) != -1:
        n = input("Введите число: ")
        if int(n) != -1:
            mode_sellect(n)

def about():
    print('byRest')
    print("Encrypter, версия 0.1")
    print("Это программа было полностью написана Rest(К.К.), вы можете делать с ней всё, что хотите.\nНе забудьте указать авторство!")

def mode_sellect(n):
    success = False
    while success != True:
        mode = int(input("Что вы хотите сделать с числом(0 - зашифровать / 1 - расшифровать): "))
        type = typer(mode)
        if mode == 1:
            if type == 1:
                if decrypt_m1(n) == -1:
                    print("Ошибка, код 1 - число не может быть расшифровано, так как ранее не было зашифровано ранее.")
                else:
                    print("Хорошо, число расшифровано: " + anti_massiver(str(decrypt_m1(n))))
            elif type == 2:
                abc = abc_ask()
                print("Хорошо, число расшифровано: " + anti_massiver(str(decrypt_m2(n, abc))))
            elif type == 3:
                abc = abc_ask()
                print("Хорошо, число расшифровано: " + anti_massiver(str(decrypt_m1(anti_massiver(str(decrypt_m2(n, abc)))))))
            elif type == 4:
                abc = abc_ask()
                print("Хорошо, число расшифровано: " + anti_massiver(str(decrypt_m2(anti_massiver(decrypt_m1(n)), abc))))
            success = True
        elif mode == 0:
            if type == 1:
                print("Хорошо, число зашифровано: " + anti_massiver(str(encrypt_m1(n))))
            elif type == 2:
                abc = abc_ask()
                print("Хорошо, число зашифровано: " + anti_massiver(str(encrypt_m2(n, abc))))
            elif type == 3:
                abc = abc_ask()
                print("Хорошо, число зашифровано: " + anti_massiver(str(encrypt_m2(encrypt_m1(n), abc))))
            elif type == 4:
                abc = abc_ask()
                print("Хорошо, число зашифровано: " + anti_massiver(str(encrypt_m1(encrypt_m2(n, abc)))))
            success = True
        else:
            print("Некоректный ввод.")
            success = False
    return 0

def typer(mode):
    if mode == 1:
        print("Выберите режим зашифровки:")
    else:
        print("Выберите режим расшифровки:")          
    print("1 - режим 'плюс/минус'")
    print("2 - алфавитный режим")
    print("3 - прогнать число через все режимы в порядке увелечения")
    print("4 - прогнать число через все режимы в порядке уменьшения")
    success = False
    while success != True:
        answer = int(input("Введите режим: "))
        if  answer >= 1 and answer <= 4:
            success = True
        else:
            print("Некоректный ввод.")
    return answer


def encrypt_m1(n):
    n = massiver(anti_massiver(n))
    for i in range(len(n)):
        if int(n[i]) >= 5:
            n[i] = int(n[i]) - 1
        else:
            n[i] = int(n[i]) + 1
    return n

def decrypt_m1(n):
    success = True
    n = massiver(n)
    for i in range(len(n)):
        if int(n[i]) == 9:
            success = False
        else:
                if int(n[i]) >= 5 and but_checker(n, i) == False:
                    n[i] = int(n[i]) + 1
                elif but_checker(n, i) == False:
                    n[i] = int(n[i]) - 1
    if success == True:
        return n
    else:
        return -1

def encrypt_m2(n, abc):
    standart_abc = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    n = massiver(n)
    for i in range(len(n)):
        for j in range(0, 10):
            if n[i] == standart_abc[j]:
                n[i] = abc[j]
                break
    return n

def decrypt_m2(n, abc):
    standart_abc = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    n = massiver(n)
    for i in range(len(n)):
        for j in range(0, 10):
            if n[i] == abc[j]:
                n[i] = standart_abc[j]
                break
    return n

def massiver(n):
    n = str(n)
    m = []
    for i in range(len(n)):
        m += n[i]
    return m

def anti_massiver(n):
    return ''.join([i for i in map(str, n) if i.isdigit()])

def but_checker(n, i):
    if int(n[i]) == 9:
        return True
    else:
        return False

def abc_ask():
    while True:
        n = input("Пожалуйста, введите алфавит для шифровки/расшифровки:")
        if len(n) != 10:
            print("Недопустимая длина алфавита!")
            continue
        n = massiver(n)
        temp = 0
        for i in range(len(n)):
            temp += int(n[i])
        if temp != 45:
            print("Ошибка, не все символы включенны в алфафите или некоторые символы повторяются!")
            continue
        break
    return n

main()