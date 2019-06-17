pipeline {
    agent {
    dockerfile {
        label 'test1'
        args '-p 1080:1080'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo hello'
            }
        }
    }
}
