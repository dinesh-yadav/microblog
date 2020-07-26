import json
import uuid
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    '''auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    r = requests.post('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(source_language,dest_language),headers=auth,json={'Text':text})
    print(r.status_code)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))'''

    subscription_key = app.config['MS_TRANSLATOR_KEY']
    endpoint = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = f'&to={dest_language}'
    constructed_url = endpoint + path + params
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        "Ocp-Apim-Subscription-Region":'centralindia',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }
    body = [{'text': text}]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']
