pipeline {
    agent any
    triggers{
        cron('*/1 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building dev-consumer branch '
                bat 'python init.py'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing dev-consumer branch'
            }
        }
    }
}