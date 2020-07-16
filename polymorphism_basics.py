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


def draw(guicontrols):
    for control in guicontrols:
        control.draw()


ddl = DropDownList()

txtbox = TextBox()

draw([ddl, txtbox])
