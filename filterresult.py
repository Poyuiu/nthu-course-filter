import customtkinter
from checkboxfilter import CheckBoxFilter
import pandas as pd
import copy
import final


class Result(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.final_condition = {"time":[], "loc":[], "dep":[]}
        # customtkinter.CTkTextbox(master=self, width=250)
        self.frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame.grid(row=0, column=0, padx=20)

        # result area lebel
        self.result_label = customtkinter.CTkLabel(
            master=self.frame, text="Courses available"
        )
        self.result_label.grid(row=0, column=0, pady=20, padx=20)
        # result textbox
        self.textbox = customtkinter.CTkTextbox(
            master=self.frame,
            width=300,
            height=500,
            font=("Arial", 18),
        )
        self.textbox.grid(
            row=1,
            column=0,
            padx=(20, 20),
            pady=(0, 20),
            sticky="nsew",
        )
        self.textbox.insert("0.0", "No courses available.")
    
    def rm_null_key(self, raw_condition) -> dict:
        ''' Remove all keys with value: empty list, making the select function work correctly '''

        for key,val in raw_condition.copy().items():
            if val==[] or val==['']:
                raw_condition.pop(key)
        return raw_condition
        
    def change_filtered_result(self, filtered_result: dict, strict=False) -> None:
        # TODO: complete showing        
        for key in self.final_condition.keys():
            try:
                self.final_condition[key] = filtered_result[key]
            except KeyError:
                continue
        
        res = final.select(
            self.rm_null_key(copy.deepcopy(self.final_condition)),
            strict=strict,
        )
        self.textbox.delete("0.0", "end")
        try:
            available_courses = res["課程中文名稱"].str.cat(sep="\n")
        except:
            available_courses = "No courses available."
        self.textbox.insert("0.0", available_courses)
