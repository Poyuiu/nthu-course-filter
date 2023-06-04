import customtkinter

from checkboxfilter import CheckBoxFilter

class Result(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # customtkinter.CTkTextbox(master=self, width=250)
        self.frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame.grid(row=0, column=0, padx=20)
        
        # result area lebel
        self.result_label = customtkinter.CTkLabel(master=self.frame, text="Courses available")
        self.result_label.grid(row=0, column=0, pady=20, padx=20)
        # result textbox
        self.textbox = customtkinter.CTkTextbox(master=self.frame, width=300, height=500)
        self.textbox.grid(row=1, column=0, padx=(20, 20), pady=(0, 20), sticky="nsew")
