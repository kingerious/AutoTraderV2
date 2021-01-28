import json
import os

root_path = os.path.abspath(os.path.dirname(__file__)).split('utils')[0]
os.chdir(root_path)
def json_reader(path=''):
    assert path != '', "路径为空"

    with open(path, "r", encoding='utf8') as f:  # 打开文件
        datas = json.load(f)  # 读取文件
    # print("json数据读取成功")
    return datas


def json_writer(path='', res=''):
    assert path != '', "路径为空"
    assert res != '', "写入数据为空"
    with open(path, "a") as f:
        json.dump(res, f, ensure_ascii=False, indent=4)
