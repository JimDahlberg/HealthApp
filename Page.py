import tkinter as tk
from tkinter.constants import S
from typing import Collection
import Subpage
import Functions

class Page:
    def __init__(self, root,container):
        """Creates the base frame for the Login screen, Sign up screen and the Content pages"""


        self._root = root
        self._container = container
        self._functions = Functions.Functions()

        self._page = tk.Frame(
            container, 
            bg="LightBlue3",
            width=root.winfo_screenwidth(),
            height=root.winfo_screenheight(), 
        )

        self._page.pack()

    def unpack(self):
        self._page.destroy()

class LoginGUI(Page):
    def __init__(self, root, container):
        """Creates the widgets used for login functionality"""
        super().__init__(root, container)

        self._login_box = tk.Frame(self._page)
        self._login_box.place(
            x=root.winfo_screenwidth()/2,
            y=root.winfo_screenheight()/2,
            anchor=tk.CENTER
        )

        self._lbl_username= tk.Label(
            self._login_box, 
            text="Username",
            padx=10,
            pady=5
        )
        self._lbl_username.grid(
            row=0,
            column=0
        )

        self._lbl_password = tk.Label(
            self._login_box,
            text="Password",
            padx=10.0,
            pady=5.0
        )
        self._lbl_password.grid(
            row=1,
            column=0
        )

        self._entry_username = tk.Entry(
            self._login_box
        )
        self._entry_username.grid(
            row=0,
            column=1
        )

        self._entry_password = tk.Entry(
            self._login_box,
            show="*"
        )
        self._entry_password.grid(
            row=1,
            column=1
        )

        self._btn_sign_in = tk.Button(
            self._login_box,
            text="Sign in",
            padx=8,
            pady=4,
            command=self.sign_in
        )
        self._btn_sign_in.grid(
            row=3,
            column=0
        )
        self._btn_sign_up = tk.Button(
            self._login_box,
            text="Sign up",
            padx=8,
            pady=4,
            command=self.signup_page
        )
        self._btn_sign_up.grid(
            row=3,
            column=1
        )

        self._lbl_wrong_username = tk.Label(
            self._login_box,
            text="",
            fg="Red"
        )
        self._lbl_wrong_username.grid(
            row=0,
            column=3
        )

        self._lbl_wrong_password = tk.Label(
            self._login_box,
            text="",
            fg="Red"
        )
        self._lbl_wrong_password.grid(
            row=1,
            column=3
        )

    
    def signup_page(self):
        """Used for the sign up button, unpacks the LoginGUI class and packs the SignUp class"""

        self.unpack()
        SignUp(self._root, self._container)
    
    def sign_in(self):
        """Used for the login button, succesful login unpacks the LoginGui class and starts the MainPage class"""

        login_attempt = self._functions.login(
            self._entry_username.get(), 
            self._entry_password.get()
            )

        if login_attempt == "usrError":
            self._lbl_wrong_username.config(fg="red", text="Username not recognised!")
            self._lbl_wrong_password.config(text="")
        elif login_attempt == "pwError":
            self._lbl_wrong_username.config(text="")
            self._lbl_wrong_password.config(text="Password not recognised!")
        else:
            self.unpack()
            MainPage(self._root, self._container, login_attempt)

