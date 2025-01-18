pipeline {
    agent any

    options {
        timestamps()        // Adds timestamps to console output
        disableConcurrentBuilds()  // Prevents concurrent builds of the pipeline
    }

    environment {
        PYTHON_VERSION = '3.12.0'  // Define the Python version to use
        PYTHON_URL = "https://www.python.org/ftp/python/${PYTHON_VERSION}/python-${PYTHON_VERSION}-amd64.exe"
    }

    stages {
        stage('Install Python 3.12') {
            steps {
                script {
                    // Download and install Python 3.12
                    bat '''
                    IF NOT EXIST "C:\\Python312\\" (
                        curl -o python-3.12.exe ${PYTHON_URL}
                        python-3.12.exe /quiet InstallAllUsers=1 PrependPath=1 TargetDir=C:\\Python312
                        python --version
                    ) ELSE (
                        echo "Python 3.12 is already installed."
                    )
                    '''
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Create and activate virtual environment
                    bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest
                    bat '''
                    call venv\\Scripts\\activate
                    pytest --html=reports/report.html --self-contained-html
                    '''
                }
            }
        }
    }

    post {
        always {
            // Archive test reports
            archiveArtifacts artifacts: 'reports\\report.html', fingerprint: true

            echo 'Pipeline execution completed.'
            cleanWs()  // Clean workspace after pipeline execution
        }
        success {
            echo 'Tests Passed Successfully!'
        }
        failure {
            echo 'Pipeline Failed. Check logs for details.'
        }
    }
}
