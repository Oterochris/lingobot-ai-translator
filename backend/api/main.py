from fastapi import FastAPI, HTTPException, File, UploadFile, Depends
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from core.translation_service import TranslationService, TranslationError

app = FastAPI(title="LingoBot API", version="1.0.0")...