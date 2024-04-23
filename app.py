import tkinter as tkinter
from tkinter import filedialog
import pandas as panda
import json

arquivoExcel = r"C:\Users\arthur.oliveira\Downloads\Lotação BNMP.xlsx"
extracData = panda.read_excel(arquivoExcel)

objetoJson = []
for _, linha in extracData.iterrows():
    objetoJsonDic = {
        "label": linha['UNIDADE'],
        "description": f"{linha['INSTÂNCIA']} > {linha['COMARCA']} > {linha['UNIDADE']}",
        "scope": "bpmn2",
        "searchTerms": [linha['INSTÂNCIA'], linha['COMARCA']]
    }
    objetoJson.append(objetoJsonDic)

json_sring = json.dumps(objetoJson, indent=4, ensure_ascii=False)
print(json_sring)