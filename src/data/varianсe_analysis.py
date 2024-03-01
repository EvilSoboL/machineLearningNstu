import numpy as np


def get_two_factor_observation_matrix(
        num_of_factors_1: int, num_of_factors_2: int, observation_numbers: int
) -> np.ndarray | None:
    observation_matrix: np.ndarray = np.zeros(
        (num_of_factors_1*num_of_factors_2*observation_numbers, (num_of_factors_1 + num_of_factors_2 + 1)), dtype=int
    )
    observation_matrix[:, 0] = 1

    observation_matrix[:, 1] = [number for number in [1, 0, 0] for _ in range(num_of_factors_2*observation_numbers)]
    observation_matrix[:, 2] = [number for number in [0, 1, 0] for _ in range(num_of_factors_2*observation_numbers)]
    observation_matrix[:, 3] = [number for number in [0, 0, 1] for _ in range(num_of_factors_2 * observation_numbers)]

    observation_matrix[:, 4] = [number for _ in range(num_of_factors_1) for number in [1, 1, 0, 0, 0, 0, 0, 0]]
    observation_matrix[:, 5] = [number for _ in range(num_of_factors_1) for number in [0, 0, 1, 1, 0, 0, 0, 0]]
    observation_matrix[:, 6] = [number for _ in range(num_of_factors_1) for number in [0, 0, 0, 0, 1, 1, 0, 0]]
    observation_matrix[:, 7] = [number for _ in range(num_of_factors_1) for number in [0, 0, 0, 0, 0, 0, 1, 1]]
    return observation_matrix
