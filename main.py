import tkinter
import tkinter.messagebox
import customtkinter
from final import select
from timeslot import TimeSlot
from leftsidebar import LeftSideBar
from tabview import Tabview
from checkboxfilter import CheckBoxFilter
from filterresult import Result

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("nthu-course-filter")
        self.geometry(f"{1300}x{700}")
        
        # left Side bar
        self.sidebar_frame = LeftSideBar(master=self)
        self.sidebar_frame.grid(row=0, column=0, pady=(20,20), rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Time slot
        self.time_slot = TimeSlot(master=self)
        self.time_slot.grid(row=0, column=1, padx=20, pady=20, sticky='n')

        # Textbox
        self.result_frame = Result(master=self)
        self.result_frame.grid(row=0, column=2, padx=(0, 0), pady=20, sticky="nsew")
        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

if __name__ == "__main__":
    app = App()
    app.mainloop()
