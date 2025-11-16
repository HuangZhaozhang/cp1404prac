"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Zhaozhang Huang, first version: 11/16/2025
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.names:
            # create a label for each name
            temp_label = Label(text=name)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)



DynamicWidgetsApp().run()
