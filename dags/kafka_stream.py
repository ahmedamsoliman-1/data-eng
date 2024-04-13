import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
# from utils import StreamLogger


# stream_logger = StreamLogger()



default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 9, 3, 10, 00)
}

# kafka_servers = ['ec2-3-28-179-223.me-central-1.compute.amazonaws.com:9092']
kafka_servers = ['localhost:9092']

def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=kafka_servers, max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: #1 minute
            break
        try:
            res = format_data(get_data())
            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

# def stream_data():
#     import json
#     from kafka import KafkaProducer
#     import time

#     res = json.dumps(get_data())
#     producer = KafkaProducer(bootstrap_servers=kafka_servers, max_block_ms=5000)
#     print(res)
#     # producer.send('users_created', json.dumps(res).encode('utf-8'))

# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:

#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )


# print(format_data(get_data()))
stream_data()