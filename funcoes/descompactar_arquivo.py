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
    print('arquivo movido')
    # remove arquivo .zip baixado
    os.remove(arquivo)
    print('pasta zip deletada')

    # move arquivo para a pasta de histórico
    arquivo_pasta_destino = glob.glob('C:/Users/A0170053/OneDrive - Telefonica/Projetos/RPA/RPA_RelatorioParceiroInfoB2B/RelatorioInfoB2B_TimeParceiro_*.csv')
    caminho_arquivo = arquivo_pasta_destino[0]
    shutil.copy(caminho_arquivo, r'C:\Users\A0170053\OneDrive - Telefonica\Projetos')
    print('arquivo copiado')

    # renomeia o excel com um nome padrão para poder rodar no integration
    arquivo_renomeado = glob.glob('C:/Users/A0170053/OneDrive - Telefonica/Projetos/RPA/RPA_RelatorioParceiroInfoB2B/RelatorioInfoB2B_TimeParceiro_*.csv')
    arquivo_renomeado2 = arquivo_renomeado[0]
    renomear = os.path.join('C:/Users/A0170053/OneDrive - Telefonica/Projetos/RPA/RPA_RelatorioParceiroInfoB2B', 'RelatorioInfoB2B_TimeParceiro.csv')
    print(renomear)
    os.rename(arquivo_renomeado2, renomear)
    print('arquivo renomeado para o nome padrão')


















