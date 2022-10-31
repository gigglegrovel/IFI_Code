
#%%
import pandas as pd
#from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
#with open('C:/Users/End User/Downloads/MX_Feed_Especial.xml', 'r',encoding="utf8") as f:
 #   data = f.read()

#bs_data = BeautifulSoup(data, 'xml')

#print(bs_data.prettify())

tree = ET.parse('C:/Users/End User/Downloads/MX_Feed_Especial.xml')
root = tree.getroot()

tags = ["id","title","url","content","property_type","operation_type","city",
"city_area","region","latitude","longitude","direccion","bathrooms","rooms",
"built_floor_area","price","currency","due_date","year_built","garage","publisher_name",
"url_image","images"]

dicc = {}

for i in range(len(tags)):
    dicc[tags[i]]=[]

for i in range(len(tags)):
    for element in root.iter(tags[i]):
        dicc[tags[i]].append(element.text)

data = pd.DataFrame(dicc)

data.to_excel("C:/Users/End User/Downloads/1_14_2022_xml.xlsx")


# %%
#for id in root.iter("id"):
  #  print(id.text)