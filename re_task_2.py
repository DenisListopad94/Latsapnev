import re

strings = ["hzzzk", "hello zz world", "pizza", "z433z342z", "z123z"]
matches = [string for string in strings if re.search(r'z.{3}z', string)]
print(matches)