# Use uma imagem oficial do Python como imagem base
FROM python:3.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o conteúdo do diretório atual para o contêiner em /app
COPY . /app

# Copie a pasta toolkit para o contêiner
COPY toolkit /app/toolkit

# Instale os pacotes especificados no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Faça a porta 800 disponível para o mundo fora do contêiner
EXPOSE 800

# Execute o app.py quando o contêiner iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "800"]