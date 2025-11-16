"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Zhaozhang Huang, IT@JCU
Started 16/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Zhaozhang Huang'

class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root
def handle_calculate(self, value):
    """ handle calculation (could be button press or other call), output result to label widget """
    try:
        number = float(value)
        result = number ** 2
        self.root.ids.output_label.text = str(result)
    except ValueError:
        self.root.ids.output_label.text = "Invalid input"
if __name__ == '__main__':
    SquareNumberApp().run()
