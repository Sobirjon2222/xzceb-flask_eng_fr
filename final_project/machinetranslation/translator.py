import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('tDe9JIsgrqq-3CfzfTQpwnmZaK-u1licGqdupD3h5tFi')
language_translator = LanguageTranslatorV3(
    version='2022-12-23',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/8a3ea532-e753-4b4a-9d5f-80e9c83e7626")

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    '''translation from english to french'''
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    #print(json.dumps(french_text, indent=2, ensure_ascii=False))
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    '''translation from french to english'''
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    #print(json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text["translations"][0]["translation"]