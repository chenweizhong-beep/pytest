import os
from typing import List

import pytest
import yaml


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


yaml_file_path = os.path.dirname(__file__) + "./datas.yml"
with open(yaml_file_path, encoding="utf-8") as f:
    datas = yaml.safe_load(f)["datas"]
    # 创建标签数据
    data1 = datas["creat_tag"]["data"]
    ids1 = datas["creat_tag"]["ids"]
    # 更新标签数据
    data2 = datas["update_tag"]["data"]
    ids2 = datas["update_tag"]["ids"]
    # 删除标签数据
    data3 = datas["deleted_tag"]["data"]
    ids3 = datas["deleted_tag"]["ids"]
    # 增加标签成员数据
    data4 = datas["creat_member"]["data"]
    ids4 = datas["creat_member"]["ids"]
    # 获取标签成员数据
    data5 = datas["get_member"]["data"]
    ids5 = datas["get_member"]["ids"]
    # 删除标签成员数据
    data6 = datas["deleted_member"]["data"]
    ids6 = datas["deleted_member"]["ids"]


@pytest.fixture(params=data1, ids=ids1)
def creat_tag(request):
    data = request.param
    yield data


@pytest.fixture(params=data2, ids=ids2)
def update_tag(request):
    data = request.param
    yield data


@pytest.fixture(params=data3, ids=ids3)
def deleted_tag(request):
    data = request.param
    yield data


@pytest.fixture(params=data4, ids=ids4)
def creat_member(request):
    data = request.param
    yield data


@pytest.fixture(params=data5, ids=ids5)
def get_member(request):
    data = request.param
    yield data


@pytest.fixture(params=data6, ids=ids6)
def deleted_member(request):
    data = request.param
    yield data
