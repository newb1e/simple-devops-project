echo "Hello 1"
docker build -t test1 https://github.com/newb1e/simple-devops-project.git
docker run --rm -ti -p 80:80 --name "test1" test1
