# Projeto de conclusão de curso - Bacharelado em Ciência da Computação

## Qual o tema? Porque?

Em 2023.1, cursei a matéria "Introdução ao Aprendizado de Máquina" e me propus a realizar o trabalho final com o tema: "[Usando GAN's para geração automática de imagens de rostos humanos](https://github.com/MatheusOliveiraSilva/Intro.-Aprendizado-de-Maquina/blob/main/Trabalho%20Final%20-%20ML/relatorio%20final%20-%20introML.pdf)". No mesmo período, cursei as eletivas "Tópicos Especiais em Inteligência Computacional" e "Álgebra Linear Aplicada". Aprendi conceitos específicos que são a base para Deep Learning. Utilizei o trabalho mencionado acima como projeto final para essas três matérias. Como pude aproveitar o conhecimento de todas elas, dediquei-me com esmero e estudo aprofundado do tema. Ao final, desenvolvi uma paixão pela área de visão computacional. Acho fascinante como podemos ensinar o computador a entender a visão humana e, ainda mais impressionante, fazê-lo gerar imagens com contextos realistas.

Dito isso, escolhi um tema do campo da visão computacional chamado "Inpainting" (preenchimento de imagens). É uma técnica em que conseguimos preencher espaços faltantes de uma imagem de forma coerente e que siga uma semântica global. Para isso, podemos usar algoritmos antigos como o PatchMatch, que são adequados para imagens de fundo. Porém, para imagens não estacionárias, como rostos e outros elementos mais específicos onde existem mudanças bruscas de padrões e nuances que devem ser notadas, ele falha. Com o avanço do deep learning, tem-se discutido cada vez mais o uso de redes neurais para essa tarefa de inpainting. Esse é exatamente o foco do meu estudo: testar diferentes tipos de abordagens, do mais simples ao mais avançado.

## Estrutura do repositório

TO DO: EDITAR ESTE PARÁGRAFO CASO EU NÃO UTILIZE NADA ALÉM DO ENCODER-DECODER.

Na pasta `implementations`, estão os notebooks de implementação. Até o momento (16/09), criei uma subpasta chamada `encoder-decoder-approach`, onde postarei todas as versões baseadas nessa arquitetura. Estou inclinado a acreditar que ficarei apenas com o encoder/decoder, pois a U-NET parece ser uma boa candidata para abordar o problema de Inpainting, devido a diversas propriedades que detalharei no relatório técnico.

Na pasta `datasets`, armazenarei todos os conjuntos de dados que utilizarei. Até agora, a primeira versão do código utiliza apenas o CIFAR10, mas meu objetivo é trabalhar com imagens maiores que 32x32. Portanto, planejo experimentar datasets com imagens de 256x256 ou até mesmo 512x512.

O arquivo `requirements.txt` contém uma lista das bibliotecas instaladas no ambiente em que estou executando os códigos. Se você deseja executar o código em seu computador, siga as instruções fornecidas. Estou considerando que você utilize o Anaconda, que é bastante comum. No entanto, se estiver usando outro gerenciador de ambientes, pesquise os comandos equivalentes. Em resumo você deve:

    - Se não possuir algum ambiente, crie ele e em seguida entre nesse ambiente via terminal com os comandos:
    ``` 
    conda create --name novo_ambiente
    conda activate novo_ambiente
    ```
    - Use meu arquivo `requirements.txt` para instalar as bibliotecas usando:
    ```
    conda install --file requirements.txt
    ```

TO DO : Atualizar essa sessão de estrutura conforme eu for atualizando o repositório com mais coisas.

## Como testar meus códigos? 

Em geral, não implementei nada que requeira uma pipeline específica para execução. Basta acessar a pasta `implementations`, escolher um notebook e executá-lo. No entanto, esteja ciente de que pode ser necessário ajustar os caminhos (paths), pois estão configurados conforme a organização em meu computador. Se você estiver usando uma distribuição específica, pode haver diferenças na execução.