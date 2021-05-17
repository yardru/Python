def caeser_eng(text, x):
    n = 26
    return ''.join([chr((ord(c) - ord('a') + x) % n + ord('a')) if c.islower() else
                    chr((ord(c) - ord('A') + x) % n + ord('A')) if c.isupper() else c for c in text])

def caeser_rus(text, x):
    n = 32
    return ''.join([chr((ord(c) - ord('а') + x) % n + ord('а')) if c.islower() else
                    chr((ord(c) - ord('А') + x) % n + ord('А')) if c.isupper() else c for c in text])

def bruteforce(text):
    for i in range(1, 26):
        print(caeser_eng(text, i))

bruteforce("Hawnj pk swhg xabkna ukq nqj.")

lang = input("Введите язык[rus/eng]: ").lower()
if lang == 'eng':
    print(caeser_eng(input("Введите текст: "), int(input("Введите сдвиг: "))))
elif lang == 'rus':
    print(caeser_rus(input("Введите текст: "), int(input("Введите сдвиг: "))))



     