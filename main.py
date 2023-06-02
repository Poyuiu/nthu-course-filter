import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class TimeSlot(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.init_hv_title()
        self.init_buttons()

    def init_hv_title(self) -> None:
        """Brute force plotting title (pending optimization)"""
        # Horizontal Title
        self.h_title = customtkinter.CTkLabel(master=self, text=f"{' ' * 12}Mon{' ' * 20}Tue{' ' * 20}Wed{' ' * 20}Thu{' ' * 20}Fri{' ' * 8}", font=("Arial", 18))
        self.h_title.grid(row=0, column=0, padx=10, pady=10)

        # Vertical Title
        self.v_title = customtkinter.CTkFrame(self, width=20, corner_radius=0, fg_color='transparent')
        # Show fg color for debugging
        self.v_title = customtkinter.CTkFrame(self, width=20, corner_radius=0)
        self.v_title.grid(row=1, column=0, sticky="w", padx=10, pady=(0,10))

        self.v_titles = []
        for i in range(13):
            if i == 4:
                cur_text = "n"
            elif i == 10:
                cur_text = "a"
            elif i == 11:
                cur_text = "b"
            elif i == 12:
                cur_text = "c"
            elif i < 4:
                cur_text = str(i + 1)
            else:
                cur_text = str(i)
            cur_vt = customtkinter.CTkLabel(master=self.v_title, text=cur_text, font=("Arial",16))
            cur_vt.grid(row=i, column=0, padx=10, pady=8)

    def init_buttons(self) -> None:
        pass

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("nthu-course-filter")
        self.geometry(f"{1100}x{670}")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=200)
        self.tabview.grid(row=0, column=0, padx=20, pady=10, sticky='n')
        self.tabview.add("major")
        self.tabview.add("location")
        self.tabview.add("Time")

        self.tabview.tab("major").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("location").grid_columnconfigure(0, weight=1)

        self.time_slot = TimeSlot(master=self)
        self.time_slot.grid(row=0, column=1, pady=20, sticky='n')
        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("major"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("major"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("major"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("major"), text="Choose major below")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("location"), text="Choose location below")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.label_tab_3 = customtkinter.CTkLabel(self.tabview.tab("Time"), text="Choose Time on RHS")
        self.label_tab_3.grid(row=0, column=0, padx=30, pady=20)
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("location"), text="CTkLabel on location")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

if __name__ == "__main__":
    app = App()
    app.mainloop()
