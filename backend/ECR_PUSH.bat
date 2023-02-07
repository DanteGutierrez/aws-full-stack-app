aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 612894771267.dkr.ecr.us-west-2.amazonaws.com

docker compose up -d

docker tag get-user:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:get-user
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:get-user

docker tag post-user:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:post-user
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:post-user

docker tag update-user:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:update-user
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:update-user

docker tag delete-user:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:delete-user
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:delete-user

docker tag post-book:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:post-book
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:post-book

docker tag get-book:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:get-book
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:get-book

docker tag update-book:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:update-book
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:update-book

docker tag delete-book:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:delete-book
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:delete-book

docker tag checkout:1.0 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:checkout
docker push 612894771267.dkr.ecr.us-west-2.amazonaws.com/bookstore:checkout