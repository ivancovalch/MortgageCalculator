from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class MortgageCalculator(MDApp):
    def build(self):
        return MDLabel (text ="Hello calculator", halign = "center")

MortgageCalculator().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
