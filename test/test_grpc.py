import asyncio
import sys
from pathlib import Path
from pprint import pprint

sys.path.append(str(Path(__file__).parent.parent))

from bilireq.grpc.dynamic import grpc_get_user_dynamics  # noqa


async def main():
    dynamics = await grpc_get_user_dynamics(uid=491589125, to_dict=True)
    pprint(dynamics)
    # print(type(dynamics))
    # for dynamic in dynamics.list:
    #     print(type(dynamic))

    # import json

    # with open("dynamics.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(MessageToDict(dynamics), ensure_ascii=False, indent=4))


asyncio.run(main())
