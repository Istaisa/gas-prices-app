"""
gas_prices_app.py
authors: Taylor and Naomi
"""

from kivy.app import App
from kivy.uix.label import Label

class GasPricesApp(App):

    def build(self):
        return Label(text="Taylor and Naomi are coding!")

if __name__ == "__main__":
    GasPricesApp().run()