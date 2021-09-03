from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Artist_track(Base):
    __tablename__ = "artists_tracks"

    id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    track_id = Column(Integer, ForeignKey("tracks.id"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    artist = relationship("Artist", back_populates="artists_tracks")
    track = relationship("Track", back_populates="artists_tracks")