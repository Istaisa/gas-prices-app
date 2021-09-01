"""
gas_prices_app.py
authors: Taylor and Naomi
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class GasPricesGrid(GridLayout):
    def __init__(self, **kwargs):
        ### Initialise grid and set number of columns
        super(GasPricesGrid, self).__init__(**kwargs)
        self.cols = 2

        ### Add location input
        self.add_widget(Label(text="Location: "))
        self.location = TextInput(multiline=False)
        self.add_widget(self.location)

        ### Add gas price input
        self.add_widget(Label(text="Gas Price ($/gallon): "))
        self.gas_price = TextInput(input_filter='float')
        self.add_widget(self.gas_price)

        ### Add gas amount input
        self.add_widget(Label(text="Amount of Gas (gallons): "))
        self.gas_amount = TextInput(input_filter='float')
        self.add_widget(self.gas_amount)


class GasPricesApp(App):

    def build(self):
        return GasPricesGrid()

if __name__ == "__main__":
    GasPricesApp().run()