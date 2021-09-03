from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    spotify_id = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    followers = Column(Integer)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    playlists = relationship("Playlist", back_populates="owner")