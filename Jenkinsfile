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
                // This uses the 'nohup' and '&' to run the app in the background, 
                // preventing the Jenkins job from hanging.
                sh 'pkill -f "python3 app.py" || true' // Stop if running
                sh 'nohup python3 app.py > app.log 2>&1 &'
                echo 'Application deployed to port 5000!'
            }
        }
    }
}