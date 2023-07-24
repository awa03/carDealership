import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Engine:
    def __init__(self, engine_type):
        self.type = engine_type

    def get_engine_type(self):
        return self.type


class Car:
    def __init__(self, car_model, car_year, engine_type, color, price, car_id):
        self.name = car_model
        self.year = car_year
        self.engine = Engine(engine_type)
        self.color = color
        self.price = price
        self.id = car_id

    def display_info(self):
        return (
            "#######################################\n"
            "  {}\n"
            "#######################################\n"
            "Year: {}\n"
            "Color: {}\n"
            "Engine: {}\n"
            "ID number: {}\n\n".format(
                self.name, self.year, self.color, self.engine.get_engine_type(), self.id
            )
        )

class Dealership:
    def __init__(self):
        self.car_list = []
        self.balance = 0

    def add_car(self, car):
        for existing_car in self.car_list:
            if car.id == existing_car.id:
                return False

        self.car_list.append(car)
        return True

    def add_new_car(self, car_model, car_year, engine_type, color, price, car_id, buy=False):
        if buy:
            self.balance -= price

        for existing_car in self.car_list:
            if car_id == existing_car.id:
                return False

        car = Car(car_model, car_year, engine_type, color, price, car_id)
        self.car_list.append(car)
        return True

    def sell_car(self, sell_id):
        for car in self.car_list:
            if car.id == sell_id:
                self.balance += car.price
                self.car_list.remove(car)
                return True

        return False

    def get_balance(self):
        return self.balance

    def get_car_info(self):
        car_info = ""
        for car in self.car_list:
            car_info += car.display_info()
        return car_info

def show_balance():
    balance = store.get_balance()
    messagebox.showinfo("Balance", "The current balance is: $" + str(balance))

def add_car_window():
    def add_car():
        car_model = car_model_entry.get()
        car_year = int(car_year_entry.get())
        engine_type = engine_type_entry.get()
        color = color_entry.get()
        price = int(price_entry.get())
        car_id = int(car_id_entry.get())
        added = store.add_new_car(car_model, car_year, engine_type, color, price, car_id, buy_var.get())
        if added:
            messagebox.showinfo("Success", "Car added successfully.")
        else:
            messagebox.showerror("Error", "Car with ID " + str(car_id) + " already exists.")
        add_car_window.destroy()

    
    
    add_car_window = tk.Toplevel(root)
    add_car_window.title("Add Car")
    add_car_window.geometry("300x200")

    car_model_label = tk.Label(add_car_window, text="Car Model:")
    car_model_label.pack()
    car_model_entry = tk.Entry(add_car_window)
    car_model_entry.pack()

    car_year_label = tk.Label(add_car_window, text="Car Year:")
    car_year_label.pack()
    car_year_entry = tk.Entry(add_car_window)
    car_year_entry.pack()

    engine_type_label = tk.Label(add_car_window, text="Engine Type:")
    engine_type_label.pack()
    engine_type_entry = tk.Entry(add_car_window)
    engine_type_entry.pack()

    color_label = tk.Label(add_car_window, text="Color:")
    color_label.pack()
    color_entry = tk.Entry(add_car_window)
    color_entry.pack()

    price_label = tk.Label(add_car_window, text="Price:")
    price_label.pack()
    price_entry = tk.Entry(add_car_window)
    price_entry.pack()

    car_id_label = tk.Label(add_car_window, text="Car ID:")
    car_id_label.pack()
    car_id_entry = tk.Entry(add_car_window)
    car_id_entry.pack()

    buy_var = tk.BooleanVar()
    buy_checkbutton = tk.Checkbutton(add_car_window, text="Buy?", variable=buy_var)
    buy_checkbutton.pack()

    add_button = tk.Button(add_car_window, text="Add", command=add_car)
    add_button.pack()

def sell_car_window():
    def sell_car():
        car_id = int(car_id_entry.get())
        sold = store.sell_car(car_id)
        if sold:
            messagebox.showinfo("Success", "Car sold successfully.")
        else:
            messagebox.showerror("Error", "Car with ID " + str(car_id) + " not found.")
        sell_car_window.destroy()

    sell_car_window = tk.Toplevel(root)
    sell_car_window.title("Sell Car")
    sell_car_window.geometry("1200x1000")

    car_id_label = tk.Label(sell_car_window, text="Car ID:")
    car_id_label.pack()
    car_id_entry = tk.Entry(sell_car_window)
    car_id_entry.pack()

    sell_button = tk.Button(sell_car_window, text="Sell", command=sell_car)
    sell_button.pack()

def view_cars_window():
    view_cars_window = tk.Toplevel(root)
    view_cars_window.title("View Cars")
    view_cars_window.geometry("600x300")

    cars_info = tk.Text(view_cars_window, wrap=tk.WORD)
    cars_info.pack()
    cars_info.insert(tk.END, store.get_car_info())


def main():
    global root, store
    root = tk.Tk()
    root.title("Aidens Dealership")
    root.geometry("300x300")  # Increased height to accommodate the image

    store = Dealership()

    # Example Cars
    store.add_new_car("Chevrolet", 2021, "v6", "white", 90000, 72984, buy=False)
    store.add_new_car("BMW", 2023, "v8", "silver", 150000, 63218, buy=False)
    # Add more example cars here...

    # Load the image
    img = Image.open("img1.jpg")
    img = img.resize((500, 300))  # Resize the image to the desired dimensions
    img = ImageTk.PhotoImage(img)

    # Create the image label
    img_label = tk.Label(root, image=img)
    img_label.pack()

    menu_frame = tk.Frame(root)
    menu_frame.pack()

    add_button = tk.Button(menu_frame, text="Add Car", command=add_car_window)
    add_button.pack(side=tk.LEFT)

    sell_button = tk.Button(menu_frame, text="Sell Car", command=sell_car_window)
    sell_button.pack(side=tk.LEFT)

    view_cars_button = tk.Button(menu_frame, text="View Cars", command=view_cars_window)
    view_cars_button.pack(side=tk.LEFT)

    balance_button = tk.Button(menu_frame, text="Balance", command=show_balance)
    balance_button.pack(side=tk.LEFT)

    exit_button = tk.Button(menu_frame, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
