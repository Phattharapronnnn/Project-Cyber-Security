import json
from elasticsearch import Elasticsearch


def getdata():
    # es = Elasticsearch(['http://172.28.3.108:9200'])  #Hacking 3
    es = Elasticsearch(['http://172.28.4.6:9200'])   #WU-WiFi
    index_name = 'logstash-2024.04.08'

    scroll_size = 10000
    search_body = {
        "query": {
            "match_all": {}  # คิวรี่ทั้งหมด
        },
        "size": scroll_size,
    }

    response = es.search(index=index_name, body=search_body, scroll='100m')
    scroll_id = response['_scroll_id']
    results = []

    while True:
        hits = response['hits']['hits']
        if not hits:
            break
        results.extend([hit['_source'] for hit in hits])
        response = es.scroll(scroll_id=scroll_id, scroll='100m')

    # Save ลง JSON
    filename = f"data_all.json"

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{filename}'")

getdata()
