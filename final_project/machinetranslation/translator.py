"""IBM Watson Language Translation Service"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']


authenticator = IAMAuthenticator(API_KEY)
# translator_instance
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

#The response type for listing supported languages.
#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

def english_to_french(english_text):
    """English to French"""
    #write the code here
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    print(french_text)
    return french_text


def french_to_english(french_text):
    """French to English"""
    #write the code here
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    print(english_text)
    return english_text

