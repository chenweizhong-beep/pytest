import allure
import pytest


@allure.feature("计算功能")
class TestCalcal2:

    @allure.story("减法功能")
    @pytest.mark.run(order=2)
    def test_sub(self, get_cacl, get_sub_data):
        result = None
        with allure.step("异常判断"):
            try:
                with allure.step("调用减法功能，获取差"):
                    result = get_cacl.sub(get_sub_data[0], get_sub_data[1])
                with allure.step("判断差是否是浮点数"):
                    if isinstance(result, float):
                        with allure.step("差是浮点数，调用取小数点后两位"):
                            result = round(result, 2)
            except Exception as e:
                print(f"异常抛出{e}")
        with allure.step("断言判断"):
            assert result == get_sub_data[2]

    @allure.story("加法功能")
    @pytest.mark.run(order=1)
    def test_add(self, get_cacl, get_add_data):
        result = None
        with allure.step("异常判断"):
            try:
                with allure.step("调用减法功能，获取和"):
                    result = get_cacl.add(get_add_data[0], get_add_data[1])
                    with allure.step("判断和是否是浮点数"):
                        if isinstance(result, float):
                            with allure.step("和是浮点数，调用取小数点后两位"):
                                result = round(result, 2)
            except Exception as e:
                print(f"异常抛出{e}")
        with allure.step("断言判断"):
            assert result == get_add_data[2]

    # @pytest.mark.flaky(reruns=4, reruns_delay=3)
    @allure.story("除法功能")
    @pytest.mark.run(order=4)
    def test_div(self, get_cacl, get_div_data):
        result = None
        with allure.step("异常判断"):
            try:
                with allure.step("调用减法功能，获取商"):
                    result = get_cacl.div(get_div_data[0], get_div_data[1])
                    with allure.step("判断和是否是浮点数"):
                        if isinstance(result, float):
                            with allure.step("和是浮点数，调用取小数点后两位"):
                                result = round(result, 2)
            except Exception as e:
                print(f"异常抛出{e}")
        with allure.step("断言判断"):
            assert result == get_div_data[2]

    @allure.story("乘法功能")
    @pytest.mark.run(order=3)
    def test_mul(self, get_cacl, get_mul_data):
        result = None
        with allure.step("异常判断"):
            try:
                with allure.step("调用减法功能，获取积"):
                    result = get_cacl.mul(get_mul_data[0], get_mul_data[1])
            except Exception as e:
                print(f"异常抛出{e}")
        with allure.step("断言判断"):
            assert result == get_mul_data[2]
