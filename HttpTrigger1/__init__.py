import logging

from matplotlib.style import library
from library import learn
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    learn.main()
    return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
    )
