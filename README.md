# Restaurant Web Application

Welcome to the Django Restaurant Web Application! This project is designed to provide a seamless experience for managing a restaurant's operations.

## Features

- User Authentication
- User Profile
- Reservation System
- Menu Display
- Order Placement
- Responsive Design

## Prerequisites

- Docker
- Kubernetes
- kubectl
- Minikube (for local Kubernetes deployment)

## Setup Instructions

### 1. Initialize a Git Repository

```sh
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/AhMeD7493/restaurant-app.git
git push -u origin master

### 2. Configure Environment Variables

Create a .env file in the project root with the following content:

DB_NAME=restaurantdb
DB_USER=admin
DB_HOST=postgres-service 
DB_PASS=admin-password
DB_PORT=5432
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,192.168.49.2,192.168.49.2:30000


### 3. Build and Run with Docker 

Ensure Docker is running, then execute:

docker build -t my-rest-app .


### 4. Access the Application

Visit http://localhost:8000 in your web browser.

### 5. Deploy with Kubernetes

Apply the Kubernetes manifests with the order:

kubectl apply -f postgres-pv.yml
kubectl apply -f postgres-pvc.yml
kubectl apply -f postgres-credentials.yml
kubectl apply -f configmap.yml
kubectl apply -f postgres-deployment.yml
kubectl apply -f postgres-service.yml
kubectl apply -f app-deployment.yml
kubectl apply -f app-service.yml

Forward the service port to your local machine:

kubectl port-forward service/django-service 8000:8000

Or Using NodePort

http://minikube-ip:30000
