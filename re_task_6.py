import re

strings = ["I am a human.", "The human race is evolving."]
replaced_strings = [re.sub(r'human', 'computer', string) for string in strings]
print(replaced_strings)