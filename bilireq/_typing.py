from typing import TYPE_CHECKING, Any, Dict, Mapping, Optional, Union

if TYPE_CHECKING:
    from .auth import Auth, WebAuth

T_Auth = Union[Mapping[str, Any], "Auth", "WebAuth", None]
