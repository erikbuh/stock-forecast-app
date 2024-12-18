# stock-forecast-app
Test app for FastAPI + Streamlit integration and Azure container deployment

## Local App

Build and run the FastAPI and Streamlit containers with:
`docker-compose up --build`

Then the app is locally accessible via: `http://localhost:8501/`

Once stopped, remove containers, networks, etc. via: 
`docker-compose down`

___

## Azure App

### Deploying the backend (FastAPI)

From the `/backend` folder:

For Azure build in the containers in their respective folders with `docker build --platform linux/amd64 -t backendfastapi .`

Run them via: `docker run -p 8000:8000 backendfastapi`

Tag them via: `docker tag backendfastapi stockforecastacr.azurecr.io/stock-forecast-backend:latest` (asigns a new name to an existing docker image)

(show available docker images on local machine with `docker images`)

Here `stockforecastacr.azurecr.io` is the Azure Container Registry (ACR) URL.

Push the tagged docker image to the ACR: `docker push stockforecastacr.azurecr.io/stock-forecast-backend:latest` 
(One needs to be logged into the right ACR: `az acr login --name stockforecastacr`)

### Deploying the frontend (Streamlit)

From the `/frontend` folder:

Build container: `docker build --platform linux/amd64 -t frontendstreamlit .`

Tag: `docker tag frontendstreamlit stockforecastacr.azurecr.io/stock-forecast-frontend:latest`

Push: `docker push stockforecastacr.azurecr.io/stock-forecast-frontend:latest`
