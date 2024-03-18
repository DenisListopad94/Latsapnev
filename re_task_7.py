import re

s = "Today's date is 01-01-2024."
date = re.search(r'\b\d{2}-\d{2}-\d{4}\b', s).group()
print(date)