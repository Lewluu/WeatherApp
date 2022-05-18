pipeline {
    agent any
    
    triggers{
        cron('*/1 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Bulding the application'
                bat 'python3 init.py'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing the application'
            }
        }
    }
}