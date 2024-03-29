# Containerization of simple web app

**Docker Compose** and **Kubernetes** in action.

Containerization of this simple web application created in Flask using two containers (api and app).

## Run in Docker

[Docker Compose overview – docs.docker.com](https://docs.docker.com/compose/)

1. Ensure that the value of the `api` variable in the `./app/app.py` file is `"http://app:5000/api/tasks"`. 
2. Build (or rebuild) the services (including images) described in `compose.yaml`.  

    `docker compose build`

3. Create and start the containers and services.

    `docker compose up`

4. Go to:

* **[localhost:5001](http://localhost:5001)** – APP
* [localhost:5000/api/tasks](http://localhost:5000/api/tasks) – API

## Run in Kubernetes

### Kubernetes in Docker Desktop

[Deploy on Kubernetes with Docker Desktop – docs.docker.com](https://docs.docker.com/desktop/kubernetes/)

1. Create or update resources in a Kubernetes cluster based on configuration files in ./kubernetes directory.

    `kubectl apply -f ./kubernetes`

2. Go to:

* **[localhost:5001](http://localhost:5001)** – APP
* [localhost:5000/api/tasks](http://localhost:5000/api/tasks) – API

### minikube

[minikube start – minikube.sigs.k8s.io](https://minikube.sigs.k8s.io/docs/start/)

1. Run Kubernetes cluster.

    `minikube start`

2. Connect to LoadBalancer services. It has to work all the time.

    `minikube tunnel`

3. Create or update resources in a Kubernetes cluster.

    `kubectl apply -f ./kubernetes`

4. Go to the addresses mentioned earlier.
