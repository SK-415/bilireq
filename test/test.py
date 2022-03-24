import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from bilireq.auth import Auth
from bilireq.dynamic import get_user_dynamics, get_followed_dynamics_update_info, get_followed_new_dynamics, get_followed_history_dynamics
from bilireq.live import get_rooms_info_by_ids
from bilireq.login import Login, get_token_info, refresh_token
from bilireq.user import get_user_info

from test_data import AUTH, PASSWORD, PHONE, UID, USERNAME


async def main():
    pass
    # 登录相关测试
    # auth = Auth()
    # print(auth.get_cookies(), auth.get_tokens(), auth["access_token"])
    # auth = Auth(AUTH)
    # print(await auth.get_info())
    print(await test_qrcode_login())
    # print(await test_sms_login())
    # print(await test_pwd_login())
    # await test_pwd_login_duration()
    # print(await refresh_token(access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN))
    # print(await get_token_info(auth))

    # print(await get_user_dynamics(UID))
    # print(await get_followed_new_dynamics(auth=auth, reqtype="app"))
    # print(await get_followed_dynamics_update_info(auth=auth))
    # print(await get_followed_history_dynamics(578888250640167815, auth=auth))
    # print(await get_rooms_info_by_ids(room_ids=[1,2], auth=auth, reqtype="app"))
    # print(await get_room_info(UID))
    # print(await get_user_info(str(UID)))
    # print(await get_user_info(20709866, auth=auth, reqtype="app"))
    # print(await get_user_info(20709866, auth=auth, reqtype="web"))


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
