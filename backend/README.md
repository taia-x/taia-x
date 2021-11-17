# Provider

## Set up

run:
```
docker-compose up
```

This will spawn a FastAPI, an IPFS and a postgres container.

To see all routes supported by the api, open a browser and follow the link: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

## Testing

```
docker exec <CONTAINER_ID> pytest 
```

## Debugging

### VSCode

Make sure to set `DEBUG=true` in your `.env` file.

Go to the debugger tab in your vscode and click on the green button right from `Python: Remote Attach`