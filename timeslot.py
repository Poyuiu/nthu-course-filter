import customtkinter
from functools import partial


class TimeSlot(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.condition = {"time": [], "loc": [], "dep": []}
        self.init_hv_title()
        self.init_buttons()

    def init_hv_title(self) -> None:
        """Brute force plotting title (pending optimization)"""
        # Horizontal Title
        self.h_title = customtkinter.CTkLabel(
            master=self,
            text=f"{' ' * 19}Mon{' ' * 13}Tue{' ' * 13}Wed{' ' * 13}Thu{' ' * 14}Fri{' ' * 14}",
            font=("Arial", 18),
        )
        self.h_title.grid(row=0, column=0, padx=10, pady=10)

        # Vertical Title
        self.v_title = customtkinter.CTkFrame(
            self, width=20, corner_radius=0, fg_color="transparent"
        )
        # Show fg color for debugging
        self.v_title = customtkinter.CTkFrame(self, width=20, corner_radius=0)
        self.v_title.grid(row=1, column=0, sticky="w", padx=(15, 0), pady=(0, 15))

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
            cur_vt = customtkinter.CTkLabel(
                master=self.v_title, text=cur_text, font=("Arial", 16)
            )
            cur_vt.grid(row=i, column=0, padx=10, pady=8)

    def init_buttons(self) -> None:
        self.buttons_grid = customtkinter.CTkFrame(self, width=20, corner_radius=10)
        self.buttons_grid.grid(row=1, column=0, sticky="ne", padx=(0, 15), pady=(0, 15))

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
                self.button_instances[j][i] = customtkinter.CTkButton(
                    master=self.buttons_grid,
                    text="",
                    fg_color="transparent",
                    border_color=button_border_color,
                    border_width=1.3,
                    hover_color=button_hover_color,
                    corner_radius=0,
                    height=43.5,
                    width=100,
                    command=button_command,
                )
                self.button_instances[j][i].grid(
                    row=i, column=j, padx=button_padx, pady=button_pady
                )

    @staticmethod
    def get_button_padx(col: int) -> tuple | int:
        if col == 0:
            return (20, 0)
        if col == 4:
            return (0, 20)
        return 0

    @staticmethod
    def get_button_pady(row: int) -> tuple | int:
        if row == 0:
            return (10, 0)
        if row == 12:
            return (0, 10)
        return 0

    @staticmethod
    def get_time_string(j: int, i: int) -> str:
        day_dict = {
            0: "M",
            1: "T",
            2: "W",
            3: "R",
            4: "F",
        }
        class_dict = {
            0: "1",
            1: "2",
            2: "3",
            3: "4",
            4: "n",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "a",
            10: "b",
            11: "c",
        }
        return f"{day_dict[j]}{class_dict[i]}"

    def switch_button_state(self, j: int, i: int) -> None:
        self.button_states[j][i] = not self.button_states[j][i]
        if self.button_states[j][i]:
            self.button_instances[j][i].configure(fg_color="#05AE60")
            self.condition["time"].append(self.get_time_string(j=j, i=i))
        else:
            self.button_instances[j][i].configure(fg_color="transparent")
            self.condition["time"].remove(self.get_time_string(j=j, i=i))
        # TODO: call textview update
        print(self.condition)
