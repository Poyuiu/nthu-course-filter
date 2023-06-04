
import customtkinter

class Tabview(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=200)
        self.tabview.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky='n')
        

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
        self.label_major.grid(row=0, column=0, padx=10, pady=10)
        self.major_combobox = customtkinter.CTkComboBox(self.tabview.tab("major"),
                                                    values=["", "AES", "AIIM", "CS", "CSR"])
        self.major_combobox.grid(row=1, column=0, padx=10, pady=(10, 10))
        # searching UI: location
        self.label_location = customtkinter.CTkLabel(self.tabview.tab("location"), text="Choose location below")
        self.label_location.grid(row=0, column=0, padx=10, pady=10)
        self.location_combobox = customtkinter.CTkComboBox(self.tabview.tab("location"),
                                                    values=[ "", "GEN I", "DELTA", "HSS", "Nanda" ] )
        self.location_combobox.grid(row=1, column=0, padx=10, pady=(10, 10))

        # searching UI: Time
        self.label_time = customtkinter.CTkLabel(self.tabview.tab("Time"), text="Choose Time on RHS")
        self.label_time.grid(row=0, column=0, padx=10, pady=10)
        
        # search button
        self.search_button = customtkinter.CTkButton(self.tabview, text="Search", command=self.searching)
        self.search_button.grid(row=4, column=0, padx=10, pady=10)

    def searching(self) -> None:
        print("searching, Nothing so far...")


