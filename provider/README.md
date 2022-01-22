# Provider

## Set up

Install python dependencies:
```
pip install fastapi uvicorn SQLAlchemy psycopg2-binary alembic python-multipart
```
Download PostgreSQL and set-up a database (taiax): https://medium.com/@viviennediegoencarnacion/getting-started-with-postgresql-on-mac-e6a5f48ee399

Create and configure alembic.ini from alembic.ini.template and datapase.py according to your postgreSQL configurations

Run the migration to create tables:
```
alembic upgrade head
```

Run the server:
```
uvicorn main:app --reload
```


To see all routes supported by the api, open a browser and follow the link: [http://localhost:8000/docs](http://localhost:8000/docs)

## Testing

```
docker exec -ti <CONTAINER_ID> pytest 
```

## Debugging

### VSCode

Make sure to set `DEBUG=true` in your `.env` file.

Go to the debugger tab in your vscode and click on the green button right from `Python: Remote Attach`