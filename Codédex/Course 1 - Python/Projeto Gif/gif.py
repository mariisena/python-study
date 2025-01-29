import imageio.v2 as imageio
from PIL import Image
import os

# Verificar o diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))  # Diretório onde o script está localizado
print("Diretório de trabalho atual:", diretorio_atual)

# Função para criar uma transição suave entre duas imagens
def create_medium_fade(image1, image2, alpha):
    return Image.blend(image1, image2, alpha)

# Lista de arquivos de imagens
imagens = [
    "Naruto1.png", 
    "Naruto2.png", 
    "Naruto3.png"
]

# Caminho completo para o GIF de saída
nome_gif = os.path.join(diretorio_atual, "naruto_medium_fade.gif")

# Carregar as imagens com PIL
try:
    imagens_pil = [Image.open(os.path.join(diretorio_atual, imagem)) for imagem in imagens]
except FileNotFoundError as e:
    print(f"Erro ao abrir imagem: {e}")
    exit()  # Interrompe o script se houver erro ao carregar as imagens

# Redimensionar as imagens para o tamanho da primeira imagem
tamanho = imagens_pil[0].size
imagens_pil = [imagem.resize(tamanho) for imagem in imagens_pil]

# Lista para armazenar os quadros do GIF
frames = []

# Criar a transição entre as imagens
for alpha in range(1, 11):  # Mistura imagem 1 com imagem 2
    fade_frame = create_medium_fade(imagens_pil[0], imagens_pil[1], alpha / 10)
    frames.append(fade_frame)

frames.append(imagens_pil[1])  # Adicionar a imagem 2

for alpha in range(1, 11):  # Mistura imagem 2 com imagem 3
    fade_frame = create_medium_fade(imagens_pil[1], imagens_pil[2], alpha / 10)
    frames.append(fade_frame)

# Criar o GIF com os quadros
try:
    with imageio.get_writer(nome_gif, mode="I", duration=0.5, loop=2) as writer:
        for frame in frames:
            writer.append_data(frame)
    print(f"GIF criado com sucesso: {nome_gif}")
except Exception as e:
    print(f"Erro ao criar o GIF: {e}")