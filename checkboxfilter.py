import customtkinter

class CheckBoxFilter(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.checkbox_slider_frame = customtkinter.CTkFrame(self, width=200)
        self.checkbox_slider_frame.grid(row=0, column=0, rowspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        # checkbox lebel
        self.label_filter = customtkinter.CTkLabel(self.checkbox_slider_frame, text="Result filter")
        self.label_filter.grid(row=0, column=0, sticky="nsew")
        
        # checkbox options
        self.label_content = customtkinter.CTkFrame(master=self.checkbox_slider_frame)
        self.label_content.grid(row=1, column=0, sticky="nsew")


        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.label_content, text="科號")
        self.checkbox_1.grid(row=1, column=0, padx=(10), pady=(10, 10), sticky="n")

        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.label_content, text="地點")
        self.checkbox_2.grid(row=2, column=0, padx=(10), pady=(10, 10), sticky="n")

        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.label_content, text="人限")
        # self.checkbox_3.grid(row=3, column=0, padx=(10), pady=(10, 10), sticky="n")

        self.checkbox_4 = customtkinter.CTkCheckBox(master=self.label_content, text="老師")
        self.checkbox_4.grid(row=1, column=1, pady=(10, 10), sticky="n")

        self.checkbox_5 = customtkinter.CTkCheckBox(master=self.label_content, text="時間")
        self.checkbox_5.grid(row=2, column=1, pady=(10, 10), sticky="n")

        # self.checkbox_6 = customtkinter.CTkCheckBox(master=self.label_content, text="學分")
        # self.checkbox_6.grid(row=3, column=1, pady=(10, 10), sticky="n")