"""
Estimate: 120 minutes
Actual:   130 minutes
Convert given miles to km in a kivy app.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    """Build a class with the given view from a kv file."""

    result = StringProperty()
    user_value = StringProperty()

    def build(self):
        """Build the GUI."""
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result = "Result"
        self.user_value = ''
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        try:
            self.result = self.convert_miles_to_km()
        except ValueError:
            self.user_value = '0.0'

    def convert_miles_to_km(self):
        """Convert miles to km and returns it."""
        result_in_km = str(float(self.root.ids.user_input.text) * FACTOR_MILES_TO_KM)
        return result_in_km

    def handle_increment(self, increment):
        """Handle the increment and set user value up or down."""
        try:
            self.user_value = str(float(self.root.ids.user_input.text) + increment)
            self.handle_update()
        except ValueError:
            self.user_value = str(increment)
            self.handle_update()


ConvertMilesKm().run()
