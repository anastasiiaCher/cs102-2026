input_strings = [
    "hello world",
    "Python is suspicious",
    "I don't know if I love programming",
    "Hello Python, my old friend",
    "Generators are powerful?"
]
substring_to_filter = "Python"

filtered = filter(lambda s: substring_to_filter in s, input_strings)
transformed = map(lambda s: s.lower(), filtered)

for result in transformed:
    print(result)

#либо сделать резалт листом и вывести его так, но скобочки не оч красиво