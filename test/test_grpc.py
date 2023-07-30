import asyncio
import sys
from pathlib import Path
from pprint import pprint
from gzip import decompress
from .test_data import AUTH as auth
from bilireq.grpc.protos.bilibili.app.dynamic.v2.dynamic_pb2 import (
    DynDetailReq,
)

# sys.path.append(str(Path(__file__).parent.parent))

from bilireq.grpc.dynamic import (  # noqa
    grpc_get_followed_dynamic_users,
    grpc_get_followed_dynamics,
    grpc_get_user_dynamics,
    grpc_get_dynamic_details,
    grpc_get_dynamic_detail,
)

# req_bin = Path("test/http_pack/request_body.bin").read_bytes()
# resp_bin = Path("test/http_pack/response_body.bin").read_bytes()

# greq = DynDetailReq()
# dreq = decompress(req_bin[5:])
# greq.ParseFromString(dreq)
# print(greq)
# exit()


async def main():
    # await auth.refresh()
    # dynamics = await grpc_get_user_dynamics(uid=491589125, auth=auth)
    # dynamics = await grpc_get_followed_dynamics(auth=auth)
    # pprint(dynamics.dynamic_list.list[0].modules[0].module_author.author.name)
    # pprint(await grpc_get_followed_dynamic_users(auth=auth))
    pprint(
        (
            await grpc_get_dynamic_detail(
                dynamic_id="824093109029699590",
                # auth=auth,
            )
        )
    )
    # print(type(dynamics))
    # for dynamic in dynamics.list:
    #     print(type(dynamic))

    # import json

    # with open("dynamics.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(MessageToDict(dynamics), ensure_ascii=False, indent=4))


asyncio.run(main())
