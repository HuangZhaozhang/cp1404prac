"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Zhaozhang Huang, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Zhaozhang Huang'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty("0.0")
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        miles = self.get_validated_miles()
        km = miles * MILES_TO_KM
        self.output_km = str(km)

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param change: the amount to change
        """
        miles = self.get_validated_miles()+change
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate() # Automatically update the conversion results

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
