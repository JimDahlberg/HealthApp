from math import prod
import tkinter as tk
import Functions

class Subpage():
    def __init__(self, root, container, current_login):
        """Creates the base for the content frames"""
        self._subpage_frame = tk.Frame(
            container,
            bg="LightBlue3"
        )
        self._subpage_frame.place(
            relwidth = 1.0,
            y=root.winfo_screenheight()/20
        )
        self._current_login = current_login
        self._functions = Functions.Functions()

    def unpack(self):
        self._subpage_frame.destroy()

class ProductsPage(Subpage):
    def __init__(self, root, container, current_login):
        """Placeholder for product page constructor"""
        super().__init__(root, container, current_login)

        food_list = self._functions.get_list_of_food()
        for i in range(len(food_list)):
            parent = tk.LabelFrame(
                self._subpage_frame,
                text=f"{food_list[i]['ItemName']}",
                padx=50
            )
            parent.grid(row=i, column=0)
            
            btn_temp = tk.Button(
                self._subpage_frame, 
                text="+Add Item")
            btn_temp.grid(row=i, column=1)
            

            food_information = []
            food_information.append(tk.Label(
                parent,
                text=f"Kcal: {food_list[i]['kcal']}"
            ))
            food_information.append(tk.Label(
                parent,
                text=f"Fat: {food_list[i]['Fat']}"
            ))
            food_information.append(tk.Label(
                parent,
                text=f"Carbs: {food_list[i]['Carbs']}"
            ))
            food_information.append(tk.Label(
                parent,
                text=f"Protein: {food_list[i]['Protein']}"
            ))
            for j in range(len(food_information)):
                food_information[j].grid(row=j, column=0)

class ProfilePage(Subpage):
    """Placeholder"""
    def __init__(self, root, container, current_login):
        super().__init__(root, container, current_login)