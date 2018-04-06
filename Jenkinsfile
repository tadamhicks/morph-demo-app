import groovy.json.JsonOutput 

node {

    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("tadamhicks/demo_app")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }

    stage('Provision Dev App') {
        /*
         *
         *  */

        withCredentials([string(credentialsId: 'sandbox-morph-scrt', variable: 'bearer')]) {
            String morpheusUrl = 'https://sandbox.morpheusdata.com/api/apps'

            Map<?, ?> postBody = [ "image": "/assets/apps/template.png", "tiers": [ "App": [ "linkedTiers": [ "Cache", "Database" ], "tier": [ "bootOrder": 1, "lockedFields": [ "bootOrder" ] ], "instances": [ [ "instance": [ "type": "docker", "cloud": "Labs UCS", "layout": [ "code": "docker-1.7-single", "id": 206 ], "expireDays": "1", "name": "frontend-${env.BUILD_NUMBER}", "allowExisting": true ], "backup": [ "createBackup": true ], "evars": [ [ "name": "DB_NAME", "value": "demo_app" ], [ "name": "WORDNIK_API_KEY", "value": "5455816781cb799cf994f0b58cc027cb0dd2633addcdd2025" ], [ "name": "ENVIRONMENT", "value": "dev" ] ], "layoutSize": 3, "volumes": [ [ "size": 5, "name": "root", "rootVolume": true ] ], "ports": [ [ "port": "9090", "lb": "", "name": "web" ] ], "config": [ "configVolume": "", "dockerImage": "tadamhicks/demo_app", "dataVolume": "", "dockerImageVersion": "${env.BUILD_NUMBER}", "logVolume": "", "expose": 8080, "dockerRegistryId": "" ], "plan": [ "code": "container-512", "id": 70 ], "metadata": [ [ "name": "", "value": "" ] ] ] ] ], "Database": [ "linkedTiers": [], "instances": [ [ "instance": [ "type": "mysql", "cloud": "Labs UCS", "layout": [ "code": "mysql-5.7-single", "id": 87 ], "expireDays": "1", "name": "db-${env.BUILD_NUMBER}", "allowExisting": true ], "backup": [ "createBackup": true ], "volumes": [ [ "size": 5, "name": "root", "rootVolume": true ] ], "plan": [ "code": "container-512", "id": 70 ], "config": [ "password": "password", "rootPassword": "password", "username": "admin" ], "deployment": [ "versionId": 61, "id": 13 ], "metadata": [ [ "name": "", "value": "" ] ], "evars": [ [ "name": "", "value": "" ] ] ] ] ], "Cache": [ "linkedTiers": [], "instances": [ [ "instance": [ "type": "redis", "cloud": "Labs UCS", "layout": [ "code": "redis-3.2-single", "id": 666 ], "expireDays": "1", "name": "cache-${env.BUILD_NUMBER}", "allowExisting": true ], "backup": [ "createBackup": true ], "volumes": [ [ "size": 3, "name": "root", "rootVolume": true ] ], "plan": [ "code": "container-256", "id": 69 ], "config": [], "metadata": [ [ "name": "", "value": "" ] ], "evars": [ [ "name": "", "value": "" ] ] ] ] ] ], "name": "demo_app_${env.BUILD_NUMBER}", "id": 68, "templateName": "A_D_A", "group": [ "id": 2, "name": "All Clouds Demo" ], "environment": "Dev" ]

            sh 'env > /tmp/env.txt'
            for (String i : readFile('/tmp/env.txt').split("\r?\n")) {
                println i
            }

            echo morpheusApp.buildApp(morpheusUrl, postBody, "${bearer}")
        }
    }

        stage('Provision Prod App') {

        withCredentials([string(credentialsId: 'demo-morph-scrt', variable: 'bearer')]) {
            String morpheusUrl = 'https://demo.morpheusdata.com/api/apps'

            Map<?, ?> postBody = [ "image": "https://demo.morpheusdata.com/storage/logos/uploads/AppTemplate/69/templateImage/Screen Shot 2017-11-21 at 7.52.28 PM_original.png", "tiers": [ "App": [ "linkedTiers": [ "Cache", "Database" ], "tier": [ "bootOrder": 1, "lockedFields": [ "bootOrder" ] ], "instances": [ [ "instance": [ "type": "wapp", "cloud": "AWS Cali", "layout": [ "code": "03574fc2-00b5-455c-919d-550230a1de96", "id": 923 ], "expireDays": "2", "name": "FRONT", "allowExisting": true, "shutdownDays": "1" ], "backup": [ "createBackup": true ], "loadBalancer": [ [ "externalAddressCheck": true, "protocol": "http", "vipPort": 101, "internalPort": 9090, "vipHostname": "morph.morph.morph.    com", "vipShared": "off", "name": "morpheus-demo_app", "externalAddress": "off", "id": -2, "balanceMode": "leastconnections", "externalPort":     9090, "enabled": true ] ], "layoutSize": 3, "volumes": [ [ "size": 3, "name": "root", "rootVolume": true ] ], "plan": [ "code": "container-256", "id": 69 ], "metadata": [ [ "name": "", "value": "" ] ], "evars": [ [ "name": "DB_NAME", "value": "demo_app" ], [ "name": "WORDNIK_API_KEY", "value": "5455816781cb799cf994f0b58cc027cb0dd2633addcdd2025" ], [ "name": "ENVIRONMENT", "value": "prod" ] ] ] ] ], "Database": [ "linkedTiers": [], "instances": [ [ "instance": [ "type": "mysql", "cloud": "AWS Cali", "layout": [ "code": "mysql-amazon-5.6-master-slave", "id": 440 ], "expireDays": "2", "name": "BACK", "allowExisting": true, "shutdownDays": "1", "userGroup": [ "id": "" ], "usingExisting": true, "existingInstanceId": 3051 ], "backup": [ "createBackup": true ], "networkInterfaces": [ [ "primaryInterface": true, "network": [ "id": "network-91" ] ] ], "volumes": [ [ "vId": 508413, "size": 1, "maxIOPS": null, "name": "root", "rootVolume": true, "storageType": 6 ] ], "plan": [ "code": "amazon-t2.small", "id": 3 ], "config": [ "publicIpType": "subnet" ], "metadata": [ [ "name": "", "value": "" ] ], "evars": [ [ "name": "", "value": "" ] ], "securityGroups": [ [ "id": "sg-63bae304" ] ] ] ] ], "Cache": [ "linkedTiers": [], "instances": [ [ "instance": [ "type": "redis", "cloud": "AWS Cali", "layout": [ "code": "redis-3.2-single", "id": 666 ], "expireDays": "2", "name": "MIDDLE", "allowExisting": true, "shutdownDays": "1" ], "backup": [ "createBackup": true ], "volumes": [ [ "size": 3, "name": "root", "rootVolume": true ] ], "plan": [ "code": "container-256", "id": 69 ], "metadata": [ [ "name": "", "value": "" ] ], "evars": [ [ "name": "", "value": "" ] ] ] ] ] ], "name": "a_d_a-prod", "description": "Production version using existing instances to promote", "templateImage": "", "id": 69, "templateName": "A_D_A-prod", "group": [ "id": 2, "name": "All Clouds Demo" ], "environment": "Production"]

            morpheusApp.buildApp(morpheusUrl, postBody, "${bearer}")
        }

    }

}