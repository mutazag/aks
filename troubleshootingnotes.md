## no public IP in the output

inspecting the output of `kubectl get service` shows no public IP address for the service.


command output is:

```bash
PS C:\git\aks> kubectl get service
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.0.0.1     <none>        443/TCP   47h
```

To add a public IP address to the service, run the following command:

```bash
PS C:\git\aks> kubectl expose deployment aks-helloworld --type=LoadBalancer --name=aks-helloworld --port=80 --target-port=80
```

## inspecting azureml services

run the commend below to get the list of services

```bash
kubectl get services -n azureml
```


or to list some service, a dummy endpoint service for example:

```bash
kubectl get services -n azureml dummymodel-4-dummep2
```

this is showing no externall IP address, which means that the service is not exposed to the internet.


# review azureml extension components



```
kubectl get deployments -n azureml
```

# deploy aks-store-app sample app

https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-app


command to deploy app:
```kubectl apply -f aks-store-quickstart.yaml```


monitor the app deployment: ```kubectl get service store-front --watch```

here you will notice an external ip address is assigned to the service.