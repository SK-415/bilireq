import asyncio
import sys
from pathlib import Path
from pprint import pprint

from test_data import AUTH as auth

sys.path.append(str(Path(__file__).parent.parent))

from bilireq.grpc.dynamic import (  # noqa
    grpc_get_followed_dynamic_users,
    grpc_get_followed_dynamics,
    grpc_get_user_dynamics,
)
from bilireq.grpc.live import grpc_get_room_info


async def main():
    dynamics = await grpc_get_user_dynamics(uid=491589125, to_dict=True)
    # dynamics = await grpc_get_followed_dynamics(auth=auth, to_dict=True)
    pprint(dynamics)
    # pprint(await grpc_get_followed_dynamic_users(auth=auth, to_dict=True))
    # pprint(await grpc_get_room_info(room_id=1234, to_dict=True))
    # print(type(dynamics))
    # for dynamic in dynamics.list:
    #     print(type(dynamic))

    # import json

    # with open("dynamics.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(MessageToDict(dynamics), ensure_ascii=False, indent=4))


asyncio.run(main())
