import re

s = "Apple and orange are fruits, but banana is the best."
matches = re.findall(r'\b[aeiouAEIOU]\w*\b', s)
print(matches)