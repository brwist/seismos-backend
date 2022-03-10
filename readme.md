###Server Setup with Docker
- clone the repository of the seismos_backend_api
- create .env file in the root directory of the repository folder
- write the all the environment variable.
- docker-compse up -d  start running docker images . <br/> 
docker-compose ps check if all the containers are up.

- Initialize the database of single store
   1. clone the seismos repository
   2. populate the .env variables into system
   3. find the .sql file of latest version in db_schema directory of seimos repository
   4. execute it on the singlestore database
- set the User Initial password
   1.  go to the seismos_backend_api repository
   2.  access cli of running seismos_backend_api container.
     docker-compose exec seismos_backend_api bash .   
   3.  access the running flask shell 
    poetry run flask shell
   4. run the create_user function to create the user. It will create bobo:1234 user.
    create_user()
