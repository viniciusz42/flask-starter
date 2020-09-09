## Flask Starter

Executar servidor desenvolvimento

```bash
pipenv install
pipenv shell
invoke dev
```

Executar testes

```bash
invoke test
```

Executar docker compose

```bash
docker-compose build
docker-compose up -d
```

Executar docker manual

```bash
docker build -t server .
docker run -d -p 5000:5000 --name server-container server
```

Documentação Swagger

`http://127.0.0.1:5000`





