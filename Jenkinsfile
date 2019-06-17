pipeline {
    agent { 
        dockerfile {
            args '-p 80:1080 -v ./counter.json:./counter.json'
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