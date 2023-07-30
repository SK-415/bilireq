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
            # shell=True,
        )

    for file_path in [
        file_path.with_name(f"{file_path.stem}_pb2_grpc.py"),
        file_path.with_name(f"{file_path.stem}_pb2.py"),
        file_path.with_name(f"{file_path.stem}_pb2.pyi"),
    ]:
        if file_path.is_file():
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open(file_path, "w", encoding="utf-8") as f:
                for line in lines:
                    if line.startswith("from bilibili."):
                        line = line.replace(
                            "from bilibili.", "from bilireq.grpc.protos.bilibili."
                        )
                    elif line.startswith("import bilibili."):
                        line = line.replace(
                            "import bilibili.", "import bilireq.grpc.protos.bilibili."
                        )
                    elif line.startswith("from pgc."):
                        line = line.replace("from pgc.", "from bilireq.grpc.protos.pgc.")
                    elif line.startswith("import pgc."):
                        line = line.replace("import pgc.", "import bilireq.grpc.protos.pgc.")
                    elif "-> bilibili" in line:
                        line = line.replace("-> bilibili", "-> bilireq.grpc.protos.bilibili")
                    elif ": bilibili" in line:
                        line = line.replace(": bilibili", ": bilireq.grpc.protos.bilibili")
                    f.write(line)
