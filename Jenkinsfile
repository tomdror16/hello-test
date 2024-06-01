pipeline {

  environment {
    dockerimagename = "tomdror166/dev:latest"
    dockerImage = ""
  }

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git branch: 'main', 
                    url: 'https://github.com/tomdror16/hello-test.git'
      }
    }

    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build dockerimagename
        }
      }
    }

    stage('Pushing Image') {
      environment {
               registryCredential = 'dockerhub-credentials'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push("latest")
          }
        }
      }
    }
    stage(‘Deploy to Minikube’) {
      steps {
          sh ‘kubectl apply -f my-react-deployments.yaml’

        }
      }
    }

  }

}
