import requests
# 以调用百度AI平台的API为例
if __name__ == '__main__':
    url = 'https://jhocrcarno.api.bdymkt.com/ocr/carno'   # 调用车牌识别的地址

    # 要是别的图片地址，本地文件应该也是可以的
    data = 'url=https://tse1-mm.cn.bing.net/th/id/R-C.98082ae60a9486c72896fadfc031f64d?rik=ZP3ZjE4Pifs6bA&riu=http%3a%2f%2fclub1.autoimg.cn%2falbum%2fuserphotos%2f2015%2f01%2f31%2f12%2f21463490-7054-glt8-tn5d-n204atmf9m7h.jpg&ehk=Bhw6%2f2sjzB7o6Jqds4SdQIUcKSVfgP0Bdt%2bYBomcZmE%3d&risl=&pid=ImgRaw&r=0'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Bce-Signature': 'AppCode/a124fe3a2273451a9d2efc0490fabcb9'
    }
    # 接口请求方式是POST，一般来说post中的data和json参数只用传一个即可
    r = requests.request("POST", url, data=data, headers=headers)
    print(r.json())
