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
        self.buttons_grid = customtkinter.CTkFrame(self, width=20, corner_radius=10)
        self.buttons_grid.grid(row=1, column=0, sticky="n", padx=10, pady=(0,10))
        self.string_input_button = customtkinter.CTkButton(master=self.buttons_grid, text="",fg_color="transparent", border_color="green", border_width=2, hover_color="green")
        self.string_input_button.grid(row=0, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(master=self.buttons_grid, text="",fg_color="transparent", border_color="green", border_width=2, hover_color="green")
        self.string_input_button.grid(row=1, column=1, padx=20, pady=(10, 10))

class Tabview(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=200)
        self.tabview.grid(row=0, column=0, rowspan=2, padx=20, pady=10, sticky='n')
        

        # 3 search tabs (text)
        self.tabview.add("major")
        self.tabview.add("location")
        self.tabview.add("Time")
        # object position
        self.tabview.tab("major").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("location").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Time").grid_columnconfigure(0, weight=1)
        # searching UI: major
        self.label_major = customtkinter.CTkLabel(self.tabview.tab("major"), text="Choose major below")
        self.label_major.grid(row=0, column=0, padx=20, pady=20)
        self.major_combobox = customtkinter.CTkComboBox(self.tabview.tab("major"),
                                                    values=["請選擇...", "資工", "電機", "物理", "..."])
        self.major_combobox.grid(row=1, column=0, padx=20, pady=(10, 10))
        # searching UI: location
        self.label_location = customtkinter.CTkLabel(self.tabview.tab("location"), text="Choose location below")
        self.label_location.grid(row=0, column=0, padx=20, pady=20)
        self.location_combobox = customtkinter.CTkComboBox(self.tabview.tab("location"),
                                                    values=["請選擇...", "台達", "資電", "人社", "..."])
        self.location_combobox.grid(row=1, column=0, padx=20, pady=(10, 10))

        # searching UI: Time
        self.label_time = customtkinter.CTkLabel(self.tabview.tab("Time"), text="Choose Time on RHS")
        self.label_time.grid(row=0, column=0, padx=20, pady=20)
        
        # search button
        self.search_button = customtkinter.CTkButton(self.tabview, text="Search", command=self.searching)
        self.search_button.grid(row=4, column=0, padx=20, pady=10)

    def searching(self) -> None:
        print("searching, Nothing so far...")
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("nthu-course-filter")
        self.geometry(f"{1100}x{670}")
        
        # Time slot
        self.time_slot = TimeSlot(master=self)
        self.time_slot.grid(row=0, column=1, pady=20, sticky='n')

        # Searching tabview
        self.time_slot = Tabview(master=self)
        self.time_slot.grid(row=0, column=0, pady=20, sticky='n')

        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

if __name__ == "__main__":
    app = App()
    app.mainloop()
