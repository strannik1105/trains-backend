from common.db.base_model import BaseModel

# include models here

from models.users.user import User  # noqa
from models.stations import Station, Route  # noqa

metadata = BaseModel.metadata
