

# Repositorio MP3/Player de Música

## Deploy com Docker Compose
```
cd docker
docker-compose build
docker-compose up -d
```

## Deploy com Python e Node

### Frontend

#### Para rodar
- Entrar na pasta `front` e executar

```
cd front
npm install
npm start
```

### Backend
- Versão do Python `3.7`
- Com Gerenciador de dependencias `PIPENV`

#### Para instalar
- Entrar na pasta `api`

```
cd api
pipenv install
```

#### Para rodar 

```
pipenv shell
python main.py
```

### Documentação da `API` em http://localhost:5000
### Acesso ao `frontend` em http://localhost:9090

