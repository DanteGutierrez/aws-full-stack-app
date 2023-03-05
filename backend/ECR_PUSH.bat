aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 190369763426.dkr.ecr.us-west-1.amazonaws.com


docker compose up -d

@REM docker tag get-user:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:get-user
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:get-user

@REM docker tag post-user:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:post-user
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:post-user

@REM docker tag delete-user:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:delete-user
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:delete-user

@REM docker tag post-book:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:post-book
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:post-book

@REM docker tag get-book:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:get-book
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:get-book

@REM docker tag delete-book:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:delete-book
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:delete-book

@REM docker tag checkout:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:checkout
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:checkout

@REM docker tag put-book:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:put-book
@REM docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:put-book

docker tag post-login:1.0 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:post-login
docker push 190369763426.dkr.ecr.us-west-1.amazonaws.com/aws-book-store:post-login