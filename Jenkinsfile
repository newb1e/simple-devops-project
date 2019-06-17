pipeline {
    agent { 
        dockerfile {
            args '-p 1080:1080'
        } 
    }
    stages {
        stage('Build') {
            steps {
                sh 'python count-posts.py'
            }
        }
    }
}