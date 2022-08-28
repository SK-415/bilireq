import sys
from pathlib import Path

# from .login import Login
from .utils import get, post  # noqa

sys.path.append(str(Path(__file__).absolute().parent / "grpc" / "protos"))
