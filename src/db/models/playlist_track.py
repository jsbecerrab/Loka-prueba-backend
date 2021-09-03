from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Playlist_track(Base):
    __tablename__ = "playlists_tracks"

    id = Column(Integer, primary_key=True, index=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id"))
    track_id = Column(Integer, ForeignKey("tracks.id"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    playlist = relationship("Playlist", back_populates="playlists_tracks")
    track = relationship("Track", back_populates="playlists_tracks")