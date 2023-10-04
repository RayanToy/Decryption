alf = input()
code = input()
d = dict(zip(alf, code))
message = input()
translate = input()
result = ''
new_result = ''
for letter in message:
    replaced_letter = d.get(letter)
    result += replaced_letter
for letter in translate:
    for key, val in d.items():
        if val == letter:
            replaced_letter = key
            new_result += replaced_letter
print(result)
print(new_result)