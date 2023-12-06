from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    Float,
    Text,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Youtuber(Base):
    __tablename__ = "youtubers"
    channel_name = Column(String(50), primary_key=True)
    channel_link = Column(String(50))
    channel_startdate = Column(Date)
    totalviews_in_10K = Column(Float)
    subscribers_in_10K = Column(Float)
    location = Column(String(50))
    other_links = Column(Text)
    videos_links = Column(Text)

    video = relationship("Video", back_populates="youtuber")


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    channel_name = Column(
        String(50), ForeignKey("youtubers.channel_name"), nullable=False
    )
    video_title = Column(Text)
    views = Column(Integer)
    comments = Column(Integer)
    duration_in_sec = Column(Integer)
    likes = Column(Integer)
    publish_date = Column(Date)
    category = Column(Text)
    sensationalism_score = Column(Integer)

    youtuber = relationship("Youtuber", back_populates="video")


engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/socialmedia?charset=utf8mb4", echo=True
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
