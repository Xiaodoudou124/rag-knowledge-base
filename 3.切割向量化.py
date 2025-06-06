import requests
import functools


def file_chunk_list():
    # 1.读取文件内容
    with open("中医v1.txt", encoding='utf-8', mode='r') as fp:
        data = fp.read()

    # 2.根据换行切割
    chunk_list = data.split("\n\n")
    return [chunk for chunk in chunk_list if chunk]


def ollama_embedding_by_api(text):
    res = requests.post(
        url="http://127.0.0.1:11434/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )
    embedding = res.json()['embedding']
    return embedding


def run():
    chunk_list = file_chunk_list()
    for chunk in chunk_list:
        vector = ollama_embedding_by_api(chunk)
        print(chunk)
        print(vector)


if __name__ == '__main__':
    run()