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

    stage('Provision App') {
        /*
         *
         *  */
        String morpheusUrl = 'https://demo.morpheusdata.com/api/apps'
        String postBody = '{ "image": "/assets/apps/template.png", "tiers": { "App": { "linkedTiers": [ "Cache", "Database" ], "tier": { "bootOrder": 1, "lockedFields": [ "bootOrder" ] }, "instances": [ { "instance": { "type": "docker" }, "environments": { "Dev": { "groups": { "All Clouds Demo": { "clouds": { "Labs UCS": { "backup": { "createBackup": true }, "instance": { "layout": { "code": "docker-1.7-single", "id": 206 }, "expireDays": "1", "name": "wun", "allowExisting": true }, "evars": [ { "name": "DB_NAME", "value": "demo_app" }, { "name": "WORDNIK_API_KEY", "value": "5455816781cb799cf994f0b58cc027cb0dd2633addcdd2025" } ], "volumes": [ { "size": 5, "name": "root", "rootVolume": true } ], "ports": [ { "port": "9090", "lb": "", "name": "front" } ], "config": { "configVolume": "", "dockerImage": "tadamhicks/demo_app", "dataVolume": "", "dockerImageVersion": "latest", "logVolume": "", "expose": 8080, "dockerRegistryId": "" }, "plan": { "code": "container-512", "id": 70 } } } } } } } } ] }, "Database": { "linkedTiers": [], "instances": [ { "instance": { "type": "mysql" }, "environments": { "Dev": { "groups": { "All Clouds Demo": { "clouds": { "Labs UCS": { "backup": { "createBackup": true }, "instance": { "layout": { "code": "mysql-5.7-single", "id": 87 }, "expireDays": "1", "name": "too", "allowExisting": true }, "volumes": [ { "size": 5, "name": "root", "rootVolume": true } ], "plan": { "code": "container-512", "id": 70 }, "config": { "password": "************", "rootPassword": "************", "username": "admin" }, "deployment": { "versionId": 61, "id": 13 } } } } } } } } ] }, "Cache": { "linkedTiers": [], "instances": [ { "instance": { "type": "redis" }, "environments": { "Dev": { "groups": { "All Clouds Demo": { "clouds": { "Labs UCS": { "backup": { "createBackup": true }, "instance": { "layout": { "code": "redis-3.2-single", "id": 666 }, "expireDays": "1", "name": "free", "allowExisting": true }, "volumes": [ { "size": 3, "name": "root", "rootVolume": true } ], "plan": { "code": "container-256", "id": 69 }, "config": {} } } } } } } } ] } }, "name": "A_D_A" }'

        String headering = 'Authorization: BEARER 9e683c25-6260-4b37-be65-0b06a54214e8'

        sh "curl -X POST -d \"${postBody}\" -H \"${headering}\" ${morpheusUrl}"

    }
}