"""Módulo de inicialização dos schemas"""

from schemas.mobile import MobileSchema, MobileViewSchema, MobileBuscaSchema, ListaMobileSchema
from schemas.mobile import MobileDelSchema, MobilePriceRangeSchema
from schemas.mobile import apresenta_mobile, apresenta_mobiles, retorna_price_range

from schemas.error import ErrorSchema
