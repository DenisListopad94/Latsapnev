import re

s = "I have 5 apples, -3 oranges, and +10 bananas."
matches = re.findall(r'-?\d+', s)
print(matches)