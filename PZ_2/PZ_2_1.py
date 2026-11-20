
while True:
    user_input = input("Введите целое число больше 999:")

    try:
        n = int(user_input)
    except ValueError:
        print("Ошибка: нужно ввести целое число. Попробуйте снова.")
        continue

    if n <= 999:
        print("Число должно быть больше 999. Попробуйте снова.")
        continue

    result = (n // 1000) % 10
    print("Цифра разряда тысяч:", result)
    break    