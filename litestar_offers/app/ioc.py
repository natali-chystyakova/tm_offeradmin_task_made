from modern_di import BaseGraph, Scope, providers

from litestar_offers.app import repositories
from litestar_offers.app.resources.db import create_sa_engine, create_session


class Dependencies(BaseGraph):
    database_engine = providers.Resource(Scope.APP, create_sa_engine)
    session = providers.Resource(Scope.REQUEST, create_session, engine=database_engine.cast)

    offer_wall_offer_service = providers.Factory(Scope.REQUEST, repositories.OfferWallOfferService, session=session.cast, auto_commit=True)
    offer_wall_service = providers.Factory(Scope.REQUEST, repositories.OfferWallService, session=session.cast, auto_commit=True)
    offer_service = providers.Factory(Scope.REQUEST, repositories.OfferService, session=session.cast,
                                      auto_commit=True)