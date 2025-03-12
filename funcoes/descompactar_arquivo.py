import os
import zipfile
import glob
import re
import shutil

# função de descompacta o relatório que foi baixado no info b2b
def descompactar_arquivo():
    # encontra o arquivo e armazena ele em uma variável
    encontrar_arquivo = glob.glob('C:/Users/A0170053/Downloads/RelatorioInfoB2B_TimeParceiro_*.zip')
    arquivo = encontrar_arquivo[0]

    pasta_destino = 'C:/Users/A0170053/Downloads'
    # descompacta arquivo e envia para uma pasta de destino
    with zipfile.ZipFile(arquivo, 'r') as zipf:
        zipf.extractall(pasta_destino)
    # encontra o arquivo .csv que foi extraido
    arquivo_extraido = glob.glob('C:/Users/A0170053/Downloads/RelatorioInfoB2B_TimeParceiro_*.csv')
    excel = arquivo_extraido[0]
    # alterar o nome e retirar os ultimos caracteres
    novo_nome = os.path.join(pasta_destino, re.sub(r'(_\d{6})\.csv$', '.csv', os.path.basename(excel)))
    os.rename(excel, novo_nome)
    # mover o csv para a nova pasta
    arquivo_destino = 'C:/Users/A0170053/OneDrive - Telefonica/Projetos/RPA/RPA_RelatorioParceiroInfoB2B'
    shutil.move(novo_nome, arquivo_destino)




















