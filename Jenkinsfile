pipeline {
    agent any
    // triggers{
    //     cron('*/1 * * * *')
    // }
    stages {
        stage('Build') {
            steps {
                echo 'Building dev-producer branch '
                bat 'python init.py'
            }
            post {
                success {
                    echo 'Success: data_out.yaml file created!'
                }
                failure {
                    echo 'Failed to create data_out.yaml!'
                }
            }
        }
        stage('Test'){
            steps{
                echo 'Testing dev-producer branch'
            }
        }
    }
}