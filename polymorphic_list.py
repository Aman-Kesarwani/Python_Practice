class Text(str):
    def duplicate(self):
        return self + self


class CustomList(list):
    def append(self, object):

        if object == "4":
            print("Skipped Append for", object)
        else:
            print("Append Called")
            super().append(object)


text = Text("JAVA")
print(id(text))
duplicate_text = text.duplicate()
text = text.lower()
print(id(text))
print(text)
print(duplicate_text)

my_list = CustomList()
my_list.append("2")
my_list.append("3")
my_list.append("4")

print(my_list)
