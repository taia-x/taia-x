# Provider

## Set up

run:
```
docker-compose up
```

This will spawn a FastAPI and a postgres container.

To see all routes supported by the api, open a browser and follow the link: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

## Testing

```
docker exec -ti <CONTAINER_ID> pytest 
```

## Debugging
```
Error: standard_init_linux.go:228: exec user process caused: no such file or directory
```
If the docker-compose command is being executed on a Windows system, change the "End of Line Sequence" from the docker-start.sh script to LF, if it was previously saved as CRLF. 

### VSCode

Make sure to set `DEBUG=true` in your `.env` file.

Go to the debugger tab in your vscode and click on the green button right from `Python: Remote Attach`
