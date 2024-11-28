build:
	docker build -t my-dockerized-app .

run:
	docker run -p 5000:5000 my-dockerized-app

push:
	docker tag my-dockerized-app my-dockerhub-username/my-dockerized-app:latest
	docker push my-dockerhub-username/my-dockerized-app:latest
