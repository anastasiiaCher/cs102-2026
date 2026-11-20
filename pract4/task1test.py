import unittest


def filter_and_transform_strings(strings, substring):
    for string in strings:
        if substring in string:
            yield string.upper()


def test_basic_filtering_and_transformation():
    input_strings = ["hello world", "Python is suspicious", "Hello Python, my old friend"]
    substring = "Python"

    result = list(filter_and_transform_strings(input_strings, substring))

    expected = [
        "PYTHON IS SUSPICIOUS",
        "HELLO PYTHON, MY OLD FRIEND"
    ]
    assert result == expected


def test_no_matches():
    input_strings = ["hello world", "world hello"]
    substring = "Python"

    result = list(filter_and_transform_strings(input_strings, substring))

    assert result == []


def test_empty_input_list():
    input_strings = []
    substring = "Python"

    result = list(filter_and_transform_strings(input_strings, substring))

    assert result == []


def test_case_sensitivity():
    input_strings = ["python is great", "PYTHON is great", "Python is great"]
    substring = "Python"

    result = list(filter_and_transform_strings(input_strings, substring))

    expected = ["PYTHON IS GREAT"]
    assert result == expected


def test_is_generator():
    input_strings = ["Python"]
    gen = filter_and_transform_strings(input_strings, "Python")
    assert hasattr(gen, "__iter__") and hasattr(gen, "__next__")

if __name__ == '__main__':
    unittest.main()