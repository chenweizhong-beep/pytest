import allure
import pytest
import yaml

from python_code.cala import Calctor

with open('./datas/calc_1.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)['add']
    num = datas['datas']
    myid = datas['myid']
    num1 = datas['datas1']
    myid1 = datas['myid1']


@allure.feature("计算功能")
class TestCalctor1:

    def setup(self):
        self.calc = Calctor()
        print("计算开始")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, c', num, ids=myid)
    @allure.story("加法功能")
    def test_add_1(self, a, b, c):
        result = self.calc.add(a, b)
        if isinstance(c, float):
            result = round(result, 2)
        assert result == c

    @pytest.mark.parametrize('a, b, c', num1, ids=myid1)
    @allure.story("除法功能")
    def test_div_1(self, a, b, c):
        try:
            result = self.calc.div(a, b)
        except Exception:
            print("抛出异常，除数不能为0")
        finally:
            assert result == c
