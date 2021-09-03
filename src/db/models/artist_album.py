from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Artist_album(Base):
    __tablename__ = "artists_albums"

    id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    artist = relationship("Artist", back_populates="artists_albums")
    album = relationship("Album", back_populates="artists_albums")