pipeline {
    agent { 
        dockerfile
        {
            args '-p 1080:1080'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'python count-posts.py'
            }
        }
    }
}
