from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        """Handle the greeting button click event"""
        print("greet")
        # Obtain the text in the input box and update the label
        input_text = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {input_text}"
    def handle_clear(self):
        """Handle the clear button click event"""
        print("clear")
        # Clear the input boxes and output labels
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""

BoxLayoutDemo().run()
