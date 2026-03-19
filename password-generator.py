import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    """
    Генерирует случайный пароль заданной длины.
    
    Параметры:
    length (int): Длина пароля (минимум 4 символа)
    use_digits (bool): Включать ли цифры
    use_special (bool): Включать ли спецсимволы
    
    Returns:
    str: Сгенерированный пароль
    """
    if length < 4:
        print("Пароль слишком короткий. Устанавливаю длину 4.")
        length = 4
    
    # База символов: всегда буквы (верхний и нижний регистр)
    chars = string.ascii_letters
    
    if use_digits:
        chars += string.digits
    
    if use_special:
        chars += string.punctuation
    
    # Генерация пароля
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("=" * 40)
    print("   ГЕНЕРАТОР СЛОЖНЫХ ПАРОЛЕЙ")
    print("=" * 40)
    
    try:
        length = int(input("Введите длину пароля (рекомендуется 12-16): "))
    except ValueError:
        print("Ошибка! Использую длину 12.")
        length = 12
    
    # Спрашиваем пользователя о настройках
    digits_choice = input("Включать цифры? (y/n): ").lower() == 'y'
    special_choice = input("Включать спецсимволы? (y/n): ").lower() == 'y'
    
    # Генерируем несколько вариантов
    print("\n" + "-" * 40)
    print("Ваши пароли:")
    
    for i in range(3):
        password = generate_password(length, digits_choice, special_choice)
        print(f"{i+1}. {password}")
    
    print("-" * 40)

if __name__ == "__main__":
    main()