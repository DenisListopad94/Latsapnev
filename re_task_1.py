import re

s = "The cat catches a caterpillar. My lovely cat."
matches = re.findall(r'\b\w*cat\w*\b', s)
print(matches)