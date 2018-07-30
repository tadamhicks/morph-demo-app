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

        withCredentials([string(credentialsId: 'demo-morph-scrt', variable: 'bearer')]) {
            String morpheusUrl = 'https://demo.morpheusdata.com/api/apps'

            Map<?, ?> postBody = [ "image": "/assets/apps/template.png", "tiers": [ "App": [ "linkedTiers": [ "Cache", "Database" ], "tier": [ "bootOrder": 1, "lockedFields": [ "bootOrder" ] ], "instances": [ [ "instance": [ "type": "docker", "cloud": "UCS Docker", "layout": [ "code": "docker-1.7-single", "id": 206 ], "expireDays": "1", "name": "frontend-${env.BUILD_NUMBER}", "allowExisting": true ], "backup": [ "createBackup": true ], "evars": [ [ "name": "DB_NAME", "value": "demo_app" ], [ "name": "WORDNIK_API_KEY", "value": "5455816781cb799cf994f0b58cc027cb0dd2633addcdd2025" ], [ "name": "ENVIRONMENT", "value": "dev" ] ], "layoutSize": 3, "volumes": [ [ "size": 5, "name": "root", "rootVolume": true ] ], "ports": [ [ "port": "9090", "lb": "", "name": "web" ] ], "config": [ "configVolume": "", "dockerImage": "tadamhicks/demo_app", "dataVolume": "", "dockerImageVersion": "${env.BUILD_NUMBER}", "logVolume": "", "expose": 8080, "dockerRegistryId": "" ], "plan": [ "code": "container-512", "id": 70 ], "metadata": [ [ "name": "", "value": "" ] ] ] ] ], "Database": [ "linkedTiers": [], "instances": [ [ "instance": [ "type": "mysql", "cloud": "UCS Docker", "layout": [ "code": "mysql-5.7-single", "id": 87 ], "expireDays": "1", "name": "db-${env.BUILD_NUMBER}", "allowExisting": true ], "backup": [ "createBackup": true ], "volumes": [ [ "size": 5, "name": "root", "rootVolume": true ] ], "plan": [ "code": "container-512", "id": 70 ], "config": [ "password": "password", "rootPassword": "password", "username": "admin" ], "deployment": [ "versionId": 61, "id": 13 ], "metadata": [ [ "name": "", "value": "" ] ], "evars": [ [ "name": "", "value": "" ] ] ] ] ], "Cache": [ "linkedTiers": [], "instances": [ [ "instance": [ "type": "redis", "cloud": "UCS Docker", "layout": [ "code": "redis-3.2-single", "id": 666 ], "expireDays": "1", "name": "cache-${env.BUILD_NUMBER}", "allowExisting": true ], "backup": [ "createBackup": true ], "volumes": [ [ "size": 3, "name": "root", "rootVolume": true ] ], "plan": [ "code": "container-256", "id": 69 ], "config": [], "metadata": [ [ "name": "", "value": "" ] ], "evars": [ [ "name": "", "value": "" ] ] ] ] ] ], "name": "demo_app_${env.BUILD_NUMBER}", "id": 68, "templateName": "A_D_A", "group": [ "id": 2, "name": "All Clouds Demo" ], "environment": "Dev" ]


            echo morpheusApp.buildApp(morpheusUrl, postBody, "${bearer}")
        }
    }

    stage('Provision Staging App') {
        withCredentials([string(credentialsId: 'demo-morph-scrt', variable: 'bearer')]) {
            String morpheusUrl = 'https://demo.morpheusdata.com/api/apps'

        Map<?, ?> postBody = [  "image": "https://demo.morpheusdata.com/storage/logos/uploads/AppTemplate/68/templateImage/Screen Shot 2017-11-21 at 7.52.28 PM_original.png",  "tiers": [  "App": [  "linkedTiers": [  "Cache",  "Database"  ],  "tier": [  "bootOrder": 1,  "lockedFields": [  "bootOrder"  ]  ],  "instances": [  [  "instance": [  "type": "docker",  "cloud": "AWS Cali",  "layout": [  "code": "docker-1.7-single",  "id": 206  ],  "expireDays": "1",  "name": "$[userInitials]-demo-$[cloudCode]-$[type]-$[sequence]",  "allowExisting": false,  "shutdownDays": "1"  ],  "planObj": [  "code": "container-128",  "customCores": false,  "coresPerSocket": null,  "hasDatastore": false,  "maxMemory": 134217728,  "customCoresPerSocket": false,  "rootStorageTypes": [],  "addVolumes": false,  "customMaxStorage": false,  "id": 68,  "storageTypes": [  [  "volumeType": "disk",  "code": "standard",  "resizable": false,  "editable": false,  "maxIOPS": null,  "displayOrder": 1,  "deletable": false,  "minStorage": null,  "hasDatastore": true,  "description": "Standard",  "externalId": null,  "customSize": true,  "configurableIOPS": false,  "optionTypes": [],  "enabled": true,  "defaultType": true,  "autoDelete": true,  "name": "Standard",  "id": 1,  "customLabel": true,  "maxStorage": null,  "volumeOptionSource": null,  "minIOPS": null  ]  ],  "value": 68,  "maxStorage": 1073741824,  "supportsAutoDatastore": true,  "memoryOptions": [],  "maxDisks": null,  "coreOptions": [],  "maxDisk": null,  "cpuOptions": [],  "maxCpu": null,  "datastores": [],  "customMaxDataStorage": false,  "minDisk": 1,  "lvmSupported": true,  "customMaxMemory": false,  "noDisks": false,  "autoOptions": null,  "rootCustomSizeOptions": [],  "maxCores": null,  "rootDiskCustomizable": false,  "name": "128MB Memory, 1GB Storage",  "customCpu": false,  "customSizeOptions": [],  "customizeVolume": false  ],  "backup": [  "createBackup": true  ],  "evars": [  [  "name": "WORDNIK_API_KEY",  "value": "5455816781cb799cf994f0b58cc027cb0dd2633addcdd2025"  ],  [  "name": "DB_NAME",  "value": "demo_app"  ],  [  "name": "ENVIRONMENT",  "value": "dev"  ]  ],  "volumes": [  [  "size": 5,  "name": "root",  "rootVolume": true,  "maxStorage": 0  ]  ],  "ports": [  [  "port": "9090",  "lb": "",  "name": "front"  ]  ],  "config": [  "dockerImage": "tadamhicks/demo_app",  "dockerImageVersion": "latest",  "expose": 8080,  "dockerRegistryId": ""  ],  "plan": [  "code": "container-512",  "id": 70  ]  ]  ]  ],  "Database": [  "linkedTiers": [],  "instances": [  [  "instance": [  "type": "mysql",  "cloud": "AWS Cali",  "layout": [  "code": "mysql-5.7-single",  "id": 87  ],  "expireDays": "1",  "name": "$[userInitials]-demo-$[cloudCode]-$[type]-$[sequence]",  "allowExisting": false,  "shutdownDays": "1"  ],  "planObj": [  "code": "container-128",  "customCores": false,  "coresPerSocket": null,  "hasDatastore": false,  "maxMemory": 134217728,  "customCoresPerSocket": false,  "rootStorageTypes": [],  "addVolumes": false,  "customMaxStorage": false,  "id": 68,  "storageTypes": [  [  "volumeType": "disk",  "code": "standard",  "resizable": false,  "editable": false,  "maxIOPS": null,  "displayOrder": 1,  "deletable": false,  "minStorage": null,  "hasDatastore": true,  "description": "Standard",  "externalId": null,  "customSize": true,  "configurableIOPS": false,  "optionTypes": [],  "enabled": true,  "defaultType": true,  "autoDelete": true,  "name": "Standard",  "id": 1,  "customLabel": true,  "maxStorage": null,  "volumeOptionSource": null,  "minIOPS": null  ]  ],  "value": 68,  "maxStorage": 1073741824,  "supportsAutoDatastore": true,  "memoryOptions": [],  "maxDisks": null,  "coreOptions": [],  "maxDisk": null,  "cpuOptions": [],  "maxCpu": null,  "datastores": [],  "customMaxDataStorage": false,  "minDisk": 1,  "lvmSupported": true,  "customMaxMemory": false,  "noDisks": false,  "autoOptions": null,  "rootCustomSizeOptions": [],  "maxCores": null,  "rootDiskCustomizable": false,  "name": "128MB Memory, 1GB Storage",  "customCpu": false,  "customSizeOptions": [],  "customizeVolume": false  ],  "backup": [  "createBackup": true  ],  "volumes": [  [  "size": 5,  "name": "root",  "rootVolume": true,  "maxStorage": 0  ]  ],  "plan": [  "code": "container-512",  "id": 70  ],  "config": [  "password": "password",  "rootPassword": "password",  "username": "admin"  ],  "deployment": [  "versionId": 61,  "id": 13  ]  ]  ]  ],  "Cache": [  "linkedTiers": [],  "instances": [  [  "instance": [  "type": "redis",  "cloud": "AWS Cali",  "layout": [  "code": "redis-3.0-single",  "id": 530  ],  "expireDays": "1",  "name": "$[userInitials]-demo-$[cloudCode]-$[type]-$[sequence]",  "allowExisting": false,  "shutdownDays": "1"  ],  "planObj": [  "code": "container-128",  "customCores": false,  "coresPerSocket": null,  "hasDatastore": false,  "maxMemory": 134217728,  "customCoresPerSocket": false,  "rootStorageTypes": [],  "addVolumes": false,  "customMaxStorage": false,  "id": 68,  "storageTypes": [  [  "volumeType": "disk",  "code": "standard",  "resizable": false,  "editable": false,  "maxIOPS": null,  "displayOrder": 1,  "deletable": false,  "minStorage": null,  "hasDatastore": true,  "description": "Standard",  "externalId": null,  "customSize": true,  "configurableIOPS": false,  "optionTypes": [],  "enabled": true,  "defaultType": true,  "autoDelete": true,  "name": "Standard",  "id": 1,  "customLabel": true,  "maxStorage": null,  "volumeOptionSource": null,  "minIOPS": null  ]  ],  "value": 68,  "maxStorage": 1073741824,  "supportsAutoDatastore": true,  "memoryOptions": [],  "maxDisks": null,  "coreOptions": [],  "maxDisk": null,  "cpuOptions": [],  "maxCpu": null,  "datastores": [],  "customMaxDataStorage": false,  "minDisk": 1,  "lvmSupported": true,  "customMaxMemory": false,  "noDisks": false,  "autoOptions": null,  "rootCustomSizeOptions": [],  "maxCores": null,  "rootDiskCustomizable": false,  "name": "128MB Memory, 1GB Storage",  "customCpu": false,  "customSizeOptions": [],  "customizeVolume": false  ],  "backup": [  "createBackup": true  ],  "volumes": [  [  "size": 3,  "name": "root",  "rootVolume": true,  "maxStorage": 0  ]  ],  "plan": [  "code": "container-256",  "id": 69  ],  "config": []  ]  ]  ]  ],  "name": "qwdeq",  "description": "3 tier app triggered by source code polling in Jenkins",  "templateImage": "",  "id": 68,  "templateName": "Docker Demo App",  "group": [  "id": 2,  "name": "All Clouds Demo"  ],  "environment": "Staging" ]
        }
    }

}