from __future__ import annotations

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Manager(Base):
    __tablename__ = "manager"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    last_name: Mapped[str]


class Season(Base):
    __tablename__ = "season"

    year: Mapped[int] = mapped_column(Integer, primary_key=True)

    weeks: Mapped[list[Week]] = relationship("Week", back_populates="season")
    teams: Mapped[list[Team]] = relationship("Team", back_populates="season")


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    season_year: Mapped[int] = mapped_column(ForeignKey("season.year"))
    manager_id: Mapped[int] = mapped_column(ForeignKey("manager.id"))

    season: Mapped[Season] = relationship("Season", back_populates="teams")
    manager: Mapped[Manager] = relationship("Manager", back_populates="teams")
    weekly_rosters: Mapped[list[WeeklyRoster]] = relationship(
        "WeeklyRoster", back_populates="team"
    )


class Week(Base):
    __tablename__ = "week"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    num: Mapped[int] = mapped_column(Integer)
    season_year: Mapped[int] = mapped_column(ForeignKey("season.year"))

    season: Mapped[Season] = relationship("Season", back_populates="weeks")
    rosters: Mapped[WeeklyRoster] = relationship("WeeklyRoster", back_populates="week")


class Matchup(Base):
    __tablename__ = "matchup"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    rosters: Mapped[WeeklyRoster] = relationship(
        "WeeklyRoster", back_populates="matchup"
    )


class WeeklyRoster(Base):
    __tablename__ = "roster"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    matchup_id: Mapped[int] = mapped_column(ForeignKey("matchup.id"))

    team = relationship("Team", back_populates="weekly_rosters")
    week = relationship("Week", back_populates="rosters")
    matchup = relationship("Matchup", back_populates="rosters")
    scores = relationship("PlayerScore", back_populates="roster")

    # Could be dynamically computed:
    #  total_points: Mapped[float]
    #  matchup_win: Mapped[bool]
    #  median_win: Mapped[bool]


class Player(Base):
    __tablename__ = "player"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    position: Mapped[str]  # TODO: Enum or something

    scores = relationship("PlayerScore", back_populates="player")


class PlayerScore(Base):
    __tablename__ = "player_score"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    roster_id: Mapped[int] = mapped_column(ForeignKey("roster.id"))

    player: Mapped[Player] = relationship("Player", back_populates="scores")
    roster: Mapped[WeeklyRoster] = relationship("WeeklyRoster", back_populates="scores")

    score: Mapped[float]
    starter: Mapped[bool]
