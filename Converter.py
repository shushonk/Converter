from tkinter import *
from tkinter import ttk

# Currency Conversion function
def currency_conversion():
    exchange_rates = {
        "USD": {"USD": 1, "EUR": 0.93, "INR": 82.74, "QAR": 3.64, "ZWD": 363.0, "AED": 3.67, "GBP": 0.75, "JPY": 133.5, "CNY": 7.07},
        "EUR": {"USD": 1.08, "EUR": 1, "INR": 89.0, "QAR": 3.92, "ZWD": 390.0, "AED": 3.95, "GBP": 0.81, "JPY": 143.0, "CNY": 7.57},
        "INR": {"USD": 0.012, "EUR": 0.011, "INR": 1, "QAR": 0.045, "ZWD": 4.5, "AED": 0.045, "GBP": 0.0091, "JPY": 1.5, "CNY": 0.085},
        "QAR": {"USD": 0.27, "EUR": 0.24, "INR": 22.0, "QAR": 1, "ZWD": 100.0, "AED": 1.08, "GBP": 0.21, "JPY": 39.0, "CNY": 1.88},
        "ZWD": {"USD": 0.0028, "EUR": 0.0026, "INR": 0.22, "QAR": 0.01, "ZWD": 1, "AED": 0.01, "GBP": 0.0018, "JPY": 0.39, "CNY": 0.02},
        "AED": {"USD": 0.27, "EUR": 0.25, "INR": 22.0, "QAR": 0.93, "ZWD": 100.0, "AED": 1, "GBP": 0.20, "JPY": 36.0, "CNY": 1.74},
        "GBP": {"USD": 1.34, "EUR": 1.23, "INR": 110.0, "QAR": 4.76, "ZWD": 555.0, "AED": 5.04, "GBP": 1, "JPY": 175.0, "CNY": 8.59},
        "JPY": {"USD": 0.0075, "EUR": 0.007, "INR": 0.67, "QAR": 0.026, "ZWD": 2.6, "AED": 0.028, "GBP": 0.0057, "JPY": 1, "CNY": 0.049},
        "CNY": {"USD": 0.14, "EUR": 0.13, "INR": 11.8, "QAR": 0.53, "ZWD": 50.0, "AED": 0.58, "GBP": 0.12, "JPY": 20.0, "CNY": 1},
    }

    def convert(val, from_currency, to_currency):
        try:
            conversion_rate = exchange_rates[from_currency][to_currency]
            return val * conversion_rate
        except KeyError:
            return "Invalid currency selected"

    def callback():
        try:
            val = float(in_field.get())
        except ValueError:
            out_val.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_val.set('Input/Output unit not chosen')
            return None
        else:
            inp = in_unit.get()
            to = out_unit.get()
            result = convert(val, inp, to)
            out_val.set(result)

    def reset():
        in_val.set('0')
        out_val.set('')
        in_unit.set('Select Unit')
        out_unit.set('Select Unit')

    window = Toplevel()
    window.title("Currency Conversion")
    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)

    titleLabel = Label(mainframe, text="Currency Conversion", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1, row=1)
    in_val = StringVar()
    in_val.set('0')
    out_val = StringVar()
    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_val)
    in_field.grid(row=1, column=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, in_unit, "USD", "EUR", "INR", "QAR", "ZWD", "AED", "GBP", "JPY", "CNY").grid(column=3, row=1, sticky=W)
    ttk.Entry(mainframe, textvariable=out_val, state="readonly").grid(column=2, row=3, sticky=(W, E))
    out_select = OptionMenu(mainframe, out_unit, "USD", "EUR", "INR", "QAR", "ZWD", "AED", "GBP", "JPY", "CNY").grid(column=3, row=3, sticky=W)
    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)
    reset_button = ttk.Button(mainframe, text="Reset", command=reset).grid(column=1, row=2, sticky=W)

    # Quit button for the individual window
    quit_button = ttk.Button(mainframe, text="Quit", command=window.destroy)
    quit_button.grid(column=2, row=4, columnspan=2, pady=10)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    in_field.focus()


# Temperature Conversion function
def temperature_conversion():
    def convert(val, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Celsius":
                return val
            elif to_unit == "Fahrenheit":
                return (val * 9/5) + 32
            elif to_unit == "Kelvin":
                return val + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (val - 32) * 5/9
            elif to_unit == "Fahrenheit":
                return val
            elif to_unit == "Kelvin":
                return (val - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return val - 273.15
            elif to_unit == "Fahrenheit":
                return (val - 273.15) * 9/5 + 32
            elif to_unit == "Kelvin":
                return val

    def callback():
        try:
            val = float(in_field.get())
        except ValueError:
            out_val.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_val.set('Input/Output unit not chosen')
            return None
        else:
            inp = in_unit.get()
            to = out_unit.get()
            result = convert(val, inp, to)
            out_val.set(result)

    def reset():
        in_val.set('0')
        out_val.set('')
        in_unit.set('Select Unit')
        out_unit.set('Select Unit')

    window = Toplevel()
    window.title("Temperature Conversion")
    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)

    titleLabel = Label(mainframe, text="Temperature Conversion", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1, row=1)
    in_val = StringVar()
    in_val.set('0')
    out_val = StringVar()
    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_val)
    in_field.grid(row=1, column=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, in_unit, "Celsius", "Fahrenheit", "Kelvin").grid(column=3, row=1, sticky=W)
    ttk.Entry(mainframe, textvariable=out_val, state="readonly").grid(column=2, row=3, sticky=(W, E))
    out_select = OptionMenu(mainframe, out_unit, "Celsius", "Fahrenheit", "Kelvin").grid(column=3, row=3, sticky=W)
    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)
    reset_button = ttk.Button(mainframe, text="Reset", command=reset).grid(column=1, row=2, sticky=W)

    # Quit button for the individual window
    quit_button = ttk.Button(mainframe, text="Quit", command=window.destroy)
    quit_button.grid(column=2, row=4, columnspan=2, pady=10)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    in_field.focus()


