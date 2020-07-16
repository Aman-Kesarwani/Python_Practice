from abc import ABC, abstractmethod


class GUIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(GUIControl):
    def draw(self):
        print("TextBox: Create Text BOX")


class DropDownList(GUIControl):
    def draw(self):
        print("DDL: Create Drop Down List")


def draw(guicontrol):
    guicontrol.draw()


ddl = DropDownList()
print(isinstance(ddl, GUIControl))
draw(ddl)

txtbox = TextBox()
draw(txtbox)
