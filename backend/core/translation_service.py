from typing import Optional, Dict
from google.cloud import translate_v2 as translate
from google.cloud import speech
import os
from fastapi import UploadFile
import io
import logging

class TranslationService:
    def __init__(self):
        self.translate_client = translate.Client()
        self.speech_client = speech.SpeechClient()
        self.logger = logging.getLogger(__name__)

    async def translate_text(...