"""
Estimate: 40 minutes
Actual:   52 minutes
Program with kivy GUI to enter a Name greet and clear the fields.."""


from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Build a class with the given view from a kv file."""
    def build(self):
        """Build the GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet with given input in the label."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_fields(self):
        """Clear the label and input field."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
