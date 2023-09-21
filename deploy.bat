@echo "delete all containers"
::docker stop horizon
::docker rm horizon

@echo "delete image"
docker rmi suppi147/horizon

@echo "rebuild image"
docker build --tag suppi147/horizon:latest .

@echo "run container"
::docker run -it -d -p 8000:8000 --name horizon --memory="1g" suppi147/horizon

@echo "push image"
docker push suppi147/horizon:latest