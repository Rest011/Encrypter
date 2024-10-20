# byRest
# Encrypter, версия 0.1
# Это программа было полностью написана Rest(К.К.), вы можете делать с ней всё, что хотите.
# Не забудьте указать авторство!

def ask():
    n = 0
    print('byRest')
    print("Encrypter, версия 0.1")
    print("Это программа было полностью написана Rest(К.К.), вы можете делать с ней всё, что хотите.\nНе забудьте указать авторство!")
    while int(n) != -1:
        n = input("Введите число: ")
        if int(n) != -1:
            mode_sellect(n)

def mode_sellect(n):
    success = False
    while success != True:
        mode = int(input("Что вы хотите сделать с числом(0 - зашифровать / 1 - расшифровать): "))
        if(mode == 1):
            if decrypt(n) == -1:
                print("Ошибка, код 1 - число не может быть расшифровано, так как ранее не было зашифровано ранее.")
            else:
                print("Хорошо, число разшифровано: " + anti_massiver(str(decrypt(n))))
            success = True
        elif(mode == 0):
            print("Хорошо, число зашифровано: " + anti_massiver(str(encrypt(n))))
            success = True
        else:
            print("Это не режим, к сожелению, пожалуйста выберите режим ещё раз.")
            success = False
    return 0

def encrypt(n):
    n = massiver(n)
    for i in range(len(n)):
        if int(n[i]) > 5:
            n[i] = int(n[i]) - 1
        else:
            n[i] = int(n[i]) + 1
    return n

def decrypt(n):
    success = True
    n = massiver(n)
    for i in range(len(n)):
        if int(n[i]) == 9:
            success = False
        else:
                if int(n[i]) > 5 and but_checker(n, i) == False:
                    n[i] = int(n[i]) + 1
                elif(but_checker(n, i) == False):
                    n[i] = int(n[i]) - 1
    if success == True:
        return n
    else:
        return -1

def massiver(n):
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

ask()