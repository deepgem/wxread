# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认40次/20分钟
READ_NUM = int(os.getenv('READ_NUM') or 40)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# SeverChan推送时需填
SERVERCHAN_SPT = "" or os.getenv("SERVERCHAN_SPT")


# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'RK': 'oxEY1bTnXf',
    'ptcz': '53e3b35a9486dd63c4d06430b05aa169402117fc407dc5cc9329b41e59f62e2b',
    'pac_uid': '0_e63870bcecc18',
    'iip': '0',
    '_qimei_uuid42': '183070d3135100ee797b08bc922054dc3062834291',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FeEOpSbFh2Mb1bUxMW9Y3FRPfXwWvOLaNlsjWIkcKeeNg6vlVS5kOVuhNKGQ1M8zaggLqMPmpE5qIUdqEXlQgYg%2F132',
    'wr_gender': '0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=1ff5a0725f8841088b42f97109c45862',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}


# 书籍
book = [
    "36d322f07186022636daa5e","6f932ec05dd9eb6f96f14b9","43f3229071984b9343f04a4","d7732ea0813ab7d58g0184b8",
    "3d03298058a9443d052d409","4fc328a0729350754fc56d4","a743220058a92aa746632c0","140329d0716ce81f140468e",
    "1d9321c0718ff5e11d9afe8","ff132750727dc0f6ff1f7b5","e8532a40719c4eb7e851cbe","9b13257072562b5c9b1c8d6"
]

# 章节
chapter = [
    "ecc32f3013eccbc87e4b62e","a87322c014a87ff679a21ea","e4d32d5015e4da3b7fbb1fa","16732dc0161679091c5aeb1",
    "8f132430178f14e45fce0f7","c9f326d018c9f0f895fb5e4","45c322601945c48cce2e120","d3d322001ad3d9446802347",
    "65132ca01b6512bd43d90e3","c20321001cc20ad4d76f5ae","c51323901dc51ce410c121b","aab325601eaab3238922e53",
    "9bf32f301f9bf31c7ff0a60","c7432af0210c74d97b01b1c","70e32fb021170efdf2eca12","6f4322302126f4922f45dec"
]

# 书籍与章节配对配置，可选
book_chapters = [   {
        "book": "74532af05b31517452d7d51",
        "chapters": [
            "02e32f0021b02e74f10ece8",
            "6ea321b021d6ea9ab1ba605",
            "341323f021e34173cb3824c",
            "c1632f5021fc16a5320f3dc",
            "636320102206364d3f0ffdc",
            "182326e0221182be0c5ca23"
        ]
    },
    {
        "book": "3c6329107163d4243c6b6d1",
        "chapters": [
            "341323f021e34173cb3824c",
            "c1632f5021fc16a5320f3dc",
            "636320102206364d3f0ffdc",
            "182326e0221182be0c5ca23",
            "16732dc0161679091c5aeb1",
            "8f132430178f14e45fce0f7"
        ]
    },
    {
        "book": "cca32e10813ab7d42g015d8d",
        "chapters": [
            "a87322c014a87ff679a21ea",
            "e4d32d5015e4da3b7fbb1fa",
            "16732dc0161679091c5aeb1",
            "8f132430178f14e45fce0f7",
            "c9f326d018c9f0f895fb5e4",
            "45c322601945c48cce2e120"
        ]
    },
    {
        "book": "9ad32d40727950039add092",
        "chapters": [
            "a3f32db0244a3f390d88bb9",
            "14b3246024514bfa6bb1534",
            "d2d32c50249d2ddea18fb39",
            "ad63251024aad61ab143c7e",
            "d0932c3024bd09bf4154e7e",
            "35f3251024e35f4a8d46404"
        ]
    },
        {
        "book": "631324c0813ab735bg01382c",
        "chapters": [
            "a0a32dd027aa0a080f42962",
            "2023270027b202cb962a56f",
            "c8f3245027cc8ffe9a588b8",
            "3de32dd027d3def184ad06e",
            "06932ec027e069059b7e512",
            "ec532f2027fec5decca5182",
            "76d325c028076dc611d6d8c"
        ]
    },
            {
        "book": "ec73249072054fb6ec77894",
        "chapters": [
            "37a32ae029837a749d80032",
            "b3e32dc0299b3e3e393ce03",
            "1d7328e029a1d7f7abc1af1",
            "2a7320a029b2a79ea27c063",
            "1c932da029c1c9ac015999a",
            "6c43287029d6c4b761a2119",
            "06432b4029e064096632ab8"
        ]
    }]

"""
建议保留区域|默认读《与神对话 1》，其它书籍自行测试时间是否增加
"""
data = {
    "appId": "wb115321887466h1810405602",
    "b": "74532af05b31517452d7d51",
    "c": "02e32f0021b02e74f10ece8",
    "ci": 9,
    "co": 334,
    "sm": "Chapter 04哇！你启发了我！嗯，",
    "pr": 45,
    "rt": 34,
    "ts": 1776479780480,
    "rn": 225,
    "sg": "4cabd1e8780c2f6d3d482ae726018f1d15956a7495d1700d5263b2ed76d1f992",
    "ct": 1776479780,
    "ps": "af0327207a96b166g0140f4",
    "pc": "af0327207a96b166g0140f4",
    "s": "a82ff817"
}


def convert(curl_command):
    """提取bash接口中的headers与cookies
    支持 -H 'Cookie: xxx' 和 -b 'xxx' 两种方式的cookie提取
    """
    # 提取 headers
    headers_temp = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_temp[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    
    # 从 -H 'Cookie: xxx' 提取
    cookie_header = next((v for k, v in headers_temp.items() 
                         if k.lower() == 'cookie'), '')
    
    # 从 -b 'xxx' 提取
    cookie_b = re.search(r"-b '([^']+)'", curl_command)
    cookie_string = cookie_b.group(1) if cookie_b else cookie_header
    
    # 解析 cookie 字符串
    if cookie_string:
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key.strip()] = value.strip()
    
    # 移除 headers 中的 Cookie/cookie
    headers = {k: v for k, v in headers_temp.items() 
              if k.lower() != 'cookie'}

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
