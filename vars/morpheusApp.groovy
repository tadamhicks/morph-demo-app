import org.incognitojoe.JenkinsHttpClient

def buildApp(String morpheusUrl, String postBody, String headering) {
        JenkinsHttpClient http = new JenkinsHttpClient()
        http.postJson(morpheusUrl, postBody, headering)
}