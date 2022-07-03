node {
    stage('build') {
        openshift.withCluster() {
            def bc = openshift.selector('buildconfig/flask-webapp-color')
            bc.startBuild()
            sleep(time:3,unit:"MINUTES")
            openshift.tag('flask-webapp-color:latest', "flask-webapp-color:${BUILD_ID}")
        }
    }
    stage('update argocd manifest') {
        // clean workspace
        sh 'rm -rf *'
        withCredentials([string(credentialsId: 'PAT', variable: 'TOKEN')]) {
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://${TOKEN}@github.com/SlitiBrahim/flask-webapp-color-argocd.git']]])
            sh 'git checkout main'
            sh 'git config --local user.email "brahim.sliti15@gmail.com"'
            sh 'git config --local user.name "SlitiBrahim"'
            sh "git config --local remote.origin.url 'https://${TOKEN}@github.com/SlitiBrahim/flask-webapp-color-argocd.git'"
            sh 'ls -lR'
            sh "sed 's/flask-webapp-color:.*/flask-webapp-color:${BUILD_ID}/' -i test/deploy.yaml"
            sh 'cat test/deploy.yaml'
            sh 'git pull'
            sh 'git status'
            sh "git commit -am 'Pipeline push test image version ${BUILD_ID}'"
            sh 'git push https://${TOKEN}@github.com/SlitiBrahim/flask-webapp-color-argocd.git'
        }
    }
}
