import re
with open('./user_records.txt') as f:
    data = f.readlines()


user_records_pattern = re.compile('([A-Za-z\s]+), \s?([0-9]+),\s?([A-Z][a-z]+)')
result_list = user_records_pattern.findall(str(data))


print(result_list)
valid_count = 0
invalid_count = 0
for record in data:
    validated = user_records_pattern.match(record)
    if validated:
        name, age, country = validated.groups()
        valid_count += 1
        print(f' Age: {age}, Country: {country}')
    else:
        invalid_count += 1
        print('Invalid record')

print("\n--Record Validity Count--")
print(f'Valid: {valid_count}\nInvalid: {invalid_count}\n\n')
    