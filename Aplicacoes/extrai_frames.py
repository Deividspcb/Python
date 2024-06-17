import cv2
import os

def frames_de_videos_em_pasta(entrada_pasta, saida_pasta):
    total_frames_baixados = 0  # Inicializa a contagem total de frames

    # Lista todos os arquivos na pasta de entrada
    arquivos = os.listdir(entrada_pasta)

    for arquivo in arquivos:
        # Verifica se o arquivo é um vídeo com extensão .mp4
        if arquivo.endswith(".mp4"):
            entrada = os.path.join(entrada_pasta, arquivo)
            saida_subpasta = os.path.join(saida_pasta, os.path.splitext(arquivo)[0])

            # Cria a subpasta de saída para cada vídeo
            os.makedirs(saida_subpasta, exist_ok=True)

            # Chama a função para extrair os frames e atualiza a contagem total
            total_frames_baixados += frames_de_video(entrada, saida_subpasta)

    print(f'Total de frames baixados: {total_frames_baixados}')

def frames_de_video(entrada, caminho_saida):
    entrada_capturada = cv2.VideoCapture(entrada)
    cont = 0
    while entrada_capturada.isOpened():
        retorno, frame = entrada_capturada.read()

        if retorno:
            cv2.imwrite(os.path.join(caminho_saida, f'{cont:04d}.jpg'), frame)
            cont += 1
        else:
            break

    cv2.destroyAllWindows()
    entrada_capturada.release()

    return cont  # Retorna a contagem de frames para cada vídeo

# Diretório de entrada contendo os vídeos
input_directory = r"Video para extrair"

# Diretório de saída para os frames
output_directory = r"Pasta onde serão salvos os frames"

# Chama a função para extrair os frames de todos os vídeos na pasta de entrada
frames_de_videos_em_pasta(input_directory, output_directory)
