import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="gist2html")
def gist2Html(req: func.HttpRequest) -> func.HttpResponse:
    functionUrl = req.url[:req.url.rfind("gist2html")]
    gistId = req.params.get('gistId')
    url = f'https://api.github.com/gists/{gistId}'

    if gistId:
        response = requests.get(url)
        responseData = response.json()
        files = responseData['files']
        rawUrl = files['index.html']['raw_url']
        indexFile = requests.get(rawUrl).text
        for key, value in files.items():
            if key != 'index.html':
                loopRawUrl = value['raw_url']
                encodedLoopRawUrl = requests.utils.quote(loopRawUrl, safe='')
                indexFile = indexFile.replace(key, functionUrl + "rawfile2html?url=" + encodedLoopRawUrl)

    return func.HttpResponse(
        indexFile,
        mimetype="text/html",
        charset="utf-8",
        status_code=200
    )

#Since the gist raw_url returns with the mime type of "text/plain", browsers won't read it as JS nor CSS
#Now "text/html" seems to be good enough for Chrome :D
@app.route(route="rawfile2html")
def rawFile2Html(req: func.HttpRequest) -> func.HttpResponse:
    raw_url = req.params.get('url')
    indexFile = requests.get(raw_url).text
    return func.HttpResponse(
        indexFile,
        mimetype="text/html",
        charset="utf-8",
        status_code=200
    )