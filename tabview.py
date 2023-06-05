
import customtkinter
from getdata import get_code_loc, get_code_course
from filterresult import Result
class Tabview(customtkinter.CTkFrame):
    def __init__(self, master, result_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.result_frame = result_frame
        self.init()
    
    def init(self)->None:
        # set variable
        self.condition = {"loc": [], "dep": []}
        self.AllLoc = [f'{item[0]} {item[1]}' for item in get_code_loc()]
        self.AllLoc.insert(0, "")
        self.AllDep = [f'{item[0]} {item[1]}' for item in get_code_course()]
        self.AllDep.insert(0, "")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=200)
        self.tabview.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky='n')

        # 3 search tabs (text)
        self.tabview.add("department")
        self.tabview.add("location")
        self.tabview.add("Time")
        # object position
        self.tabview.tab("department").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("location").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Time").grid_columnconfigure(0, weight=1)

        # searching UI: department
        self.label_department = customtkinter.CTkLabel(self.tabview.tab("department"), 
                                                    text="Choose department below")
        self.label_department.grid(row=0, column=0, padx=10, pady=10)
        self.department_combobox = customtkinter.CTkOptionMenu(self.tabview.tab("department"),
                                                            values=self.AllDep,
                                                            command=self.setDepartment,
                                                            dynamic_resizing=False)
        self.department_combobox.grid(row=1, column=0, padx=10, pady=(10, 10))

        # searching UI: location
        self.label_location = customtkinter.CTkLabel(self.tabview.tab("location"), 
                                                    text="Choose location below" )
        self.label_location.grid(row=0, column=0, padx=10, pady=10)
        self.location_combobox = customtkinter.CTkOptionMenu(self.tabview.tab("location"),
                                                    values=self.AllLoc,
                                                    command=self.setLoc,
                                                    dynamic_resizing=False)
        self.location_combobox.grid(row=1, column=0, padx=10, pady=(10, 10))

        # searching UI: Time
        self.label_time = customtkinter.CTkLabel(self.tabview.tab("Time"), 
                                                text="Choose Time on RHS")
        self.label_time.grid(row=0, column=0, padx=10, pady=10)
        
        # search button
        # self.search_button = customtkinter.CTkButton(self.tabview, 
        #                                             text="Search", 
        #                                             command=self.searching)
        # self.search_button.grid(row=4, column=0, padx=10, pady=10)


    def searching(self) -> None:
        for key, val in self.condition.copy().items():
            if val==[]:
                self.condition.pop(key)
        self.result_frame.change_filtered_result(filtered_result = self.condition, strict=True)

    def setLoc(self, newLoc: str):
        tmplist = newLoc.split(' ')
        tmplist.pop()
        self.condition["loc"] = [' '.join(tmplist)]
        self.searching()
        # print(self.condition)

    def setDepartment(self, newDep: str):
        self.condition["dep"] = [newDep.split(' ')[0]]
        self.searching()
        # print(self.condition)
