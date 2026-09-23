pipeline {
    agent { label 'windows-agent' } // Replace with your specific Windows agent label

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from your GitHub repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat """
                call venv\\Scripts\\activate
                pytest test_app.py --junitxml=results.xml
                """
            }
        }
    }

    post {
        success {
            echo 'Build succeeded! All unit tests passed.'
        }
        failure {
            echo 'Build failed! One or more unit tests did not pass.'
        }
    }
}
