pipeline {
    agent any
    
    // triggers{
    //     cron('*/1 * * * *')
    // }

    stages {
        stage('Build') {
            steps {
                echo 'Bulding the application'
                bat 'python main_app.py'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing the application'
            }
        }
    }
}