pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python count-posts.py'
            }
        }
    }
}