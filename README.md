# simple-delay-api
These are two simple APIs which induces some delay for the given number of seconds either by sleep() or by doing some CPU intensive operation
&nbsp;  
&nbsp;  
### Setup
```
pip install -r requirements.txt
```

### Run locally
```
python api.py
```

### Docker build & run
```
docker build -t delay-api:1.0 .
docker run -d -p 8081:8081 delay-api:1.0
```
OR simply pull from docker hub & run.
```
docker run -d -p 8081:8081 gireeshp/delay-api:1.0
```
&nbsp;  
## Access the application URL
Hit either of following API with URL parameter 'seconds' - which is the wait you need in number of seconds. If the argument is skipped, default wait will be 10 seconds  
http://127.0.0.1:8081/delay?seconds=3  
(this induces a CPU intensive wait of 3 seconds)  
OR  
http://127.0.0.1:8081/sleep?seconds=3  
(this induces a simple 3 seconds delay by sleeping)  

&nbsp;  
&nbsp;  
# Deploying to Kubernetes
This section explains how this application can be deployed to Kubernetes. Using minikube here (see [setting up minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/)). We are going to create the Deployment, Service, Ingress & a Horizontal Auto Scaler.
&nbsp;  

### Start minikube
```
simple-delay-api$ minikube start
simple-delay-api$ minikube addons enable heapster
simple-delay-api$ minikube addons enable metrics-server
simple-delay-api$ kubectl apply -f k8.yaml 

ingress.networking.k8s.io/delay-api created
service/delay-api created
deployment.apps/delay-api created
horizontalpodautoscaler.autoscaling/delay-api created
```
&nbsp;  

Check the ingress IP.
```
simple-delay-api$ kubectl get ingress
NAME        HOSTS   ADDRESS         PORTS   AGE
delay-api   *       192.168.64.21   80      2m25s
```

Now we can access the API over browser using URLs
http://192.168.64.21/delay
OR
http://192.168.64.21/sleep