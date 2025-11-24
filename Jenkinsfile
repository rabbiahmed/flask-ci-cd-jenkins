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
                // Stop any existing instance, then start the new one in the background
                echo 'Deploying application... 🟢'
                
                // Define variables for clarity and robustness
                script {
                    def PYTHON3 = '/usr/bin/python3'
                    def WORKSPACE = pwd() // Gets the current workspace path
                    def APP_COMMAND = "${PYTHON3} ${WORKSPACE}/app.py"

                    // 1. Kill any existing instance using the full command path
                    sh "pkill -f \"${PYTHON3} app.py\" || true" 

                    // 2. Start the new instance using nohup and full paths
                    // We run this in the background (&) and discard shell output (> /dev/null 2>&1)
                    sh "nohup ${APP_COMMAND} > ${WORKSPACE}/app.log 2>&1 &" 
                    
                    // Wait briefly to allow the application to start before the job ends
                    sh 'sleep 5' 
                }

                echo 'Application deployed to port 5000!'
            }
        }
    }
}