import azure.functions as func
import logging
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="gist2html")
def gist2html(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    url = f'https://api.github.com/gists/{name}'
    if name:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
        session = requests.Session()
        response = requests.get(url)
        responseData = response.json()
        raw_url = responseData['files']['index.html']['raw_url']
        indexFile = requests.get(raw_url).text
        return func.HttpResponse(
            indexFile,
            mimetype="text/html",
            charset="utf-8",
            status_code=200
        )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )