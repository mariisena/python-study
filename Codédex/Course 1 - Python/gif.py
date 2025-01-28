import imageio.v2 as imageio
from PIL import Image

# Função para criar uma transição suave entre duas imagens
def create_medium_fade(image1, image2, alpha):
    return Image.blend(image1, image2, alpha)

# Lista de arquivos de imagens
imagens = [
    "C:/Users/marii/OneDrive/Área de Trabalho/CC/Linguagens de Programação/Python-study/Codédex/Course 1 - Python/Naruto1.png", 
    "C:/Users/marii/OneDrive/Área de Trabalho/CC/Linguagens de Programação/Python-study/Codédex/Course 1 - Python/Naruto2.png", 
    "C:/Users/marii/OneDrive/Área de Trabalho/CC/Linguagens de Programação/Python-study/Codédex/Course 1 - Python/Naruto3.png"
]

# Nome do arquivo GIF que será gerado
nome_gif = "naruto_medium_fade.gif"

# Carregar as imagens com PIL
imagens_pil = [Image.open(imagem) for imagem in imagens]

# Redimensionar as imagens para o tamanho da primeira imagem
tamanho = imagens_pil[0].size
imagens_pil = [imagem.resize(tamanho) for imagem in imagens_pil]

# Lista para armazenar os quadros do GIF
frames = []

# Criar a transição entre as imagens
# Mistura imagem 1 com imagem 2
for alpha in range(1, 11):  # Ajuste para 10 passos intermediários
    fade_frame = create_medium_fade(imagens_pil[0], imagens_pil[1], alpha / 10)
    frames.append(fade_frame)

# Adicionar a imagem 2
frames.append(imagens_pil[1])

# Mistura imagem 2 com imagem 3
for alpha in range(1, 11):  # Ajuste para 10 passos intermediários
    fade_frame = create_medium_fade(imagens_pil[1], imagens_pil[2], alpha / 10)
    frames.append(fade_frame)

# Criar o GIF com os quadros
with imageio.get_writer(nome_gif, mode="I", duration=0.5, loop=2) as writer:
    for frame in frames:
        writer.append_data(frame)

print(f"GIF criado com sucesso: {nome_gif}")
