import customtkinter
from tabview import Tabview
from checkboxfilter import CheckBoxFilter

class LeftSideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        customtkinter.CTkFrame(self, width=140, corner_radius=0)
        # Searching tabview
        self.search_tab = Tabview(master=self)
        self.search_tab.grid(row=0, column=0, sticky='n')

        # result filter
        self.result_filter = CheckBoxFilter(master = self)
        self.result_filter.grid(row=1, column=0, pady=0, sticky='n')

        # appearance mode
        self.appearance_mode_label = customtkinter.CTkLabel(master = self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=2, column=0, padx=20)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master = self, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=3, column=0, padx=20)

        # scaling
        self.scaling_label = customtkinter.CTkLabel(master = self, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(master = self, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(0,10))

        # set default
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)