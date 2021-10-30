import os
from typing import List

import pytest
import yaml

from python_code.cala import Calctor


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


yaml_file_path = os.path.dirname(__file__) + "./datas/calc_2.yml"
with open(yaml_file_path, encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    add_data = datas['add']['datas']
    add_myid = datas['add']['myid']
    sub_data = datas['sub']['datas']
    sub_myid = datas['sub']['myid']
    mul_data = datas['mul']['datas']
    mul_myid = datas['mul']['myid']
    div_data = datas['div']['datas']
    div_myid = datas['div']['myid']


@pytest.fixture()
def get_cacl():
    cacl = Calctor()
    return cacl



@pytest.fixture(params=add_data, ids=add_myid)
def get_add_data(request):
    print("计算开始le")
    data = request.param
    print(f"测试数据{data}")
    yield data
    print("计算结束")


@pytest.fixture(params=sub_data, ids=sub_myid)
def get_sub_data(request):
    print("计算开始")
    data = request.param
    print(f"测试数据{data}")
    yield data
    print("计算结束")


@pytest.fixture(params=mul_data, ids=mul_myid)
def get_mul_data(request):
    print("计算开始")
    data = request.param
    print(f"测试数据{data}")
    yield data
    print("计算结束")


@pytest.fixture(params=div_data, ids=div_myid)
def get_div_data(request):
    print("计算开始")
    data = request.param
    print(f"数据{data}")
    yield data
    print("计算结束")

# yaml_file_path = os.path.dirname(__file__) + "./datas/calc_1.yml"
#
# with open(yaml_file_path, encoding='utf-8') as f:
#     datas = yaml.safe_load(f)
#     num = datas['add']['datas']
#     myid = datas['add']['myid']
#     num1 = datas['div']['datas']
#     myid1 = datas['div']['myid']
#
#
# @pytest.fixture()
# def get_cacl():
#     cacl = Calctor()
#     print("计算开始")
#     yield cacl
#     print("计算结束")
#
#
# @pytest.fixture(params=num, ids=myid)
# def get_add_datas(request):
#     data = request.param
#     print(f"测试数据为{data}")
#     return data
#
#
# @pytest.fixture(params=num1, ids=myid1)
# def get_div_datas(request):
#     data = request.param
#     print(f"测试数据为{data}")
#     return data
