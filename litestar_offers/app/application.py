import dataclasses

import litestar
import modern_di_litestar
from advanced_alchemy.exceptions import DuplicateKeyError
from lite_bootstrap import LitestarBootstrapper
from litestar.config.app import AppConfig
from opentelemetry.instrumentation.asyncpg import AsyncPGInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

from litestar_offers.app import exceptions, ioc
from litestar_offers.app.api.routs import ROUTER
from litestar_offers.app.settings import settings


def build_app() -> litestar.Litestar:
    bootstrap_config = dataclasses.replace(
        settings.api_bootstrapper_config,
        application_config=AppConfig(
            exception_handlers={
                DuplicateKeyError: exceptions.duplicate_key_error_handler,
            },
            route_handlers=[ROUTER],
            plugins=[modern_di_litestar.ModernDIPlugin()],
            dependencies={
                "offer_wall_offer_service": modern_di_litestar.FromDI(ioc.Dependencies.offer_wall_offer_service),
                "offer_wall_service": modern_di_litestar.FromDI(ioc.Dependencies.offer_wall_service),
                "offer_service": modern_di_litestar.FromDI(ioc.Dependencies.offer_service),
            },
            request_max_body_size=settings.request_max_body_size,
        ),
        opentelemetry_instrumentors=[
            SQLAlchemyInstrumentor(),
            AsyncPGInstrumentor(capture_parameters=True),  # type: ignore[no-untyped-call]
        ],
    )
    bootstrapper = LitestarBootstrapper(bootstrap_config=bootstrap_config)
    return bootstrapper.bootstrap()