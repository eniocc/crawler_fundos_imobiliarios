import requests
import pandas as pd
from bs4 import BeautifulSoup as BS

url = 'https://www.fundsexplorer.com.br/ranking'

#html = urllib.request.urlopen(url)
data = requests.get(url).text

soup = BS(data, 'html.parser')

# print('Classes of each table:')
# for table in soup.find_all('table'):
#     print(table.get('class'))

tables = soup.find_all('table')

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = soup.find('table', class_='table table-hover')

df = pd.DataFrame(columns=["COD", "SETOR","PRECO_ATUAL","LIQUIDEZ_DIARIA","DIVIDENDO","DIVIDEND_YIELD","DY_3M_ACUM","DY_6M_ACUM","DY_12M_ACUM","DY_3M_MEDIA","DY_6M_MEDIA","DY_12M_MEDIA","DY_ANO","VARIACAO_PRECO","RENTAB_PERIODO","RENTAB_ACUM","PATRIMONIO_LIQ","VPA","P_VPA","DY_PATRIMONIAL","VARIACAO_PATRIMONIAL","RENTAB_PATR_NO_PERIODO","RENTAB_PATR_ACUM","VACANCIA_FISICA","VACANCIA_FINANCEIRA","QUANTIDADE_ATIVOS"])

for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        cod = columns[0].text.strip()
        setor = columns[1].text.strip()
        preco_atual = columns[2].text.strip("R$ ")
        liquidez_diaria = columns[3].text.strip(".0") #.span.contents[0].strip('&0.')
        dividendo = columns[4].text.strip("R$ ") #.span.contents[0].strip('&0.')
        dividendo_yield = columns[5].text.strip("%") #.span.contents[0].strip('&0.')
        dy_3m_acum = columns[6].text.strip("%")
        dy_6m_acum = columns[7].text.strip("%")
        dy_12m_acum = columns[8].text.strip("%")
        dy_3m_media = columns[9].text.strip("%")
        dy_6m_media = columns[10].text.strip("%")
        dy_12m_media = columns[11].text.strip("%")
        dy_ano = columns[12].text.strip("%")
        variacao_preco = columns[13].text.strip("%")
        rentab_periodo = columns[14].text.strip("%")
        rentab_acum = columns[15].text.strip("%")
        patrimonio_liq = columns[16].text.strip("R$")
        vpa = columns[17].text.strip("R$")
        p_vpa = columns[18].text.strip()
        dy_patrimonial = columns[19].text.strip("%")
        variacao_patrimonial = columns[20].text.strip("%")
        rentab_patr_no_periodo = columns[21].text.strip("%")
        rentab_patr_acum = columns[22].text.strip("%")
        vacancia_fisica = columns[23].text.strip("%")
        vacancia_financeira = columns[24].text.strip("%")
        quantidade_ativos = columns[25].text.strip("%")

        df = df.append({'COD': cod,  'SETOR': setor, 'PRECO_ATUAL': preco_atual, 'LIQUIDEZ_DIARIA': liquidez_diaria, 'DIVIDENDO': dividendo, 'DIVIDEND_YIELD': dividendo_yield,
        "DY_3M_ACUM": dy_3m_acum, "DY_6M_ACUM": dy_6m_acum, "DY_12M_ACUM": dy_12m_acum, "DY_3M_MEDIA": dy_3m_media, "DY_6M_MEDIA": dy_6m_media, "DY_12M_MEDIA": dy_12m_media, 
        "DY_ANO": dy_ano, "VARIACAO_PRECO": variacao_preco, "RENTAB_PERIODO": rentab_periodo, "RENTAB_ACUM": rentab_acum, "PATRIMONIO_LIQ": patrimonio_liq, "VPA": vpa, 
        "P_VPA": p_vpa, "DY_PATRIMONIAL": dy_patrimonial, "VARIACAO_PATRIMONIAL": variacao_patrimonial, "RENTAB_PATR_NO_PERIODO": rentab_patr_no_periodo, "RENTAB_PATR_ACUM": rentab_patr_acum,
        "VACANCIA_FISICA": vacancia_fisica, "VACANCIA_FINANCEIRA": vacancia_financeira, "QUANTIDADE_ATIVOS": quantidade_ativos}, ignore_index=True)
        
df.to_csv("fiis.csv", index=False)
