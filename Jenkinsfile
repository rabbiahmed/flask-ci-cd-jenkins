pipeline {
    agent any // Specifies where the pipeline will run (your Jenkins agent/server)

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
                    def PYTHON3 = '/usr/bin/python3'
                    def WORKSPACE = pwd()
                    def APP_COMMAND = "${PYTHON3} ${WORKSPACE}/app.py"
                    def LOG_FILE = "${WORKSPACE}/app.log"

                    // 1. Kill any existing instance
                    sh "pkill -f \"${PYTHON3} app.py\" || true" 

                    // 2. Start the new instance using a detached shell command (double forking)
                    sh "sh -c '${APP_COMMAND} > ${LOG_FILE} 2>&1 &' &"
                    
                    // Wait briefly to allow the application to start
                    sh 'sleep 5' 
                }

                echo 'Application deployed to port 5000!'
            }
        }
    }
}