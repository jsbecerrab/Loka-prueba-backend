from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Artist(Base):
  __tablename__ = "artists"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  popularity = Column(Integer)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime)

  artists_albums = relationship("Artist_album", back_populates="artist")
  artists_tracks = relationship("Artist_track", back_populates="artist")