class SignUp(Page):
    """Creates the widgets used for signup functionality"""
    def __init__(self, root, container):
        super().__init__(root, container)

        self._signup_box = tk.Frame(self._page)
        self._signup_box.place(
            x=root.winfo_screenwidth()/2,
            y=root.winfo_screenheight()/2,
            anchor=tk.CENTER
        )

        self._lbl_username = tk.Label(
            self._signup_box,
            text="Username",
            padx=10.0,
            pady=5.0
        )
        self._lbl_username.grid(
            row=0,
            column=0
        )

        self._entry_username = tk.Entry(
            self._signup_box
        )
        self._entry_username.grid(
            row=0,
            column=1
        )

        self._lbl_wrong_username = tk.Label(
            self._signup_box,
            text="",
            fg="Red"
        )
        self._lbl_wrong_username.grid(
            row=0,
            column=2
        )

        self._lbl_password = tk.Label(
            self._signup_box,
            text="Password",
            padx=10.0,
            pady=5.0
        )
        self._lbl_password.grid(
            row=1,
            column=0
        )
        
        self._entry_password = tk.Entry(
            self._signup_box
        )
        self._entry_password.grid(
            row=1,
            column=1
        )

        self._lbl_wrong_password = tk.Label(
            self._signup_box,
            text="",
            fg="Red"
        )
        self._lbl_wrong_password.grid(
            row=1,
            column=2
        )

        self._lbl_gender = tk.Label(
            self._signup_box,
            text="Gender",
            padx=10.0,
            pady=5.0
        )
        self._lbl_gender.grid(
            row=2,
            column=0
        )
        
        gender_value = tk.StringVar(self._signup_box)
        self._opt_gender = tk.OptionMenu(
            self._signup_box,
            gender_value,
            "Man", "Woman"
        )
        self._opt_gender.grid(
            row=2,
            column=1
        )

        self._lbl_current_weigth = tk.Label(
            self._signup_box,
            text = "Current weigth",
            padx=10.0,
            pady=5.0
        )
        self._lbl_current_weigth.grid(
            row=3,
            column=0
        )

        self._entry_current_weigth = tk.Entry(
            self._signup_box,
        )
        self._entry_current_weigth.grid(
            row=3,
            column=1
        )

        self._lbl_goal_weigth = tk.Label(
            self._signup_box,
            text="Goal weight",
            padx=10.0,
            pady=5.0 
        )
        self._lbl_goal_weigth.grid(
            row=4,
            column=0
        )

        self._entry_goal_weigth = tk.Entry(
            self._signup_box
        )
        self._entry_goal_weigth.grid(
            row=4,
            column=1
        )
        
        self._lbl_set_goal = tk.Label(
            self._signup_box,
            text="Set Goal",
            padx=10.0,
            pady=5.0
        )
        self._lbl_set_goal.grid(
            row=5,
            column=0
        )
        
        goal_value = tk.StringVar(self._signup_box)
        self._opt_set_goal = tk.OptionMenu(
            self._signup_box,
            goal_value,
            "Gain weigth", "Maintain weigth", "Lose weigth"
        )
        self._opt_set_goal.grid(
            row=5,
            column=1
        )

        self._btn_to_login = tk.Button(
            self._signup_box,
            text="Back",
            padx=8,
            pady=4,
            command=self.login_page
        )
        self._btn_to_login.grid(
            row=6,
            column=1
        )
        
        self._btn_sign_in = tk.Button(
            self._signup_box,
            text="Sign up",
            padx=10.0,
            pady=5.0,
            command=self.sign_up
        )
        self._btn_sign_in.grid(
            row=6,
            column=0
        )

    def login_page(self):
        """Used for buttons that redirect to the login screen, unpacks the frame and creates the LoginGUI"""

        self.unpack()
        LoginGUI(self._root, self._container)

    def sign_up(self):
        """Functionality used to insert new accounts into database, not fully implemented"""
        signup_attempt = self._functions.sign_up(
            self._entry_username.get(),
            self._entry_password.get(),
            "",
            "",
            ""
            )

        if signup_attempt == "Succes":
            username = self._entry_username.get()
            
            for widget in self._signup_box.winfo_children():
                widget.destroy()
            
            lbl_account_created = tk.Label(
                self._signup_box,
                text=f"Welcome to Health Application {username}!"
            )
            lbl_account_created.grid(
                row=0,
                column=0
            )

            btn_to_login = tk.Button(
                self._signup_box,
                text="Sign in",
                padx=8.0,
                pady=4.0,
                command=self.login_page
            )
            btn_to_login.grid(
                row=1,
                column=0
            )
            
        elif signup_attempt == "usrError":
            self._lbl_wrong_username.config(text="Username taken, try again", fg="Red")


class MainPage(Page):
    def __init__(self, root, container, loginID):
        """Creates the frame for the content pages"""
        super().__init__(root, container)

        self._current_login = loginID

        self._menu_frame = tk.Frame(
            self._page,
            width=root.winfo_screenwidth(),
            height=root.winfo_screenheight()/20,
            bg="LightBlue4"
            )
        self._menu_frame.place(
            x=0,
            y=0
            )
        
        self._btn1_menu = tk.Button(
            self._menu_frame,
            bg="LightBlue4",
            fg="White",
            text="Products",
            command=self.press_products
        )
        self._btn1_menu.place(
            relheight=1.0, 
            relwidth=1.0/5.0,
            relx=0.0/5.0
        )

        self._btn2_menu = tk.Button(
            self._menu_frame,
            bg="LightBlue4",
            fg="White",
            text="Profile",
            command=self.press_profile
        )
        self._btn2_menu.place(
            relheight=1.0,
            relwidth=1.0/5.0, 
            relx=1.0/5.0
        )

        self._btn3_menu = tk.Button(
            self._menu_frame,
            bg="LightBlue4",
            fg="White",
            text="Personal Statistics",
            command=self.press_personal_statistics
        )
        self._btn3_menu.place(
            relheight=1.0,
            relwidth=1.0/5.0, 
            relx=2.0/5.0
        )
        
        self._btn_sign_out = tk.Button(
            self._menu_frame,
            text="Sign out",
            width=6,
            pady=3,
            command=self.press_signout
        )
        self._btn_sign_out.place(
            relx=0.95/1.0,
            rely=0.3/1.0
            )

        self._lbl_signed_in_as = tk.Label(
            self._menu_frame,
            text=f"Signed in as {self._functions.get_username(self._current_login)}",
            pady=4,
            bg="LightBlue4",
            fg="white"
        )
        self._lbl_signed_in_as.place(
            rely=0.3/1.0,
            relx= 0.85/1.0
        )

        self._subpage = Subpage.ProductsPage(self._root, self._container, self._current_login)

    def press_signout(self):
        """Redirect to the login screen"""
        self.unpack()
        LoginGUI(self._root, self._container)

    def press_products(self):
        """Redirect to product page"""
        self._subpage.unpack()
        self._subpage = Subpage.ProductsPage(self._root, self._container, self._current_login)
    
    def press_profile(self):
        """Redirect to profile page"""
        self._subpage.unpack()
        self._subpage = Subpage.ProfilePage(self._root, self._container, self._current_login)
    
    def press_personal_statistics(self):
        """Placeholder"""
        self._subpage.unpack()
        self._subpage = Subpage.Subpage(self._root, self._container, self._current_login)