#!/usr/bin/bash
# Pull the image
docker pull memsql/cluster-in-a-box


# Spin up a MemSQL cluster on your machinedocker 
run -i --init \

    --name memsql-ciab \
    -e LICENSE_KEY=BDAwMjQ0NGEyNmY5MDQ0MzE5ZTUxMWFmNWJkYTNkNTVkAAAAAAAAAAAEAAAAAAAAAAwwNgIZAM8vRZfE1C7YTy2pXGFMExpsLbqEKmqWRwIZAMpeZkEXDWn3qdSYenuOtB7LWuMZy5iKMw== \

-e ROOT_PASSWORD=jhe4odcl146z3
    -p 3306:3306 -p 8080:8080 \
memsql/cluster-in-a-box

# [PASSWORD] should be non-empty

# If you don't have a License key you can obtain one by 
# registering on the MemSQL Customer Portal: https://portal.memsql.com/


# Start the container
docker start memsql-ciab


# Connect to MemSQL Studio at http://localhost:8080
# The default Username is root and Password should be left blank.


# Connect to the container and open the MemSQL client application
docker exec -it memsql-ciab memsql


# You can also connect to MemSQL with a third-party tools like Sequel Pro or the MySQL client
mysql -h 127.0.0.1 -u root -P 3306 --prompt="memsql> "


# Stop and remove the container
docker stop memsql-ciab && docker rm memsql-ciab