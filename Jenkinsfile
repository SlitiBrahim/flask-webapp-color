node {
    stage('build') {
        /*
         openshift.withCluster() {
         def bc = openshift.selector('buildconfig/flask-webapp-color')
         bc.startBuild()
         sleep(time:3,unit:"MINUTES")
         openshift.tag('flask-webapp-color:latest', "flask-webapp-color:${BUILD_ID}")
     }
         */
        echo 'just kiddin'
    }
    stage('update argocd manifest') {
        echo 'work it'
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'jzigic-github-pat-b', url: 'https://github.com/SlitiBrahim/flask-webapp-color-argocd']]])
        sh 'git status'
        sh 'ls -lR'
        sh "sed 's/flask-webapp-color:.*/flask-webapp-color:${BUILD_ID}/' -i test/deploy.yaml"
        sh 'cat test/deploy.yaml'
    }
}

