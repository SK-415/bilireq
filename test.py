import asyncio
from biliapi import get
from biliapi.dynamic import get_user_dynamics
# from biliapi.live import get_rooms_info, get_room_info
from biliapi.user import get_user_info
from biliapi.login import Login, sms_login


async def main():
    uid = 10352806
    # print(await test_qrcode_login())
    print(await test_sms_login())
    # print(await sms_login(12345, tel=1821717724, captcha_key="54e1195e9b6d95ca85d7e04b6d385392"))
    # print(await get_user_dynamics(uid))
    # print(await get_rooms_info(room_ids=[1,2]))
    # print(await get_room_info(10352806))
    # print(await get_user_info(str(uid)))


async def test_qrcode_login():
    login = Login()
    await login.get_qrcode(print_=True)
    return await login.qrcode_login(retry=-1)


async def test_sms_login():
    login = Login()
    await login.send_sms(tel='')
    while True:
        try:
            return await login.sms_login(input())
        except Exception as e:
            print(e)


asyncio.run(main())