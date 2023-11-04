# miax11devops

Para hacerlo manual:


1. Create the repossitorio en ECR con comandos o desde la UI que es esto
aws ecr create-repository --repository-name lambdamiax11 --region eu-west-3

2. Build the image
docker build -t 351061903689.dkr.ecr.eu-west-3.amazonaws.com/lambdamiax11 .

3. To test:
docker run  -p 8080:8080 351061903689.dkr.ecr.eu-west-3.amazonaws.com/lambdamiax11

4. Log docker into the aws registry (only 1 time)
aws ecr get-login-password | docker login --username AWS --password-stdin 351061903689.dkr.ecr.eu-west-3.amazonaws.com/lambdamiax11

5. Push the image
docker push 351061903689.dkr.ecr.eu-west-3.amazonaws.com/lambdamiax11