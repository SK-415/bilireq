class ResponseCodeException(Exception):
    """请求返回 code 不为 0"""

    def __init__(self, code: int, msg: str, data: dict):
        self.code = code
        self.msg = msg
        self.data = data

    def __repr__(self) -> str:
        return f"<ResponseCodeException code={self.code} message={self.msg}>"
    
    def __str__(self) -> str:
        return self.__repr__()