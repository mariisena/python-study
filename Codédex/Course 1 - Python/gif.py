import imageio.v3 as iio

# Lista de arquivos de imagens (substitua pelos nomes das suas imagens)
imagens = ["imagem1.png", "imagem2.png", "imagem3.png"]

# Nome do arquivo GIF que será gerado
nome_gif = "meu_gif.gif"

# Criando o GIF
with imageio.get_writer(nome_gif, mode="I", duration=0.5) as writer:
    for imagem in imagens:
        frame = imageio.imread(imagem)
        writer.append_data(frame)

print(f"GIF criado com sucesso: {nome_gif}")
