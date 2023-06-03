import tkinter
import tkinter.messagebox
import customtkinter
from functools import partial

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
        self.h_title = customtkinter.CTkLabel(master=self, text=f"{' ' * 19}Mon{' ' * 13}Tue{' ' * 13}Wed{' ' * 13}Thu{' ' * 14}Fri{' ' * 14}", font=("Arial", 18))
        self.h_title.grid(row=0, column=0, padx=10, pady=10)

        # Vertical Title
        self.v_title = customtkinter.CTkFrame(self, width=20, corner_radius=0, fg_color='transparent')
        # Show fg color for debugging
        self.v_title = customtkinter.CTkFrame(self, width=20, corner_radius=0)
        self.v_title.grid(row=1, column=0, sticky="w", padx=(15,0), pady=(0,15))

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
        self.buttons_grid.grid(row=1, column=0, sticky="ne", padx=(0,15), pady=(0,15))

        # (pending discussion) color
        general_border_color = "gray"
        noon_border_color = "#f0f100"
        abc_border_color = "#02dafd"
        button_hover_color = "#AAFEC2"

        self.button_instances = [[None] * 13 for _ in range(5)]
        self.button_states = [[False] * 13 for _ in range(5)]
        for i in range(13):
            for j in range(5):
                if i >= 9:
                    button_border_color = abc_border_color
                elif i == 4:
                    button_border_color = noon_border_color
                else:
                    button_border_color = general_border_color

                button_padx = self.get_button_padx(col=j)
                button_pady = self.get_button_pady(row=i)

                button_command = partial(self.switch_button_state, j, i)
                self.button_instances[j][i] = customtkinter.CTkButton(master=self.buttons_grid, text="",fg_color="transparent", border_color=button_border_color, border_width=1.3, hover_color=button_hover_color, corner_radius=0, height=43.5, width=100, command=button_command)
                self.button_instances[j][i].grid(row=i, column=j, padx=button_padx, pady=button_pady)
    
    @staticmethod
    def get_button_padx(col: int)->tuple|int:
        if col == 0:
            return (20, 0)
        if col == 4:
            return (0, 20)
        return 0
    
    @staticmethod
    def get_button_pady(row: int)->tuple|int:
        if row == 0:
            return (10, 0)
        if row == 12:
            return (0, 10)
        return 0

    def switch_button_state(self, j:int, i:int)->None:
        self.button_states[j][i] = not self.button_states[j][i]
        if self.button_states[j][i]:
            self.button_instances[j][i].configure(fg_color="#05AE60")
        else:
            self.button_instances[j][i].configure(fg_color="transparent")

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
