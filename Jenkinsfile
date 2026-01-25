pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t fastapi-app:ci .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f fastapi_ci || true

                docker run -d \
               -p 8000:8000 \
               -e DATABASE_URL=sqlite:////data/test.db \
               -v fastapi_data:/data \
               --name fastapi_ci \
               fastapi-app:ci

               sleep 10
               docker ps | grep fastapi_ci
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                docker rm -f fastapi_ci || true
                '''
            }
        }
    }
}

