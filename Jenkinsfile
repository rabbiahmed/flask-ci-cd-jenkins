pipeline {
    agent any // Specifies where the pipeline will run (your Jenkins agent/server)

    // Environment configuration
    environment {
        PATH = "${env.PATH}:/var/lib/jenkins/.local/bin"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clones the code from the specified SCM
                git url: 'https://github.com/rabbiahmed/flask-ci-cd-jenkins.git', branch: 'main' // Remote Repository
            }
        }
        
        stage('Build & Dependencies') {
            steps {
                sh 'pip install -r requirements.txt' // Install Flask
            }
        }

        stage('Test (Simulated)') {
            steps {
                // In a real project, this would run unit/integration tests
                echo 'Running simulated tests...'
                sh 'python3 -m compileall app.py' // Simple syntax check
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application... 🟢'
                script {
                    def WORKSPACE = pwd()
                    def LOG_FILE = "${WORKSPACE}/app.log"
                    // Use the full explicit path to the installed gunicorn executable
                    def GUNICORN_BIN = "/var/lib/jenkins/.local/bin/gunicorn" 

                    // 1. Kill any existing Gunicorn instance
                    sh "pkill -f 'gunicorn app:app' || true" 

                    // 2. FINAL Deployment Command: Use setsid with an inline shell execution
                    // This creates a new session and process group, fully detaching the process.
                    sh "setsid sh -c '${GUNICORN_BIN} --bind 0.0.0.0:5000 app:app > ${LOG_FILE} 2>&1 &' > /dev/null"
                    
                    // Wait briefly for the server to spin up
                    sh 'sleep 5' 
                }

                echo 'Application deployed to port 5000 via Gunicorn!'
            }
        }
    }
}