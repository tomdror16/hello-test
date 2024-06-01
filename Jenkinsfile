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

    
stage('Deploy to Kubernetes Cluster') {
  steps {
  ///CREATE AND APPLY THE PATCH. REMEMBER TO LOGIN ON THE CLUSTER. (-s $CLUSTER_URL --token $TOKEN_CLUSTER --insecure-skip-tls-verify)
    sh  '''
                     
    PATCH_TO_DEPLOY={\\"metadata\\":{\\"labels\\":{\\"version\\":\\"${env.BUILD_ID}\\"}},\\"spec\\":{\\"template\\":{\\"metadata\\":{\\"labels\\":{\\"version\\":\\"${env.BUILD_ID}\\"}},\\"spec\\":{\\"containers\\":[{\\"name\\":\\"$NAME_DEPLOY\\",\\"image\\":\\"my-image:${env.BUILD_ID}\\"}]}}}}
                    
    kubectl patch deployment $NAME_DEPLOY  -n $NAMESPACE -p $PATCH_TO_DEPLOY \
    -s $CLUSTER_URL --token $TOKEN_CLUSTER --insecure-skip-tls-verify
                    
    '''
                    
    }
}

      
    }

  }

}
