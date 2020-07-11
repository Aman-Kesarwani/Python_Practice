from pprint import pprint
sentence = "This is a most common problem solving question"

set_character = {character for character in sentence}
print(set_character)
print(type(set_character))

count_dict = dict()
for key in sentence:
    if key not in count_dict:
        count_dict[key] = 1
    else:
        count_dict[key] += 1

pprint(count_dict, width=1)

sorted_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

print("The largest repetition is of: ", sorted_list[0])
