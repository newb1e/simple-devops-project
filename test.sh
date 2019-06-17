echo "Hello 123"
docker build -t test1 https://github.com/newb1e/simple-devops-project.git
docker run --rm -p 80:80 --name "test1" test1
