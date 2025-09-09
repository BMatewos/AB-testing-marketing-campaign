from dataclasses import dataclass
import numpy as np
from scipy import stats

@dataclass
class ABResult:
    metric: str
    p_value: float
    statistic: float
    significant: bool
    alpha: float = 0.05

def two_proportion_z_test(success_a:int, total_a:int, success_b:int, total_b:int, metric_name:str="conversion"):
    """
    Classic A/B test for binary outcomes (e.g., purchases / clicks).
    Returns z-test result using pooled variance.
    """
    if not (0 <= success_a <= total_a and 0 <= success_b <= total_b):
        raise ValueError("Successes must be between 0 and total.")
    p_a = success_a / total_a if total_a else 0.0
    p_b = success_b / total_b if total_b else 0.0
    p_pool = (success_a + success_b) / (total_a + total_b)
    se = np.sqrt(p_pool*(1-p_pool)*(1/total_a + 1/total_b))
    if se == 0:
        # degenerate case
        return ABResult(metric_name, p_value=1.0, statistic=0.0, significant=False)
    z = (p_b - p_a) / se
    p_val = 2 * (1 - stats.norm.cdf(abs(z)))  # two-sided
    return ABResult(metric_name, p_value=float(p_val), statistic=float(z), significant=bool(p_val < 0.05))

def t_test_metric(values_a, values_b, metric_name:str="mean_metric"):
    """
    Welch’s t-test for continuous metrics (e.g., revenue per user).
    """
    t_stat, p_val = stats.ttest_ind(values_b, values_a, equal_var=False, nan_policy="omit")
    return ABResult(metric_name, p_value=float(p_val), statistic=float(t_stat), significant=bool(p_val < 0.05))
