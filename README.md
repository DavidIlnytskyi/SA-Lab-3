# SA-Lab-3

Author: Davyd Ilnytskyi

---

### Setup hazelcast network
`docker network create --subnet=172.18.0.0/16 hazelcast-network`


### Setup hazelcast node
```
docker run -d --rm -v "$(pwd)"/hazelcast-docker.xml:/opt/hazelcast/hazelcast-docker.xml \
  -e HAZELCAST_CONFIG=hazelcast-docker.xml \
  --network hazelcast-network \
  --ip 172.18.0.10 \
  --name member1 \
  -p 5701:5701 \
  hazelcast/hazelcast:latest
  ```