# Arquivo de processamento de dados, contendo as funções de preprocessamento de dados para o dataset ImageNet.
# O dataset ImageNet é um dataset de imagens de 1000 classes, com 1000 imagens por classe, totalizando 1 milhão de imagens. Mas 
# diferente dos outros datasets, nem todas imagens são de dimensões iguais, e nem todas imagens são coloridas. Por isso, é necessário
# um preprocessamento diferente para esse dataset.

import os
import random
from PIL import Image
import shutil

def sample_imagenet_data(root_dir, output_dir, n_samples=100000, split_ratios=(0.7, 0.2, 0.1), target_size=(256, 256)):
    """
    Amostra e organiza o dataset ImageNet.
    
    Parâmetros:
        root_dir (str): Diretório raiz do ImageNet
        output_dir (str): Diretório de saída para as amostras
        n_samples (int): Número total de imagens a serem amostradas
        split_ratios (tuple): Proporção de divisão para treino, validação e teste (deve somar 1.0)
        target_size (tuple): Resolução desejada das imagens
    """
    
    print("Iniciando o processamento das imagens...")
    
    # Verifica os proporções
    assert abs(sum(split_ratios) - 1.0) < 1e-10, "As proporções de treino, validação e teste devem somar 1.0"
    
    # Cria os diretórios de saída
    train_dir = os.path.join(output_dir, 'train/all_images')
    val_dir = os.path.join(output_dir, 'val/all_images')
    test_dir = os.path.join(output_dir, 'test/all_images')
    for dir in [train_dir, val_dir, test_dir]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    # Obtém a lista completa de imagens
    all_images = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('.JPEG', '.jpg', '.png')):
                all_images.append(os.path.join(subdir, file))
    
    print(f"Total de imagens encontradas: {len(all_images)}")
    
    # Amostra aleatoriamente n_samples imagens
    sampled_images = random.sample(all_images, n_samples)
    
    print(f"Total de imagens amostradas: {len(sampled_images)}")
    
    # Divide as imagens nos conjuntos de treino, validação e teste
    n_train = int(n_samples * split_ratios[0])
    n_val = int(n_samples * split_ratios[1])
    
    train_images = sampled_images[:n_train]
    val_images = sampled_images[n_train:n_train+n_val]
    test_images = sampled_images[n_train+n_val:]
    
    # Função auxiliar para redimensionar e salvar imagens
    def process_and_save(images, output_folder):
        for idx, img_path in enumerate(images, 1):
            img = Image.open(img_path)
            img = img.resize(target_size)
            img.save(os.path.join(output_folder, os.path.basename(img_path)))
            if idx % 1000 == 0:
                print(f"{idx} imagens processadas e salvas em {output_folder}")
    
    process_and_save(train_images, train_dir)
    print(f"Imagens de treino processadas e salvas em {train_dir}")
    
    process_and_save(val_images, val_dir)
    print(f"Imagens de validação processadas e salvas em {val_dir}")
    
    process_and_save(test_images, test_dir)
    print(f"Imagens de teste processadas e salvas em {test_dir}")

    print("Processamento concluído!")


path = r'E:\downloads\imagenet-object-localization-challenge\ILSVRC\Data\CLS-LOC\test'
output_path = r'C:\Users\mathe\Desktop\facul\database-tcc\ImageNet200k'

sample_imagenet_data(path, output_path, n_samples=200000)
