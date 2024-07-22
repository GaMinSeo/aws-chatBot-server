# 챗봇 API

이 프로젝트는 SentenceTransformer 모델을 사용하여 사용자 입력과 미리 정의된 응답 간의 유사성을 기반으로 응답을 제공하는 간단한 챗봇 API입니다.
![initial](https://github.com/user-attachments/assets/f20758f1-6fb5-4986-8eeb-bf7ea8b4d7fb.PNG)
## 목차

- [API 엔드포인트](#api-엔드포인트)
- [데이터 형식](#데이터-형식)
- [의존성](#의존성)
- [AWS Lambda 배포](#aws-lambda-배포)

## API 엔드포인트

### POST /chatbot

- **요청 형식**: BODY JSON
    ```json
    {
        "message": "안녕하세요"
    }
    ```
- **응답 형식**: JSON
    ```json
    {
        "result": "success",
        "answer": "안녕하세요! 무엇을 도와드릴까요?",
        "timeStamp": "2023-07-22T12:34:56.789Z"
    }
    ```

## 데이터 형식

- **combined_data.csv** 파일은 두 개의 주요 열을 포함합니다:
  - `embedding`: 문장의 임베딩 벡터
  - `chatbot`: 챗봇의 응답

## 의존성

이 프로젝트는 다음과 같은 주요 라이브러리에 의존합니다:
- Flask
- Flask-RESTful
- SentenceTransformer
- PyTorch
- 기타 의존성은 `requirements.txt` 파일을 참고하십시오.

## AWS Lambda 배포

### 가상환경 설정 및 Docker 컨테이너로 AWS ECR 활용

1. `Dockerfile` 작성:

2. Docker 이미지 빌드 및 ECR에 푸시:

3. AWS Lambda 함수 생성 및 설정:
    - AWS Lambda 콘솔에서 새 함수를 생성하고, 배포 패키지로 ECR 이미지를 사용하도록 설정합니다.
    - 필요한 IAM 역할과 권한을 설정합니다.

4. API Gateway 설정:
    - AWS API Gateway를 사용하여 Lambda 함수와 연결하고, HTTP 엔드포인트를 설정합니다.
