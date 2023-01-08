import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('9NeWuGjZ4gD7Hc7Rv44ai95nH1j11wuivrIinXcmGxT2')
language_translator = LanguageTranslatorV3(
    version='2022-12-23',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/8a3ea532-e753-4b4a-9d5f-80e9c83e7626")


def english_to_french(english_text):
   translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
   french_text=translation ["translations"][0]["translation"]
   return french_text
   
def french_to_english(french_text):
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = translation ["translations"][0]["translation"]
    return english_text 