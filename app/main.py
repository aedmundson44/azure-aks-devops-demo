from fastapi import FastAPI
import socket

# creates your application object; everything attaches to this "app"
app = FastAPI()

@app.get("/")
def root():
    # decorator: registers the function below to handle GET requests at the "/" URL
    # the function that runs when someone visits "/"
    #return a dict with keys "app" and "version"
    return {"app": "aks-demo", "version": "1.0"}

@app.get("/health")
def health():
    # registers this function for GET requests at "/health"
    # Kubernetes will ping this to check your app is alive
    #return a dict with key "status" and value "ok"
    return {"status": "ok"}

@app.get("/info")
def info():
    # registers this function for GET requests at "/info"
    # shows which machine/pod is serving the request
    #return a dict with the hostname — use socket.gethostname()
    return {"hostname": socket.gethostname()}