# Weight Conversion function
def weight_conversion():
    def convert(val, from_unit, to_unit):
        weight_units = {
            "grams": 1,
            "kilograms": 1000,
            "pounds": 453.592,
            "ounces": 28.3495,
        }
        if from_unit == to_unit:
            return val
        return (val * weight_units[from_unit]) / weight_units[to_unit]

    def callback():
        try:
            val = float(in_field.get())
        except ValueError:
            out_val.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_val.set('Input/Output unit not chosen')
            return None
        else:
            inp = in_unit.get()
            to = out_unit.get()
            result = convert(val, inp, to)
            out_val.set(result)

    def reset():
        in_val.set('0')
        out_val.set('')
        in_unit.set('Select Unit')
        out_unit.set('Select Unit')

    window = Toplevel()
    window.title("Weight Conversion")
    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)

    titleLabel = Label(mainframe, text="Weight Conversion", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1, row=1)
    in_val = StringVar()
    in_val.set('0')
    out_val = StringVar()
    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_val)
    in_field.grid(row=1, column=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, in_unit, "grams", "kilograms", "pounds", "ounces").grid(column=3, row=1, sticky=W)
    ttk.Entry(mainframe, textvariable=out_val, state="readonly").grid(column=2, row=3, sticky=(W, E))
    out_select = OptionMenu(mainframe, out_unit, "grams", "kilograms", "pounds", "ounces").grid(column=3, row=3, sticky=W)
    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)
    reset_button = ttk.Button(mainframe, text="Reset", command=reset).grid(column=1, row=2, sticky=W)

    # Quit button for the individual window
    quit_button = ttk.Button(mainframe, text="Quit", command=window.destroy)
    quit_button.grid(column=2, row=4, columnspan=2, pady=10)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    in_field.focus()


# Length Conversion function
def length_conversion():
    def convert(val, from_unit, to_unit):
        length_units = {
            "meters": 1,
            "kilometers": 1000,
            "inches": 0.0254,
            "feet": 0.3048,
            "miles": 1609.34,
        }
        if from_unit == to_unit:
            return val
        return (val * length_units[from_unit]) / length_units[to_unit]

    def callback():
        try:
            val = float(in_field.get())
        except ValueError:
            out_val.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_val.set('Input/Output unit not chosen')
            return None
        else:
            inp = in_unit.get()
            to = out_unit.get()
            result = convert(val, inp, to)
            out_val.set(result)

    def reset():
        in_val.set('0')
        out_val.set('')
        in_unit.set('Select Unit')
        out_unit.set('Select Unit')

    window = Toplevel()
    window.title("Length Conversion")
    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)

    titleLabel = Label(mainframe, text="Length Conversion", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1, row=1)
    in_val = StringVar()
    in_val.set('0')
    out_val = StringVar()
    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_val)
    in_field.grid(row=1, column=2, sticky=(W, E))
    in_select = OptionMenu(mainframe, in_unit, "meters", "kilometers", "inches", "feet", "miles").grid(column=3, row=1, sticky=W)
    ttk.Entry(mainframe, textvariable=out_val, state="readonly").grid(column=2, row=3, sticky=(W, E))
    out_select = OptionMenu(mainframe, out_unit, "meters", "kilometers", "inches", "feet", "miles").grid(column=3, row=3, sticky=W)
    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)
    reset_button = ttk.Button(mainframe, text="Reset", command=reset).grid(column=1, row=2, sticky=W)

    # Quit button for the individual window
    quit_button = ttk.Button(mainframe, text="Quit", command=window.destroy)
    quit_button.grid(column=2, row=4, columnspan=2, pady=10)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    in_field.focus()


# Main application
def main():
    root = Tk()
    root.title("Multi Converter")
    root.geometry("300x200")

    button1 = Button(root, text="Currency Conversion", command=currency_conversion)
    button1.pack(pady=10)
    button2 = Button(root, text="Temperature Conversion", command=temperature_conversion)
    button2.pack(pady=10)
    button3 = Button(root, text="Weight Conversion", command=weight_conversion)
    button3.pack(pady=10)
    button4 = Button(root, text="Length Conversion", command=length_conversion)
    button4.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

