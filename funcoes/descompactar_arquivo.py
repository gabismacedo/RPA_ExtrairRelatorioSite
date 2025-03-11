import os
import zipfile
import glob
import re
import shutil

def descompactar_arquivo():
    encontrar_arquivo = glob.glob('C:/Users/A0170053/Downloads/RelatorioInfoB2B_TimeParceiro_*.zip')
    print(encontrar_arquivo)

    arquivo = encontrar_arquivo[0]
    print(arquivo)
    pasta_destino = 'C:/Users/A0170053/Downloads'

    with zipfile.ZipFile(arquivo, 'r') as zipf:
        zipf.extractall(pasta_destino)

    arquivo_extraido = glob.glob('C:/Users/A0170053/Downloads/RelatorioInfoB2B_TimeParceiro_*.csv')
    excel = arquivo_extraido[0]
    print(excel)

    novo_nome = os.path.join(pasta_destino, re.sub(r'(_\d{6})\.csv$', '.csv', os.path.basename(excel)))
    os.rename(excel, novo_nome)
    print(novo_nome)

    arquivo_destino = 'C:/Users/A0170053/OneDrive - Telefonica/Projetos/RPA/RPA_RelatorioParceiroInfoB2B'

    shutil.move(novo_nome, arquivo_destino)




















