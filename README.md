# Detecção de Sepse com Aprendizado de Máquina
Este projeto visa desenvolver um modelo de machine learning para prever a ocorrência de sepse em pacientes internados em Unidades de Terapia Intensiva (UTIs). Utilizamos técnicas de aprendizado de máquina supervisionado, especificamente classificação, para criar um modelo preditivo que discrimine entre pacientes com probabilidade de desenvolver sepse e aqueles que não têm, com base em um conjunto abrangente de características.

## Contexto
Sepse é uma condição médica grave que ocorre quando a resposta do corpo a uma infecção resulta em inflamação sistêmica e danos aos próprios tecidos e órgãos. É potencialmente fatal e pode ser desencadeada por fatores como idade avançada, sistemas imunológicos comprometidos (devido a condições como câncer ou diabetes), traumas graves e queimaduras. Este projeto não visa substituir ferramentas de diagnóstico, mas sim melhorar a detecção precoce e a intervenção para sepse, melhorando os resultados dos pacientes e reduzindo os custos de saúde.

## Objetivos
Desenvolver um modelo de aprendizado de máquina para prever sepse.
Criar uma API usando FastAPI para disponibilizar o modelo de ML.
Implantar a aplicação em um contêiner Docker para facilitar a distribuição e escalabilidade.

## Estrutura do Projeto
Este projeto segue a estrutura do Processo Padrão Intersetorial para Mineração de Dados [(CRISP-DM)](https://www.datascience-pm.com/data-science-process/):

1. Compreensão do Negócio
2. Compreensão dos Dados
3. Preparação dos Dados
4. Modelagem
5. Avaliação
6. Implantação

## Hipóteses
Hipótese Nula (H0): Não há relação significativa entre sepse e PRG (Plasma/Glicose).
Hipótese Alternativa (Ha): Existe uma relação significativa entre sepse e PRG (Plasma/Glicose).

## Descrição dos dados

Column Name |	Attribute/Target |	Descrição
------------|------------------|-----------
ID	        |N/A	             |Unique number to represent patient ID
PRG	        |Attribute1	       |Plasma glucose
PL	        |Attribute 2	     |Blood Work Result-1 (mu U/ml)
PR	        |Attribute 3	     |Blood Pressure (mm Hg)
SK	        |Attribute 4	     |Blood Work Result-2 (mm)
TS	        |Attribute 5	     |Blood Work Result-3 (mu U/ml)
M11         |	Attribute 6	     |Body mass index (weight in kg/(height in m)^2
BD2	        |Attribute 7	     |Blood Work Result-4 (mu U/ml)
Age	        |Attribute 8	     |patients age (years)
Insurance	  |N/A	             |If a patient holds a valid insurance card
Sepssis	    |Alvo              |Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise

## Ferramentas e Tecnologias
Linguagem de Programação: Python
Modelagem de ML: Jupyter Notebook (link para o notebook)
Framework para API: FastAPI
Conteinerização: Docker

## Implementação
1. Desenvolvimento do Modelo de ML
O modelo foi treinado, avaliado e testado utilizando um conjunto de dados de características dos pacientes. O objetivo é prever a probabilidade de um paciente desenvolver sepse.

2. Criação da API com FastAPI
Para facilitar a utilização do modelo por desenvolvedores frontend, foi criada uma API Restful utilizando FastAPI. Esta API aceita solicitações HTTP e retorna respostas em um formato de dados padronizado (JSON).

3. Conteinerização com Docker
Para simplificar a implantação e garantir que o ambiente de execução seja consistente, a aplicação foi conteinerizada usando Docker.

# Uso
Requisitos
Docker instalado no sistema

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
