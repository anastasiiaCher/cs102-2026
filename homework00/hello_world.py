"""Module for hello world function."""


def text() -> str:
    """Return hello world message."""
    message = "Hello, World!"
    return message


if __name__ == "__main__":
    print(text())
