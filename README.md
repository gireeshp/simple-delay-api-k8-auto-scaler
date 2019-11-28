# simple-delay-api-k8-auto-scaler
These are two simple APIs which induces some delay for the given number of seconds either by sleep() or by doing some CPU intensive operation. We will deploy these API into Kubernetes and demonstrate how auto scaling works.
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
&nbsp;  
### Testing the auto-scaling

Use the <> to simulate the hits. Provide values as below.
URL - http://192.168.64.21/delay   
Total - 1000   
Parallel - 50   
&nbsp;  
Check current status before clicking "Start" button   
```
simple-delay-api$ kubectl get hpa
NAME        REFERENCE              TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
delay-api   Deployment/delay-api   0%/25%    1         10        1          17m
simple-delay-api$ kubectl get deploy
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
delay-api   1/1     1            1           17m
```

Check after a few minutes
```
simple-delay-api$ kubectl get hpa
NAME        REFERENCE              TARGETS    MINPODS   MAXPODS   REPLICAS   AGE
delay-api   Deployment/delay-api   201%/25%   1         10        10         20m
simple-delay-api$ kubectl get deploy
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
delay-api   10/10   10           10          20m
simple-delay-api$ kubectl get pods
NAME                        READY   STATUS    RESTARTS   AGE
delay-api-fb78b764b-4xlxl   1/1     Running   0          2m1s
delay-api-fb78b764b-86cf9   1/1     Running   0          2m1s
delay-api-fb78b764b-94s5q   1/1     Running   0          20m
delay-api-fb78b764b-dprgw   1/1     Running   0          2m16s
delay-api-fb78b764b-gqtg5   1/1     Running   0          2m16s
delay-api-fb78b764b-h695t   1/1     Running   0          2m1s
delay-api-fb78b764b-hbf4g   1/1     Running   0          106s
delay-api-fb78b764b-hpmpf   1/1     Running   0          2m1s
delay-api-fb78b764b-hwd7j   1/1     Running   0          106s
delay-api-fb78b764b-kzbs2   1/1     Running   0          2m16s
```
