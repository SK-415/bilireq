import os
import subprocess
from pathlib import Path


os.chdir(Path(__file__).parent.absolute() / "protos")


for file_path in Path(".").rglob("*.proto"):
    if file_path.is_file():
        subprocess.run(
            [
                "python",
                "-m",
                "grpc_tools.protoc",
                "-I=.",
                "--python_out=.",
                "--grpc_python_out=.",
                "--mypy_out=.",
                str(file_path),
            ],
            shell=True,
        )
