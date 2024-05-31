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
  
    stage('Build') {
      steps {
        echo 'Building the ToDo application on Docker'
        sh 'docker build . -t dev:latest'
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

    stage('Deploying React.js container to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "deployment.yaml", "service.yaml")
        }
      }
    }

  }

}
