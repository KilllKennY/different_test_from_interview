import re

status_dict = {}

with open('input.txt', 'r') as infile:
    for line in infile:
        code_id = re.search(r'\s\d{3}\s', line).group().strip()

        if code_id in status_dict:
            status_dict[code_id] += 1
        else:
            status_dict[code_id] = 1


status_dict_sorted = sorted(status_dict.items(), key=lambda item: item[1], reverse=True)
for key, value in status_dict_sorted:
    print(value, key)
