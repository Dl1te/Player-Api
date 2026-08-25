from sqlalchemy.orm import Session
import models, schemas

def get_player_by_nick(db: Session, nick: str):
    return db.query(models.Player).filter(models.Player.nick == nick).first()

def get_all_players(db: Session):
    return db.query(models.Player).all()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(
        nick=player.nick,
        name=player.name,
        donate=player.donate
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(db: Session, nick: str, update: schemas.PlayerUpdate):
    player = get_player_by_nick(db, nick)
    if not player:
        return None
    
    if update.name is not None:
        player.name = update.name
    if update.donate is not None:
        player.donate = update.donate
    
    db.commit()
    db.refresh(player)
    return player

def delete_player(db: Session, nick: str):
    player = get_player_by_nick(db, nick)
    if not player:
        return False
    
    db.delete(player)
    db.commit()
    return True