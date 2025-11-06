from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from litestar_offers.app import models


class OfferWallOfferRepository(SQLAlchemyAsyncRepository[models.OfferWallOffer]):
    model_type = models.Deck


class OfferWallOfferService(SQLAlchemyAsyncRepositoryService[models.OfferWallOffer]):
    repository_type = OfferWallOfferRepository


class OfferWallRepository(SQLAlchemyAsyncRepository[models.OfferWall]):
    model_type = models.OfferWall


class OfferWallService(SQLAlchemyAsyncRepositoryService[models.OfferWall]):
    repository_type = OfferWallRepository


class OfferRepository(SQLAlchemyAsyncRepository[models.Offer]):
    model_type = models.Offer


class OfferService(SQLAlchemyAsyncRepositoryService[models.Offer]):
    repository_type = OfferRepository