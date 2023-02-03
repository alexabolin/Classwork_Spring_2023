import pytest

from blood_calculator import HDL_analysis
from blood_calculator import LDL_analysis
from blood_calculator import Chol_analysis


@pytest.mark.parametrize("test, input, expected",
                         [(HDL_analysis, 65, "Normal"),
                          (HDL_analysis, 45, "Borderline Low"),
                          (HDL_analysis, 20, "Low"),
                          (LDL_analysis, 100, "Normal"),
                          (LDL_analysis, 140, "Borderline High"),
                          (LDL_analysis, 180, "High"),
                          (LDL_analysis, 200, "Very High"),
                          (Chol_analysis, 250, "High"),
                          (Chol_analysis, 210, "Borderline High"),
                          (Chol_analysis, 190, "Normal")])
def test_HDL_analysis_normal(test, input, expected):
    # Arrange (parameters)
    # Act
    answer = test(input)
    # Assert
    assert answer == expected

# @pytest.mark.parametrize("LDL_input, expected",
# [(100, "Normal"),
# (140, "Borderline High"),
# (180, "High"),
# (200, "Very High"),
# ])

# def test_LDL_analysis_normal(LDL_input, expected):
#     from blood_calculator import LDL_analysis
#     # Arrange (parameters)
#     # Act
#     answer = LDL_analysis(LDL_input)
#     # Assert
#     assert answer == expected

# @pytest.mark.parametrize("Chol_input, expected",
# [(250, "High"),
# (210, "Borderline High"),
# (190, "Normal")
# ])

# def test_Chol_analysis_normal(Chol_input, expected):
#     from blood_calculator import Chol_analysis
#     # Arrange (parameters)
#     # Act
#     answer = Chol_analysis(Chol_input)
#     # Assert
#     assert answer == expected
