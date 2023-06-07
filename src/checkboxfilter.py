import customtkinter


class CheckBoxFilter(customtkinter.CTkFrame):
    def __init__(self, master, result_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.result_frame = result_frame

        self.checkbox_slider_frame = customtkinter.CTkFrame(self, width=200)
        self.checkbox_slider_frame.grid(
            row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="n"
        )

        # checkbox lebel
        self.label_filter = customtkinter.CTkLabel(
            self.checkbox_slider_frame, text="Result filter", font=("Arial", 18)
        )
        self.label_filter.grid(row=0, column=0, sticky="nsew")

        # checkbox options
        self.label_content = customtkinter.CTkFrame(master=self.checkbox_slider_frame)
        self.label_content.grid(row=1, column=0, sticky="nsew")

        self.check1 = customtkinter.StringVar(value="off")
        self.checkbox_1 = customtkinter.CTkCheckBox(
            master=self.label_content,
            text="科號",
            command=self.checkbox1_act,
            variable=self.check1,
            onvalue="on",
            offvalue="off",
        )
        self.checkbox_1.grid(row=1, column=0, padx=(10), pady=(10, 10), sticky="n")

        self.check2 = customtkinter.StringVar(value="off")
        self.checkbox_2 = customtkinter.CTkCheckBox(
            master=self.label_content,
            text="地點",
            command=self.checkbox2_act,
            variable=self.check2,
            onvalue="on",
            offvalue="off",
        )
        self.checkbox_2.grid(row=2, column=0, padx=(10), pady=(10, 10), sticky="n")

        self.check3 = customtkinter.StringVar(value="off")
        self.checkbox_3 = customtkinter.CTkCheckBox(
            master=self.label_content,
            text="老師",
            command=self.checkbox3_act,
            variable=self.check3,
            onvalue="on",
            offvalue="off",
        )
        self.checkbox_3.grid(row=1, column=1, pady=(10, 10), sticky="n")

        # self.checkbox_4 = customtkinter.CTkCheckBox(master=self.label_content, text="時間")
        self.check4 = customtkinter.StringVar(value="off")
        self.checkbox_4 = customtkinter.CTkCheckBox(
            master=self.label_content,
            text="時間",
            command=self.checkbox4_act,
            variable=self.check4,
            onvalue="on",
            offvalue="off",
        )
        self.checkbox_4.grid(row=2, column=1, pady=(10, 10), sticky="n")

    def checkbox1_act(self):
        self.result_frame.change_filtered_result(
            filtered_result=None,
            checkbox_filter={"cid": (True if self.check1.get() == "on" else False)},
            strict=True,
        )

    def checkbox2_act(self):
        self.result_frame.change_filtered_result(
            filtered_result=None,
            checkbox_filter={"loc": (True if self.check2.get() == "on" else False)},
            strict=True,
        )

    def checkbox3_act(self):
        self.result_frame.change_filtered_result(
            filtered_result=None,
            checkbox_filter={"tch": (True if self.check3.get() == "on" else False)},
            strict=True,
        )

    def checkbox4_act(self):
        self.result_frame.change_filtered_result(
            filtered_result=None,
            checkbox_filter={"t": (True if self.check4.get() == "on" else False)},
            strict=True,
        )
