"""Лаба 00"""


def text(message: str = "message") -> str:
    """Возвращает переданное текстовое сообщение.

    :param message: Строка текста для вывода.
    :return: Исходная строка текста.
    """
    return message


if __name__ == "__main__":
    print(text())
