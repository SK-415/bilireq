import asyncio

from bilireq.login import Login

PHONE_NUM = 1
PASSWD = 1


async def main():
    print("===== 二维码登录 =====")
    login = Login()
    image = await login.get_qrcode()
    image.show()  # type: ignore
    await login.qrcode_login(interval=5)

    # print("===== 验证码登录 =====") # 不可用
    # login = Login()
    # await login.send_sms(PHONE_NUM)
    # await login.sms_login(input("请输入验证码: "))

    # print("==== 账号密码登录 ====") # 不可用
    # login = Login()
    # await login.pwd_login(str(PHONE_NUM), PASSWD)


asyncio.run(main())
