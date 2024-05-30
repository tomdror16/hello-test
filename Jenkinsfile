pipeline { 
    agent { label 'MyVM' }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps { 
                sh 'python3 -m py_compile hello.py' 
                sh 'docker build -t hello-app:latest .'
            }
        }
        stage('Test'){
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') {
                    sh 'docker stop simple_hello_app'
                    sh 'docker rm simple_hello_app'
                }
                sh 'docker run -d -p 8080:8080 --name simple_hello_app -it hello-app'
                sh 'curl http://localhost:8080 > result.txt'
                sh 'if grep Hello! result.txt; then echo "Test1 Success"; else echo "Test1 Failed" && exit 1;fi'
                sh 'curl http://localhost:8080/healthz > result.txt'
                sh 'if grep OK result.txt ; then echo "Test2 Success"; else echo "Test2 Failed"; fi'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Copy the remote repo. Deploy then using deployment code"'
            }
        }
    }
    post {
            success {
            echo 'All tests ran fine'
        }
            failure {
            echo 'One of the steps failed'
        }
            always {
            //emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
            echo 'Sending email ....'
        }
    }
}
