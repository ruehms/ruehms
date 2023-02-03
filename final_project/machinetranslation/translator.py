"name is Rana Shiba , language translator code"
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
os.environ['apikey']="CkcNvAQ-8duNJ84bEO-PVfUqDyDYkbzpf9eFzChbuJ91"
os.environ['url'] = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/0294fdf6-53d6-41fb-b9a4-07ccfc225d49"
apikey = os.getenv("apikey")
url = os.getenv("url")

"""The below authenticates to the IBM Watson service and initiates an instance"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/0294fdf6-53d6-41fb-b9a4-07ccfc225d49")
#language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """code translates from en to fr / Rana Shiba"""
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']

    return french_text
  
def french_to_english(french_text):
    """ code translator from fr to en / Rana Shiba"""
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
