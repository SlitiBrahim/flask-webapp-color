node {
    /*
    stage('build') {
        openshift.withCluster() {
            def bc = openshift.selector('buildconfig/flask-webapp-color')
            bc.startBuild()
            sleep(time:3,unit:"MINUTES")
            openshift.tag('flask-webapp-color:latest', "flask-webapp-color:${BUILD_ID}")
        }
    } */
    stage('update argocd manifest') {
        echo 'work it'
        cleanWs()
        //checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://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@github.com/SlitiBrahim/flask-webapp-color-argocd.git']]])
        sh 'git clone https://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@github.com/SlitiBrahim/flask-webapp-color-argocd.git'
        dir('flask-webapp-color-argocd') {
            sh 'git status'
            sh 'git checkout main'
            sh 'git config user.email "brahim.sliti15@gmail.com"'
            sh 'git config user.name "SlitiBrahim"'
            //sh "git config remote.origin.url 'https://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@github.com/SlitiBrahim/flask-webapp-color-argocd.git'"
            sh 'ls -lR'
            sh "sed 's/flask-webapp-color:.*/flask-webapp-color:${BUILD_ID}/' -i test/deploy.yaml"
            sh 'cat test/deploy.yaml'
            sh 'git status'
            sh "git commit -am 'Pipeline push image version ${BUILD_ID}'"
            sh 'git log'
            sh 'git remote -v'
            sh 'git push https://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@github.com/SlitiBrahim/flask-webapp-color-argocd.git'
        }
    }
}

