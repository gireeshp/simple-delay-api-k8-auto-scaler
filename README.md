# simple-delay-api
This is just a simple API to test K8 auto scaling project

docker build -t delay-api:1.0 .
docker run -d -p 5000:5000 delay-api:1.0

# Minikube start/stop/delete/dashboard
minikube start
minikube dashboard
minikube stop
minikube delete

# Use local images (didn't work)
minikube docker-env
eval $(minikube docker-env)

# Create deployments/services using commands
kubectl create deployment delay-api --image gireeshp/delay-api:1.1
kubectl expose deployment delay-api --type=NodePort --port=8081
kubectl get pod
minikube service delay-api --url
kubectl delete services delay-api
kubectl delete deployment delay-api
https://kubernetes.io/docs/setup/learning-environment/minikube/

# Create deployments/services using YAML
kubectl create -f deployment.yaml
kubectl create -f service.yaml   --Didn't work
kubectl expose deployment delay-api-dep --type=NodePort --port=8081
kubectl autoscale deployment delay-api-dep --cpu-percent=20 --min=1 --max=5

kubectl delete hpa delay-api-dep
https://www.mirantis.com/blog/introduction-to-yaml-creating-a-kubernetes-deployment/



http://alesnosek.com/blog/2017/02/14/accessing-kubernetes-pods-from-outside-of-the-cluster/
