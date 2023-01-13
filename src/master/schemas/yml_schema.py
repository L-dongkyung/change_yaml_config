from typing import Union

from pydantic import BaseModel


class UpdateYml(BaseModel):
    path: str
    data: Union[str, list]
    is_str: bool = False
