# Detecção de Sepse com Aprendizado de Máquina
<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="30" alt="docker logo"  />
  <img width="20" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="30" alt="fastapi logo"  />
  
</div>
Este projeto visa desenvolver um modelo de machine learning para prever a ocorrência de sepse em pacientes internados em Unidades de Terapia Intensiva (UTIs). Utilizamos técnicas de aprendizado de máquina supervisionado, especificamente classificação, para criar um modelo preditivo que discrimine entre pacientes com probabilidade de desenvolver sepse e aqueles que não têm, com base em um conjunto abrangente de características.

## Contexto
Sepse é uma condição médica grave que ocorre quando a resposta do corpo a uma infecção resulta em inflamação sistêmica e danos aos próprios tecidos e órgãos. É potencialmente fatal e pode ser desencadeada por fatores como idade avançada, sistemas imunológicos comprometidos (devido a condições como câncer ou diabetes), traumas graves e queimaduras. Este projeto não visa substituir ferramentas de diagnóstico, mas sim melhorar a detecção precoce e a intervenção para sepse, melhorando os resultados dos pacientes e reduzindo os custos de saúde.

## Objetivos

* Desenvolver um modelo de aprendizado de máquina para prever sepse.
* Criar uma API usando FastAPI para disponibilizar o modelo de ML.
* Implantar a aplicação em um contêiner Docker para facilitar a distribuição e escalabilidade.

## Estrutura do Projeto
Este projeto segue a estrutura do Processo Padrão Intersetorial para Mineração de Dados [(CRISP-DM)](https://www.datascience-pm.com/data-science-process/):

1. Compreensão do Negócio
2. Compreensão dos Dados
3. Preparação dos Dados
4. Modelagem
5. Avaliação
6. Implantação

## Hipóteses

> Hipótese Nula (H0): Não há relação significativa entre sepse e PRG (Plasma/Glicose).
> 
> Hipótese Alternativa (Ha): Existe uma relação significativa entre sepse e PRG (Plasma/Glicose).

## Descrição dos dados

Nome da Coluna |	Attribute/Target |	Descrição
------------|------------------|-----------
ID	        |N/A	             |Número exclusivo para representar o ID do paciente
PRG	        |Attribute1	       |Glicose plasmática
PL	        |Attribute 2	     |Resultado de exame de sangue-1 (mu U/ml)
PR	        |Attribute 3	     |Pressão Arterial (mm Hg)
SK	        |Attribute 4	     |Resultado de exame de sangue-2 (mm)
TS	        |Attribute 5	     |Resultado de exame de sangue-3 (mu U/ml)
M11         |	Attribute 6	     |Índice de massa corporal (peso em kg/(altura em m)^2
BD2	        |Attribute 7	     |Resultado de exame de sangue-4 (mu U/ml)
Age	        |Attribute 8	     |idade dos pacientes (anos)
Insurance	  |N/A	             |Se um paciente possuir um cartão de seguro válido
Sepssis	    |Alvo              |Positivo: se um paciente na UTI desenvolverá sepse, e Negativo: caso contrário

## Ferramentas e Tecnologias

Linguagem de Programação: Python ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)<br>
Modelagem de ML: Jupyter Notebook ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)<br>
Framework para API: FastAPI ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)<br>
Conteinerização: Docker ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)<br>

## Implementação
1. Desenvolvimento do Modelo de ML
O modelo foi treinado, avaliado e testado utilizando um conjunto de dados de características dos pacientes. O objetivo é prever a probabilidade de um paciente desenvolver sepse.

2. Criação da API com FastAPI
Para facilitar a utilização do modelo por desenvolvedores frontend, foi criada uma API Restful utilizando FastAPI. Esta API aceita solicitações HTTP e retorna respostas em um formato de dados padronizado (JSON).

3. Conteinerização com Docker
Para simplificar a implantação e garantir que o ambiente de execução seja consistente, a aplicação foi conteinerizada usando Docker.

# Uso
- Requisitos
> Docker instalado no sistema

## Passos para Executar
Clone este repositório:

bash
Copiar código
~~~
git clone https://github.com/seu-usuario/deteccao-sepse.git
cd deteccao-sepse
~~~
Construa a imagem Docker:

bash
Copiar código
~~~
docker build -t deteccao-sepse .
~~~
Execute o contêiner:

bash
Copiar código
~~~
docker run -p 8000:8000 deteccao-sepse
~~~

> Acesse a API em http://localhost:8000/docs para testar os endpoints e ver a documentação gerada automaticamente pelo FastAPI.

## Conclusão
Este projeto demonstra um fluxo de trabalho completo de machine learning, desde a modelagem até a implantação de uma API consumível e conteinerizada. Ele serve como um exemplo prático de como utilizar ferramentas modernas para criar soluções de machine learning escaláveis e acessíveis

## Autor:
Luiz Gustavo <br>
Conecte-se comigo no [Linkedin](https://www.linkedin.com/in/gustavoalmeidas/)
