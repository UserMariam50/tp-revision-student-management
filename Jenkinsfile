
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install flask'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m unittest test_student_manager.py -v'
            }
        }

    }
}
