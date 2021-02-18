# Deployment instructions

1. Download the main branch as `DeepLift-Backend-main.zip` and copy to the home folder of the `ubuntu` user on the EC2 instance (It is okay if you overwrite the previous zip file that exists here).
   Example: `scp -i deeplift_key.pem DeepLift-Backend-main.zip ubuntu@server-address:~/DeepLift-Backend-main.zip`

2. SSH into the EC2 instance as the `ubuntu` user.
   Example: `ssh -i deeplift_key.pem ubuntu@server-address`

3. Switch to the root user and run `deploy.sh`
