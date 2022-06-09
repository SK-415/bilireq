class ResponseCodeError(Exception):
    """请求返回 code 不为 0"""

    def __init__(self, code: int, msg: str, data: dict):
        self.code = code
        self.msg = msg
        self.data = data

    def __repr__(self) -> str:
        return f"错误码: {self.code}, 信息: {self.msg}"

    def __str__(self) -> str:
        return self.__repr__()


class AuthParamError(Exception):
    """缺少必要鉴权参数"""

    def __init__(self, *params: str):
        self.params = params

    def __repr__(self) -> str:
        return f"缺少鉴权参数 {', '.join(self.params)}"

    def __str__(self) -> str:
        return self.__repr__()


class AuthTypeError(Exception):
    """鉴权类型错误"""

    def __init__(self, auth_type: str):
        self.auth_type = auth_type

    def __repr__(self) -> str:
        return f"'{self.auth_type}' 是当前不支持的鉴权类型"

    def __str__(self) -> str:
        return self.__repr__()


class GrpcError(Exception):
    """RPC 错误"""

    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg

    def __repr__(self) -> str:
        return f"错误码: {self.code}, 信息: {self.msg}"

    def __str__(self) -> str:
        return self.__repr__()


if __name__ == "__main__":
    raise ValueError("test")
    raise AuthParamError("hehe", "heihei", "233")
