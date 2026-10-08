# Набор специальных символов из условия задания
SPECIAL_CHARS = "!@#$%^&*()-_=+."


def has_min_length(password: str, min_length: int = 8) -> bool:
    """1. Проверка минимальной длины пароля."""
    return len(password) >= min_length


def has_uppercase(password: str) -> bool:
    """2. Проверка наличия хотя бы одной заглавной буквы."""
    return any(char.isupper() for char in password)


def has_lowercase(password: str) -> bool:
    """3. Проверка наличия хотя бы одной строчной буквы."""
    return any(char.islower() for char in password)


def has_digit(password: str) -> bool:
    """4. Проверка наличия хотя бы одной цифры."""
    return any(char.isdigit() for char in password)


def has_special(password: str, spec_chars: str = SPECIAL_CHARS) -> bool:
    """5. Проверка наличия хотя бы одного специального символа из заданного набора."""
    return any(char in spec_chars for char in password)


def check_password(password: str) -> bool:
    """Проверяет пароль по всем пяти условиям и выводит детальный отчёт."""
    results = {
        "Длина не менее 8 символов": has_min_length(password),
        "Хотя бы одна заглавная буква": has_uppercase(password),
        "Хотя бы одна строчная буква": has_lowercase(password),
        "Хотя бы одна цифра": has_digit(password),
        "Хотя бы один спецсимвол (!@#$%^&*()-_=+.)": has_special(password),
    }

    print("\n--- Результаты проверки пароля ---")
    all_passed = True
    for rule, passed in results.items():
        status = "[✓] Пройдено" if passed else "[✗] Не пройдено"
        print(f"{status}: {rule}")
        if not passed:
            all_passed = False

    print("-----------------------------------")
    if all_passed:
        print("Итог: Пароль надежный!\n")
    else:
        print("Итог: Пароль слишком слабый, исправьте замечания.\n")

    return all_passed


if __name__ == "__main__":
    print("=== Программа проверки надежности пароля ===")
    user_password = input("Введите пароль для проверки: ")
    check_password(user_password)
