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
This section explains how this imple delay application can be deployed to Kubernetes. Using minikube here (see [setting up minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/))
&nbsp;  

### Start minikube
```
(base) Gireeshs-MacBook-Pro:~ gireesh$ minikube start
😄  minikube v1.5.0 on Darwin 10.14.6
✨  Automatically selected the 'hyperkit' driver
🔥  Creating hyperkit VM (CPUs=2, Memory=2000MB, Disk=20000MB) ...
🐳  Preparing Kubernetes v1.16.2 on Docker 18.09.9 ...
🚜  Pulling images ...
🚀  Launching Kubernetes ... 
⌛  Waiting for: apiserver proxy etcd scheduler controller dns
🏄  Done! kubectl is now configured to use "minikube"
```
Start the dashboard too, so that we can verify the components.
```
(base) Gireeshs-MacBook-Pro:simple-delay-api gireesh$ minikube dashboard
🤔  Verifying dashboard health ...
🚀  Launching proxy ...
🤔  Verifying proxy health ...
🎉  Opening http://127.0.0.1:52788/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
```


&nbsp;  
### Create Deployment
```
(base) Gireeshs-MacBook-Pro:simple-delay-api gireesh$ kubectl create -f deployment.yaml
deployment.apps/delay-api-dep created
```

We can see the deployment in the minikube dashboard.
<img width="1239" alt="MinikubeDB-delay-api-deployment" src="https://user-images.githubusercontent.com/4717349/68527039-8f7a4c80-0308-11ea-84d3-d529de5e7f7b.png">

Use below command to find the POD IPs
```
kubectl get pods -l app=delay-api-dep -o yaml | grep podIP
    podIP: 172.17.0.6
    podIPs:
    podIP: 172.17.0.7
    podIPs:
```

Now we can access the application in POD from any Kubernetes Nodes. For minikube, use "minikube ssh" command to get into the Node and use curl to try out the application:
```
(base) Gireeshs-MacBook-Pro:~ gireesh$ minikube ssh
                         _             _            
            _         _ ( )           ( )           
  ___ ___  (_)  ___  (_)| |/')  _   _ | |_      __  
/' _ ` _ `\| |/' _ `\| || , <  ( ) ( )| '_`\  /'__`\
| ( ) ( ) || || ( ) || || |\`\ | (_) || |_) )(  ___/
(_) (_) (_)(_)(_) (_)(_)(_) (_)`\___/'(_,__/'`\____)

$ curl 172.17.0.6:8081/delay?seconds=3
Successful$ 
$ 
```

### Create Service
Now let's create a service
```
kubectl create -f service.yaml
service/delay-api-service created
```
