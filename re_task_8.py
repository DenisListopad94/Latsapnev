import re

s = "The quick brown fox jumps over the lazy dog."
matches = re.findall(r'\b\w*b\w*\b', s)
print(matches)