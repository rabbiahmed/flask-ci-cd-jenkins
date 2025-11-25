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
                echo 'Deploying application via Systemd... 🟢'
                script {
                    // 1. Copy the service file into the systemd directory
                    // The sudo is necessary to write to /etc/systemd/system/
                    sh 'sudo /usr/bin/cp flask.service /etc/systemd/system/flask.service' 

                    // 2. Reload systemd manager configuration
                    sh 'sudo systemctl daemon-reload'

                    // 3. Enable the service (ensures it starts on boot)
                    sh 'sudo systemctl enable flask.service'

                    // 4. Restart the service (deploys the new code)
                    // This is the command that runs Gunicorn outside of the Jenkins session.
                    sh 'sudo systemctl restart flask.service'
                    
                    // 5. Check the status (optional, but good for logs)
                    sh 'sudo systemctl status flask.service'
                }
                echo 'Application deployed to port 5000 and managed by Systemd!'
            }
        }
    }
}