pipeline {
    agent any
    
    triggers{
        cron('*/1 * * * *')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Bulding the application'
                withEnv(['PYTHONPATH=C:/Users/Iuliu Antoniu/AppData/Local/Programs/Python/Python310;C:/Users/Iuliu Antoniu/AppData/Local/Programs/Python/Python310/Scripts/']){
                    bat 'py init.py'
                }
            }
        }
        stage('Test'){
            steps{
                echo 'Testing the application'
            }
        }
    }
}