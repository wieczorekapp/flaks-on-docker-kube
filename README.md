# flask-on-docker-kube
Simple web application Flask + SQLAlchemy + Gunicorn + PostgreSQL + Nginx running on Docker(docker-compose) and local Kubernetes cluster.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
You must have installed:
- Docker
- minikube
- git
- kompose(optional to convert docker-compose to Kubernetes)

### Installing
```
git clone https://github.com/wieczorekapp/flaks-on-docker-kube
```

```
cd flaks-on-docker-kube
```
Rename env files, remove _ in filenames.

```
docker compose -f docker-compose.prod.yml up -d --build
```

```
docker compose -f docker-compose.prod.yml exec web python manage.py create_db
```

Application works on localhost on port 1337.
It has two endpoints:
/
/history


Kubernetes
```
minikube start
```

```
kubectl apply -f .
```

To check ip addres
```
kubectl describe svc nginx
```

Optional to convert docker-compose to Kubernetes

```
kompose -f docker-compose.prod convert
```

### Possible improvements in the future
- a better way to limit the number of requests(ngnix configuration to improve)
- refactor flask code to separate model, controller and different views(now it's only fast prototype)
- adding error handling(logging them to the database)
- improve Kubernets configuration, learning about good practices and getting to know Kubernetes
