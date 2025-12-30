from PIL import Image
import os


def aplicar_marca_dagua(pasta_img, logo_path, sufixo="_marca"):
    if not os.path.exists(pasta_img):
        raise FileNotFoundError("Pasta de imagens não encontrada.")

    if not os.path.exists(logo_path):
        raise FileNotFoundError("Logo não encontrada.")

    os.makedirs("output", exist_ok=True)

    logo = Image.open(logo_path).convert("RGBA")
    margem = 20
    contador = 0

    for nome_arquivo in os.listdir(pasta_img):
        if not nome_arquivo.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        caminho_base, extensao = os.path.splitext(nome_arquivo)
        img = Image.open(os.path.join(pasta_img, nome_arquivo)).convert("RGBA")

        posicao = (
            img.width - logo.width - margem,
            img.height - logo.height - margem
        )

        img.paste(logo, posicao, logo)

        if extensao.lower() in (".jpg", ".jpeg"):
            img = img.convert("RGB")

        nome_final = f"{caminho_base}{sufixo}{extensao}"
        img.save(os.path.join("output", nome_final))
        contador += 1

    return contador
