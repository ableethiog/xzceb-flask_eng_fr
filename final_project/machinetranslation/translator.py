''' import required modules '''
import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


''' Translator instance '''
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))


def english_to_french(text1):
    ''' function to translate a text from English to French '''
    frenchtranslation = language_translator.translate(
        text=text1,
        model_id='en-fr'
    ).get_result()

    # Extract the translated text from the response
    return frenchtranslation.get('translations')[0].get('translation')

def french_to_english(text1):
    ''' function to translate the text from French to English '''
    englishtranslation = language_translator.translate(
    text=text1,
    model_id='fr-en'
    ).get_result()

    # Extract the translated text from the response
    return englishtranslation.get('translations')[0].get('translation')



