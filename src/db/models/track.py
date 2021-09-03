from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Track(Base):
  __tablename__ = "tracks"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  popularity = Column(Integer)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime)

  albums_tracks = relationship("Album_track", back_populates="track")
  artists_tracks = relationship("Artist_track", back_populates="track")
  playlists_tracks = relationship("Playlist_track", back_populates="track")