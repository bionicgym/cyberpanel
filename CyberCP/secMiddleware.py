from django.conf import settings
from django.shortcuts import HttpResponse
from plogical.CyberCPLogFileWriter import CyberCPLogFileWriter as logging
import json

class secMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            if request.body.find(';') > -1 or request.body.find('&&') > -1 or request.body.find('|') > -1 or request.body.find('...') > -1:
                logging.writeToFile('Bad Input on.')
        response = self.get_response(request)
        return response

    #def __call__(self, request):
    #    if request.method == 'POST':
    #        data = json.loads(request.body)
    #        for key, value in data.iteritems():
    #            if value.find(';') > -1 or value.find('&&') > -1 or value.find('|') > -1 or value.find('...') > -1:
    #                logging.writeToFile(request.body)
    #                return HttpResponse('Error')
    #            if key.find(';') > -1 or key.find('&&') > -1 or key.find('|') > -1 or key.find('...') > -1:
    #                logging.writeToFile(request.body)
    #                return HttpResponse('Error')
    #    response = self.get_response(request)
    #    return response