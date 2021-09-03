from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Album_track(Base):
    __tablename__ = "albums_tracks"

    id = Column(Integer, primary_key=True, index=True)
    albums_id = Column(Integer, ForeignKey("albums.id"))
    track_id = Column(Integer, ForeignKey("tracks.id"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    album = relationship("Album", back_populates="albums_tracks")
    track = relationship("Track", back_populates="albums_tracks")