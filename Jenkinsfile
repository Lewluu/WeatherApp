pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[credentialsId: 'c5c6e9f0-7347-4d1b-8d3f-a61a4108a80b', url: 'https://github.com/Lewluu/WeatherApp.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'dev', credentialsId: 'c5c6e9f0-7347-4d1b-8d3f-a61a4108a80b', url: 'https://github.com/Lewluu/WeatherApp.git'
                bat 'pip install requests'
                bat 'python init.py'
            }
        }
        stage('Test'){
            steps{
                echo 'The job was tested'
            }
        }
    }
}