from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import json
import os

app = FastAPI(title="Beacon Alert API")

class Beacon(BaseModel):
    nome: str
    mensagem: str

BEACONS_FILE = "metavision/beacons.json"

def carregar_beacons() -> Dict[str, Beacon]:
    if not os.path.exists(BEACONS_FILE):
        return {}
    with open(BEACONS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return {mac: Beacon(**info) for mac, info in data.items()}

beacons_db: Dict[str, Beacon] = carregar_beacons()

@app.get("/api/beacons", response_model=Dict[str, Beacon])
def listar_beacons():
    return beacons_db

@app.get("/api/beacons/{mac}", response_model=Beacon)
def obter_beacon(mac: str):
    beacon = beacons_db.get(mac.upper())
    if not beacon:
        raise HTTPException(status_code=404, detail="Beacon não encontrado")
    return beacon
