# Flask-MongoDB-Kubernetes Application

This project demonstrates the deployment of a containerized Python Flask application with MongoDB on a Kubernetes cluster. The application supports CRUD (Create, Read, Update, Delete) operations through RESTful API endpoints.

---

## Features
- CRUD operations with MongoDB
- RESTful Flask API
- Containerized with Docker
- Deployed on Kubernetes with StatefulSet, Deployments, and Services
- Service discovery between Python Flask app and MongoDB

---

## Prerequisites
Before starting, ensure you have the following installed:
- Python 3.x
- Docker
- Kubernetes (Minikube/Docker Desktop or a Kubernetes cluster)
- `kubectl` command-line tool
- MongoDB

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo-name/flask-mongodb-kubernetes.git
cd flask-mongodb-kubernetes
```

### Step 2: Build and Push Docker Image
1. Build the Docker image:
    ```bash
    docker build -t <your-dockerhub-username>/flask-mongodb-app:latest .
    ```
2. Push the image to Docker Hub:
    ```bash
    docker push <your-dockerhub-username>/flask-mongodb-app:latest
    ```

---

## Deployment Steps

### Step 1: Deploy MongoDB on Kubernetes
1. Apply the StatefulSet for MongoDB:
    ```bash
    kubectl apply -f mongodb-statefulset.yaml
    ```
2. Expose MongoDB with a Service:
    ```bash
    kubectl apply -f mongodb-service.yaml
    ```

### Step 2: Deploy Flask Application on Kubernetes
1. Apply the Deployment for the Flask app:
    ```bash
    kubectl apply -f python-app-deployment.yaml
    ```
2. Expose the Flask app with a Service:
    ```bash
    kubectl apply -f python-app-service.yaml
    ```

---

## Endpoints
The Flask application exposes the following endpoints:

| Method | Endpoint   | Description                         |
|--------|------------|-------------------------------------|
| POST   | `/create`  | Create a new record in MongoDB      |
| GET    | `/read`    | Read all records from MongoDB       |
| PUT    | `/update`  | Update a record in MongoDB          |
| DELETE | `/delete`  | Delete a record from MongoDB        |

### Example: `curl` Commands
1. **Create a Record**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title": "My Book", "author": "John Doe"}' http://<service-ip>:<port>/create
    ```
2. **Read Records**
    ```bash
    curl -X GET http://<service-ip>:<port>/read
    ```
3. **Update a Record**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"query": {"title": "My Book"}, "update": {"author": "Jane Doe"}}' http://<service-ip>:<port>/update
    ```
4. **Delete a Record**
    ```bash
    curl -X DELETE -H "Content-Type: application/json" -d '{"title": "My Book"}' http://<service-ip>:<port>/delete
    ```

---

## Testing the Application
1. Test the Flask API using tools like `curl`, Postman, or a web browser.
2. Verify the Flask app connects to MongoDB and performs CRUD operations successfully.

---

## Project Files
- `app.py`: Python Flask application.
- `Dockerfile`: Docker configuration for containerizing the Flask app.
- `requirements.txt`: Python dependencies.
- `mongodb-statefulset.yaml`: Kubernetes StatefulSet for MongoDB.
- `mongodb-service.yaml`: Kubernetes Service for MongoDB.
- `python-app-deployment.yaml`: Kubernetes Deployment for the Flask app.
- `python-app-service.yaml`: Kubernetes Service for the Flask app.

---

## Troubleshooting
1. **Cannot Connect to MongoDB**:
   - Ensure the `mongodb-service` name is used in the Flask app connection string.
   - Check the MongoDB pod logs:
     ```bash
     kubectl logs <mongodb-pod-name>
     ```

2. **Flask App Errors**:
   - Check Flask pod logs:
     ```bash
     kubectl logs <flask-app-pod-name>
     ```

3. **Service Not Accessible**:
   - Ensure the services are running:
     ```bash
     kubectl get svc
     ```

---

## Acknowledgments
This project is part of the AIN-3003 course assignment at Bahçeşehir University.
