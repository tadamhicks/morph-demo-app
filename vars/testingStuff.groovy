import org.incognitjoe.JenkinsHttpClient

def print_ghibli_films() {
    JenkinsHttpClient http = new JenkinsHttpClient()
    println(http.get('https://ghibliapi.herokuapp.com/films/'))
}

def notifySlack(String slackHookUrl, String postBody) {
    JenkinsHttpClient http = new JenkinsHttpClient()
    http.postJson(slackHookUrl, postBody)
}