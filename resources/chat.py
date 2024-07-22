from datetime import datetime
import json
from flask import request
from flask_restful import Resource
import csv
from sentence_transformers import SentenceTransformer, util
import os

# 캐시 디렉토리 설정
cache_dir = '/tmp/transformers_cache'
os.makedirs(cache_dir, exist_ok=True)

# HF_HOME 환경 변수를 설정
os.environ['HF_HOME'] = cache_dir

# 모델과 데이터를 전역 변수로 설정하여 초기화 시 한 번만 로드
sbert_model = SentenceTransformer('jhgan/ko-sroberta-multitask', cache_folder=cache_dir)

local_data_path = './data/combined_data.csv'
with open(local_data_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

embeddings = [json.loads(row['embedding']) for row in data]
chatbot_responses = [row['chatbot'] for row in data]

class ChatBotResource(Resource):
    def post(self):
        message = request.json.get('message')
        if not message:
            return {'result': 'fail', 'error': 'No message provided'}, 400

        try:
            # 유저가 입력한 문장을 벡터라이징
            embedding = sbert_model.encode(message, convert_to_tensor=True)

            # 유사도 계산을 최적화하여 가장 유사한 답변을 찾기
            similarities = util.pytorch_cos_sim(embedding, embeddings)
            max_index = similarities.argmax().item()
            answer = chatbot_responses[max_index]
            timestamp = datetime.now().isoformat()

            print(f"Message: {message}")
            print(f"Answer: {answer}")
            print(f"Timestamp: {timestamp}")
            return {'result': 'success', 'answer': answer, 'timeStamp': timestamp}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {'result': 'fail', 'error': 'An error occurred'}, 500
