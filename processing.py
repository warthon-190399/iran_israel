#%%
import pandas as pd
import requests
from bs4 import BeautifulSoup
# %%
def article_content(url):
    try:
        print("Obteniendo contenido del artículo en:", url)
        response = requests.get(url)
        print("Parseando el contenido...")
        soup = BeautifulSoup(response.content, "html.parser")
        print("Extrayendo el texto del artículo...")
        article_text = soup.get_text()
        print("Contenido del artículo obtenido exitosamente.")
        return article_text
    
    except Exception as e:
        print("Error al obtener el contenido del artículo:", e)
        return None
# %%
aj = pd.read_csv("aj.csv", delimiter=";")
cnn = pd.read_csv("cnn.csv", delimiter=";")
nyp = pd.read_csv("nyp.csv")
rt = pd.read_csv("rt.csv", delimiter=";")
# %%
rt["Contenido"] = rt["URL"].apply(article_content)
# %%
aj.to_csv("aj.csv", index=False)
cnn.to_csv("cnn.csv", index=False)
nyp.to_csv("nyp.csv", index=False)
rt.to_csv("rt.csv", index=False)
# %%
