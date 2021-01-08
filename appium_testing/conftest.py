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
with open(yaml_file_path, encoding='utf-8') as f:
    values = yaml.safe_load(f)['add']
    data = values['datas']
    name = values['myid']


@pytest.fixture(params=data, ids=name)
def add_names(request):
    data = request.param
    yield data
