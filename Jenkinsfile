pipeline {
  agent any

  environment {
    DOCKER_USER = 'nukal'
    IMAGE_NAME = 'nukala_cicd1/python-jenkins-app'
    IMAGE_TAG = 'latest'
  }

  stages {
    stage('Checkout') {
      steps {
        echo "Checking out source code..."
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        echo "Building Docker image..."
        sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'nukala_cicd1',
          usernameVariable: 'DOCKER_USER',
          passwordVariable: 'DOCKER_PASS'
        )]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push $IMAGE_NAME:$IMAGE_TAG
          '''
        }
      }
    }
  }

  post {
    success {
      echo "✅ Docker image pushed: $IMAGE_NAME:$IMAGE_TAG"
    }
    failure {
      echo "❌ Build or push failed. Check logs."
    }
  }
}
