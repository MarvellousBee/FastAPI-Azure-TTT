# FastAPI-Azure-TTT
 Online Tic-Tac-toe.
 
![](media/image1.png)  


## Local Deployment
1.  Navigate your terminal to project's directory,
2.  deploy FastAPI with `uvicorn server:app`,
4.  open 2 clients (use `python client.py`) on your network,
5.  follow instructions in the chat box.

## Online Deployment
1.  Navigate your terminal to project's directory,
2.  deploy FastAPI on Azure as an App serive,
3.  run with `gunicorn -w 4 -k uvicorn.workers.UvicornWorker server:app`,
4.  Change line 10 of `client.py` to match server's IP
5.  open 2 clients (use `python client.py`) on your network,
6.  follow instructions in the chat box.

