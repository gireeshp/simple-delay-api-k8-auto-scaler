# simple-delay-api
These are two simple APIs which induces some delay for the given number of seconds either by sleep() or by doing some CPU intensive operation

## Setup
```
pip install -r requirements.txt
```

## Run locally
```
python api.py
```

## Docker build & run
```
docker build -t delay-api:1.0 .
docker run -d -p 8081:8081 delay-api:1.0
```
OR simply pull from docker hub & run.
```
docker pull gireeshp/delay-api:1.0
```



## Run
Hit either of following API with URL parameter 'seconds' - which is the wait you need in number of seconds. If the argument is skipped, default wait will be 10 seconds  
http://127.0.0.1:8081/delay?seconds=3  
(this induces a CPU intensive wait of 3 seconds)  
OR  
http://127.0.0.1:8081/sleep?seconds=3  
(this induces a simple 3 seconds delay by sleeping)  

## Deploy into Kubernetes (using minikube here)
```
minikube start
kubectl create -f deployment.yaml
kubectl create -f service.yaml
```



# Create deployments/services using commands
kubectl create deployment delay-api --image gireeshp/delay-api:1.1
kubectl expose deployment delay-api --type=NodePort --port=8081
kubectl get pod
minikube service delay-api --url
kubectl delete services delay-api
kubectl delete deployment delay-api
https://kubernetes.io/docs/setup/learning-environment/minikube/

# Create deployments/services using YAML
kubectl create -f service.yaml   --Didn't work
kubectl expose deployment delay-api-dep --type=NodePort --port=8081
kubectl autoscale deployment delay-api-dep --cpu-percent=20 --min=1 --max=5

kubectl delete hpa delay-api-dep
https://www.mirantis.com/blog/introduction-to-yaml-creating-a-kubernetes-deployment/



http://alesnosek.com/blog/2017/02/14/accessing-kubernetes-pods-from-outside-of-the-cluster/
