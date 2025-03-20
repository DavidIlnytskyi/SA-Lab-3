# SA-Lab-3

Author: Davyd Ilnytskyi

---

### Setup hazelcast network
`docker network create --subnet=172.18.0.0/16 hazelcast-network`


### Setup hazelcast node
```
bash ./bash-scripts/setup-hazelcast.sh
```

### Setup Config, Facade, Logging, Message services
```
python3 ./python-scripts/setup.py
```
![Setup image](/images/setup.png)

---

# Tasks

1. Запустити три екземпляри _logging service_, _hazelcast_
2. Записати 10 повідомлень через HTTP Post Facade-service
![Load ten messages](./images/load-10-messages.png)
3. Показати які повідомлення отримав кожен з екземплярів _logging service_.
![alt text](./images/logs-5001.png)
![alt text](./images/logs-5002.png)
![alt text](./images/logs-5003.png)
4. Через Facade Get прочитати повідомлення
![alt text](./images/Facade-Get.png)
5. Вбити один _loggigng service_ разом з _hazelcast node_
![alt text](./images/Kill-Node.png)
6. Перевірити, чи вдається прочитати повідомлення
![alt text](./images/Facade-Get-After-Kill.png)

Вдається отримати повідомлення, що розташовуються на двох інших нодах. Це відбувається, оскільки всі три ноди є окремими кластерами.