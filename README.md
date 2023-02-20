# flaks-on-docker-kube
Simple web application flask + SQLAlchemy + Gunicorn + PostgreSQL + Nginx running on Docker(docker-compose) and local Kubernetes cluster.

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

Optional
To convert docker-compose to Kubernetes

```
cd docker_compose
```

```
kompose -f docker-compose.prod convert
```
