pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub') // Environment variable for Docker Hub credentials
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'main', url: 'https://github.com/Sanjeevvisuu/simple-app.git'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo 'Building the Django application as a Docker image...'
                    sh '''
                    # Ensure that the Jenkins user can access Docker (optional if sudo is configured)
                         docker build -t simplecicd .  # Build with the tag "simplecicd"
                    '''
                }
            }
        }

        stage('Docker Image Push') {
            steps {
                script {
                    echo 'Pushing application to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                        # Log in to Docker Hub
                        echo "$DOCKER_PASSWORD" |  docker login -u "$DOCKER_USERNAME" --password-stdin
                        # Tag and push the image (ensure you're tagging the correct one)
                        docker tag simplecicd:latest $DOCKER_USERNAME/simplecicd:latest
                        docker push $DOCKER_USERNAME/simplecicd:latest
                        '''
                    }
                    echo 'Pushed application to Docker Hub.'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            // Optional: Add a cleanup step for Docker images
           
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
