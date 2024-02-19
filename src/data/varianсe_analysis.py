import pandas as pd

VALUES = [
    3.1, 2.9, 4.1, 3.9, 2.1, 1.9, 2.1, 1.9,
    3.9, 4.1, 4.9, 5.1, 2.9, 3.1, 3.0, 3.0,
    2.1, 1.9, 3.1, 2.9, 1.1, 0.9, 1.0, 1.0
]


def get_observation_matrix(num_of_factors_1: int, num_of_factors_2: int, observation_numbers: int, values: list) -> pd.DataFrame:
    factor_1 = [
        f'A{i + 1}' for i in range(num_of_factors_1)
        for _ in range(num_of_factors_2)
        for _ in range(observation_numbers)
    ]
    factor_2 = [
        f'B{i + 1}' for _ in range(num_of_factors_1)
        for i in range(num_of_factors_2)
        for _ in range(observation_numbers)
    ]
    observation_matrix = pd.DataFrame({'Factor 1': factor_1,
                                       'Factor 2': factor_2,
                                       'Values': values})
    return observation_matrix
