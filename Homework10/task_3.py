# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a,b,result', [pytest.param(100, 100, 1, marks=pytest.mark.smoke), (1, 4, 0.25), pytest.param(100, 2, 50, marks=pytest.mark.skip)])
def test_all_division(a, b, result):
    assert all_division(a, b) == result

