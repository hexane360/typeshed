# Stubs for requests.api (Python 3)

import sys
from typing import Optional, Union, Any, Iterable, Mapping, MutableMapping, Tuple, IO, Text

from .models import Response

if sys.version_info >= (3,):
    _Text = str
else:
    _Text = Union[str, Text]

_ParamsMappingValueType = Union[_Text, bytes, int, float, Iterable[Union[_Text, bytes, int, float]]]
_Data = Union[
    None,
    _Text,
    bytes,
    MutableMapping[str, Any],
    MutableMapping[Text, Any],
    Iterable[Tuple[_Text, Optional[_Text]]],
    IO
]

def request(method: str, url: str, **kwargs) -> Response: ...
def get(url: Union[_Text, bytes],
        params: Optional[
            Union[Mapping[Union[_Text, bytes, int, float], _ParamsMappingValueType],
                  Union[_Text, bytes],
                  Tuple[Union[_Text, bytes, int, float], _ParamsMappingValueType],
                  Mapping[_Text, _ParamsMappingValueType],
                  Mapping[bytes, _ParamsMappingValueType],
                  Mapping[int, _ParamsMappingValueType],
                  Mapping[float, _ParamsMappingValueType]]] = ...,
        **kwargs) -> Response: ...
def options(url: Union[_Text, bytes], **kwargs) -> Response: ...
def head(url: Union[_Text, bytes], **kwargs) -> Response: ...
def post(url: Union[_Text, bytes], data: _Data = ..., json=..., **kwargs) -> Response: ...
def put(url: Union[_Text, bytes], data: _Data = ..., json=..., **kwargs) -> Response: ...
def patch(url: Union[_Text, bytes], data: _Data = ..., json=..., **kwargs) -> Response: ...
def delete(url: Union[_Text, bytes], **kwargs) -> Response: ...
