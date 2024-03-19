import re

phone_numbers = ["452658711", "560987122", "574920984", "322876125", "988009122"]
valid_numbers = [number for number in phone_numbers if re.match(r'[89]\d{9}', number)]
print(valid_numbers)