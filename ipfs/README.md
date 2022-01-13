### CORS Error Fix

If you run into CORS errors, you have to set the corresponding headers `Access-Control-Allow-Origin` and `Access-Control-Allow-Methods` as follows:

1. Open a shell in the ipfs docker container with:

```bash
$ docker exec -it <container id> sh
```

2. Set the corresponding headers with:

```bash
$ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["*"]'
$ ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["PUT", "POST"]'
```

This allows every origin ("\*") to send HTTP PUT and POST messages to the IPFS API.

> This only takes effect after restarting the container! You can check if the headers are set properly if http://localhost:5001/webui shows: "Connected to IPFS"
