import pandas as pd
import requests, os

response = requests.get('http://140.114.49.183/download.php')

with open('cur.xlsx', 'wb') as file:
    file.write(response.content)
    file.close()


df = pd.read_excel('cur.xlsx')
os.remove("cur.xlsx")


def select(target:dict = {}  ):
    '''
        target: {
            "time":[] (ex. ["F1", "F5"])
            "loc" :[] (ex. ["GEN ll", "HSS"]) 
            "dep" :[] (ex. ["AES", "CS", "EE"])
        }
    '''
    series_ls =[]
    for _, item in df.iterrows():
        flag1 = False
        flag2 = False
        flag3 = False
        for key in target.keys():

            for condi in target[key]:
                if key == "time":
                    if not pd.isnull(item['教室與上課時間']):
                        if condi in item["教室與上課時間"]:
                            flag1 = True
                elif key == "loc" :
                    if not pd.isnull(item['教室與上課時間']):
                        if condi in item["教室與上課時間"]:
                            flag2 = True
                else:
                    if condi in item["科號"]:
                        flag3 = True

            
        if 'time' not in target.keys():
            flag1 = True
        if 'loc' not in target.keys():
            flag2 = True
        if 'dep' not in target.keys():
            flag3 = True

        if flag1 and flag2 and flag3:
            series_ls.append(item)
    
    return pd.DataFrame(series_ls)

if __name__ == "__main__":
    temp = select({"time": ["F3", "F4", "M1"],"loc" : ["GEN II", "ENG I"], "dep": ["MATH"]})
    # temp.to_csv("./out.csv")
    print(temp[["科號", "教室與上課時間"]])

    temp = select({"time": ["M3", "T4", "M1"]})
    # temp.to_csv("./out.csv")
    print(temp[["科號", "教室與上課時間"]])

    temp = select({"time": ["Ma", "Mb", "Mc"],"loc" : ["GEN II", "ENG I"]})
    # temp.to_csv("./out.csv")
    print(temp[["科號", "教室與上課時間"]])