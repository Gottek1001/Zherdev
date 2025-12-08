pipeline {
    agent any
    
    environment {
        PROJECT_NAME = 'devops-dz'
        DOCKER_COMPOSE = 'docker-compose.yml'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', 
                    url: 'https://github.com/Gottek1001/Zherdev.git'
                echo 'Код получен из GitHub'
            }
        }
        
        stage('Build Docker Images') {
            steps {
                sh '''
                    echo " Сборка Docker образов..."
                    docker-compose -f ${DOCKER_COMPOSE} build
                '''
            }
        }
        
        stage('Run Application') {
            steps {
                sh '''
                    echo "Запуск приложения..."
                    docker-compose -f ${DOCKER_COMPOSE} down
                    docker-compose -f ${DOCKER_COMPOSE} up -d
                '''
            }
        }
        
        stage('Health Check') {
            steps {
                sleep 10
                sh '''
                    echo "Проверка приложения..."
                    if curl -s -f http://localhost:5000 > /dev/null; then
                        echo "Приложение работает!"
                        echo "Доступно по адресу: http://localhost:5000"
                        echo "И через Nginx: http://localhost:8080"
                    else
                        echo "Приложение не отвечает"
                        exit 1
                    fi
                '''
            }
        }
        
        stage('Show Logs') {
            steps {
                sh '''
                    echo "Последние логи:"
                    docker-compose -f ${DOCKER_COMPOSE} logs --tail=20
                '''
            }
        }
    }
    
    post {
        success {
            echo ' Pipeline успешно завершен!'
            emailext (
                subject: "CI/CD Pipeline успешен: ${env.JOB_NAME}",
                body: "Сборка ${env.BUILD_NUMBER} завершена успешно.\n\nПосмотреть: ${env.BUILD_URL}",
                to: 'fvika512@gmail.com'
            )
        }
        failure {
            echo 'Pipeline завершился с ошибкой'
            emailext (
                subject: "CI/CD Pipeline неудача: ${env.JOB_NAME}",
                body: "Сборка ${env.BUILD_NUMBER} завершена с ошибкой.\n\nПосмотреть: ${env.BUILD_URL}",
                to: 'fvika512@gmail.com'
            )
        }
    }
}