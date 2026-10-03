We welcome contributions! To ensure a smooth collaboration, please follow these guidelines:

**Contributing to Needpedia**
- Fork the repo
- create a branch in your fork
- commit your code in branch
- Submit a PR in the main repo
- Your code would be reviewed by then would be deployed on staging server for testing, and if everything was fine it should be deployed on production server

**Docker Setup Steps:**
1. Follow this link to install docker https://docs.docker.com/engine/install/ubuntu/
2. Follow this link to install docker compose https://docs.docker.com/compose/install/
3. Stop your local running postgresql service by command `sudo service postgresql stop`
4. Go to project directory and run command `sudo docker-compose build` (NOTE: Its only for first time)
5. After successfully build run command `sudo docker-compose up`
 You project will be running on `localhost:3000`
