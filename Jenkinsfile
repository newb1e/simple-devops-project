pipeline {
    agent { 
        dockerfile {
            args '-p 1080:1080'
        } 
    }
    stages {
        stage('Test') {
            steps {
                sh 'python count-posts.py &'
                input message: 'Finished using the web site? (Click "Proceed" to continue)'
            }
        }
    }
}