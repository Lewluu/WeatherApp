pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git branch: 'dev', credentialsId: 'c5c6e9f0-7347-4d1b-8d3f-a61a4108a80b', url: 'https://github.com/Lewluu/WeatherApp.git'
                echo 'Bulding the application'
                echo '$PATH'
                // bat 'python get-pip.py'
                bat 'pip install requests'
                // bat 'python init.py'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing the application'
            }
        }
    }
}