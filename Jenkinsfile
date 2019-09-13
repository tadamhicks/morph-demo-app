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

            Map<?, ?> postBody = [
"id": 1,
  "templateName": "Spud Marketing",
  "defaultCluster": null,
  "defaultPool": null,
  "name": "jera-demo",
  "group": [
    "id": 2,
    "name": "Demo"
  ],
  "tiers": [
    "Web": [
      "instances": [
        [
          "instance": [
            "cloud": "AWS",
            "type": "tomcat"
          ],
          "config": []
        ]
      ],
      "tierIndex": 0
    ],
    "Database": [
      "instances": [
        [
          "instance": [
            "cloud": "AWS",
            "type": "mysql"
          ],
          "config": []
        ]
      ],
      "tierIndex": 1
    ]
  ]
]


            echo morpheusApp.buildApp(morpheusUrl, postBody, "${bearer}")
        }
    }


}