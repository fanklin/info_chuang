# import qiniu
#
# access_key = 'BeIq3etfE2ggjKdQnmBP1OLMC1hgAT6MIPK0js22'
# secret_key = '-b8NxSi3kdIN7wBgXyqKN1Is94EymxVDn8lg7GgMv'
#
# # 指定上传文件保存到哪个存储空间
# bucket_name = 'info001'
#
#
# def storage(data):
#     """上传文件到七牛云平台"""
#     # 进行上传之前的初始化
#     q = qiniu.Auth(access_key, secret_key)
#
#     token = q.upload_token(bucket_name)
#
#     # 上传文件到七牛云
#     ret, info = qiniu.put_data(token, None, data)
#
#     if info.status_code == 200:
#         # 上传成功
#         return ret.get('key')
#         # print(token)
#     else:
#         # 上传失败 qd6libghf.bkt.clouddn.com
#         raise Exception('上传文件到七牛云失败')
#
#
# if __name__ == "__main__":
#     file = input('请输入您要上传的文件路径:')
#
#     with open(file, 'rb') as f:
#         storage(f.read())


import logging

from qiniu import Auth, put_data

# 需要填写你的 Access Key 和 Secret Key
access_key = 'BeIq3etfE2ggjKdQnmBP1OLMC1hgAT6MIPK0js22'
secret_key = 'b8NxSi3kdIN7wBgXyqKN1Is94EymxVDn8lg7GgMv'

# 要上传的空间
bucket_name = 'info001'


def storage(data):
    """七牛云存储上传文件接口"""
    if not data:
        return None
    try:
        # 构建鉴权对象
        q = Auth(access_key, secret_key)

        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name)

        # 上传文件  第二个参数是图片的名字， 如果为NOne 七牛会自动生成随机的文件名
        ret, info = put_data(token, None, data)
        print(ret)
        print(info)

    except Exception as e:
        logging.error(e)
        raise e

    if info and info.status_code != 200:
        raise Exception("上传文件到七牛失败")

    # 返回七牛中保存的图片名，这个图片名也是访问七牛获取图片的路径
    return ret["key"]


if __name__ == '__main__':
    file = input('请输入文件路径')
    with open(file, 'rb') as f:
        storage(f.read())