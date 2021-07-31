import asyncio

from test_data import UID, PHONE, USERNAME, PASSWORD, ACCESS_TOKEN, REFRESH_TOKEN
from biliapi.dynamic import get_user_dynamics
from biliapi.login import Login, refresh_token, get_token_info
from biliapi.user import get_user_info


async def main():
    # 登录相关测试
    # print(await test_qrcode_login())
    # print(await test_sms_login())
    # print(await test_pwd_login())
    # await test_pwd_login_duration()
    # print(await refresh_token(access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN))
    print(await get_token_info(access_token=ACCESS_TOKEN))

    # print(await get_user_dynamics(UID))
    # print(await get_rooms_info(room_ids=[1,2]))
    # print(await get_room_info(UID))
    # print(await get_user_info(str(UID)))


async def test_qrcode_login():
    login = Login()
    await login.get_qrcode(print_=True)
    return await login.qrcode_login(retry=-1)


async def test_sms_login():
    login = Login()
    await login.send_sms(tel=PHONE)
    while True:
        try:
            return await login.sms_login(input())
        except Exception as e:
            print(e)


async def test_pwd_login():
    login = Login()
    return await login.pwd_login(USERNAME, PASSWORD)

async def test_pwd_login_duration():
    from datetime import datetime
    print(datetime.now())
    while True:
        try:
            print(await test_pwd_login())
            print(datetime.now())
            break
        except Exception as e:
            print(e)
        await asyncio.sleep(10)
        


asyncio.run(main())
