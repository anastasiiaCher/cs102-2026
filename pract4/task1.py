def filter_and_transform_strings(strings, substring):
   for string in strings:
       if substring in string:
            yield string.upper()
input_strings = [
   "hello world",
   "Python is suspicious",
   "I don't know if I love programming",
   "Hello Python, my old friend",
   "Generators are powerful?"
]
substring_to_filter = "Python"

for result in filter_and_transform_strings(input_strings, substring_to_filter):
    print("Результат:" + result)
