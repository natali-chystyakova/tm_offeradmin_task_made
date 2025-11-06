import typing

import sqlalchemy as sa
from advanced_alchemy.base import BigIntAuditBase, orm_registry
from sqlalchemy import orm



import uuid
from sqlalchemy import (
    Column, String, Integer, Boolean, Text, ForeignKey, UniqueConstraint, Index
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from litestar_offers.app.resources.db import Base

from sqlalchemy import Table

METADATA: typing.Final = orm_registry.metadata
orm.DeclarativeBase.metadata = METADATA

# junction table with order
class OfferWallOffer(Base):
    __tablename__ = "offer_wall_offer"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    offer_wall_token = Column(UUID(as_uuid=True), ForeignKey("offer_wall.token"), nullable=False)
    offer_uuid = Column(UUID(as_uuid=True), ForeignKey("offer.uuid"), nullable=False)
    order = Column(Integer, default=0)

    # constrain uniqueness
    __table_args__ = (UniqueConstraint("offer_wall_token", "offer_uuid", name="uix_wall_offer"),)

class OfferWall(Base):
    __tablename__ = "offer_wall"
    token = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=True)
    url = Column(String(1024), nullable=True, index=True)
    description = Column(Text, nullable=True)

    # relationship to OfferWallOffer for ordering
    offer_assignments = relationship("OfferWallOffer", backref="offer_wall", cascade="all, delete-orphan")

class Offer(Base):
    __tablename__ = "offer"
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(Integer, nullable=False)  # non-PK id (как в Django-модели)
    url = Column(String(1024), nullable=True)
    is_active = Column(Boolean, default=True)
    name = Column(String(255), unique=True, nullable=False)
    sum_to = Column(String(100), nullable=True)
    term_to = Column(Integer, nullable=True)
    percent_rate = Column(Integer, nullable=True)