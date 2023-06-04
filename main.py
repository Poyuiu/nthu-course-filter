import tkinter
import tkinter.messagebox
import customtkinter
from timeslot import TimeSlot

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

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
        self.geometry(f"{1100}x{700}")
        
        # Time slot
        self.time_slot = TimeSlot(master=self)
        self.time_slot.grid(row=0, column=1, padx=20, pady=20, sticky='n')

        # Searching tabview
        self.time_slot = Tabview(master=self)
        self.time_slot.grid(row=0, column=0, pady=20, sticky='n')

        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

if __name__ == "__main__":
    app = App()
    app.mainloop()
