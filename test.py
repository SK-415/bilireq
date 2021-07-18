import asyncio
from biliapi import get
from biliapi.dynamic import get_user_dynamics
from biliapi.live import get_rooms_info, get_room_info
from biliapi.user import get_user_info


async def main():
    uid = 10352806
    # print(await get_user_dynamics(10352806))
    # print(await get_rooms_info(['1','2','3','4','5']))
    # print(await get_room_info(10352806))
    print(await get_user_info(str(uid)))

asyncio.run(main())