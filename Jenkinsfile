node {
    stage('build') {
        openshift.withCluster() {
            def bc = openshift.selector('buildconfig/flask-webapp-color')
            bc.startBuild()
            sleep(time:3,unit:"MINUTES")
            openshift.tag('flask-webapp-color:latest', "flask-webapp-color:${BUILD_ID}")
        }
    }
    stage('update argocd manifest' {
            echo 'work it'
        }
    }
}
