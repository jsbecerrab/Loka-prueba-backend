from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


from ..database import Base

class Album(Base):
  __tablename__ = "albums"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  release_date = Column(DateTime, nullable=False)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime)

  albums_tracks = relationship("Album_track", back_populates="album")
  artists_albums = relationship("Artist_album", back_populates="album")