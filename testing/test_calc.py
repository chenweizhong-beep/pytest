import allure
import pytest
import yaml

from python_code.cala import Calctor


def setup_module():
    print("模块级别的SETUP")


def teardown_module():
    print("模块级别的TEARDOWN")


with open('datas./calc.yml', encoding='UTF-8') as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    myid = datas['myid']


@allure.feature("加法功能案例")
class TestCalctor:
    def setup_class(self):
        print("类级别的SETUP")

    def teardown_class(self):
        print("类级别的TEARDOWN")

    def setup(self):  # 实例化放到方法的setup中供每一个方法调用
        self.calc = Calctor()
        print("方法用例开始执行")

    def teardown(self):
        print("方法用例执行结束")

    @pytest.mark.parametrize('a,b,expect', add_datas, ids=myid)
    @allure.story("正向案例")
    def test_add_1(self, a, b, expect):
        # calc = Calctor()
        # if isinstance()
        with allure.step("取得测试数据，并调用功能"):
            result = self.calc.add(a, b)
        with allure.step("判断是否为浮点数"):
            if isinstance(result, float):
                with allure.step("输出结果"):
                    result = round(result, 2)
            with allure.step("断言验证"):
                assert result == expect

    # def test_add_2(self):
    #     # calc = Calctor()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
    #
    # def test_add_3(self):
    #     # calc = Calctor()
    #     result = self.calc.add(-3, 3)
    #     assert result == 0
