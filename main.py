from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session 
from database import engine, get_db
import models
import schemas
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Players API")

@app.get("/")
def home():
    return {"message": "Players API"}

@app.post("/players", response_model=schemas.PlayerResponse)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    existing = crud.get_player_by_nick(db, player.nick)
    if existing:
        raise HTTPException(400, f"Игрок с ником '{player.nick}' уже существует")
    
    return crud.create_player(db, player)

@app.get("/players")
def get_all_players(db: Session = Depends(get_db)):
    players = crud.get_all_players(db)
    return {"players": players}

@app.get("/players/{nick}", response_model=schemas.PlayerResponse)
def get_player_by_nick(nick: str, db: Session = Depends(get_db)):
    player = crud.get_player_by_nick(db, nick)
    if not player:
        raise HTTPException(404, f"Игрок с ником '{nick}' не найден")
    return player

@app.put("/players/{nick}", response_model=schemas.PlayerResponse)
def update_player(nick: str, update: schemas.PlayerUpdate, db: Session = Depends(get_db)):
    player = crud.update_player(db, nick, update)
    if not player:
        raise HTTPException(404, f"Игрок с ником '{nick}' не найден")
    return player

@app.delete("/players/{nick}")
def delete_player(nick: str, db: Session = Depends(get_db)):
    deleted = crud.delete_player(db, nick)
    if not deleted:
        raise HTTPException(404, f"Игрок с ником '{nick}' не найден")
    return {"message": f"Игрок '{nick}' удален"}