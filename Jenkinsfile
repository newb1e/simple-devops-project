pipeline {
    agent { dockerfile true }
    //{
    //    args '-p 1080:1080'
    //    }
    //}
    stages {
        stage('Build') {
            steps {
                sh 'echo hello'
                sh 'python count-posts.py'
            }
        }
    }
}
