pipeline {
    agent {}
    options {
        timeout(time: 20, unit: 'MINUTES') 
    }
    stages {
        stage('preamble') {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject() {
                            echo "Using project: ${openshift.project()}"
                        }
                    }
                }
            }
        }
    }
}
