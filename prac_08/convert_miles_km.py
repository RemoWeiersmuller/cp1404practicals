"""
Estimate: 120 minutes
Actual:   XX minutes
Convert given miles to km in a kivy app.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKm(App):
    """Build a class with the given view from a kv file."""

    result = StringProperty()
    user_value = StringProperty()

    def build(self):
        """Build the GUI."""
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result = "Result"
        self.user_value = '0'
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.result = self.convert_miles_to_km()

    def convert_miles_to_km(self):
        result_in_km = str(float(self.root.ids.user_input.text) * 1.60934)
        return result_in_km

    def handle_increment(self, increment):
        self.user_value = str(float(self.user_value) + increment)
        self.handle_update()

ConvertMilesKm().run()
