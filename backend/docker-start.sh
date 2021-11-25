#!/bin/bash

pip install --upgrade pip
pip install -r requirements.txt

if [[ "$DEBUG" = true ]]; then
    pip install debugpy
    python -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --reload --host 0.0.0.0
else
    uvicorn app.main:app --reload --host 0.0.0.0
fi