"""
src/stats_models.py
Executes Fractional Factorial evaluation and validates linear regression assumptions.
"""
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats

def evaluate_fractional_factorial(df):
    """
    Fits the ordinary least squares model for main screening effects.
    """
    formula = 'CPA ~ C(Hook) + C(Visual) + C(CTA) + C(Demo) + C(Offer)'
    model = ols(formula, data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return model, anova_table

def verify_model_assumptions(model, df):
    """
    Tests residuals to confirm structural validity (Normality and Homoscedasticity).
    """
    residuals = model.resid
    
    # Shapiro-Wilk Test for Normality
    _, shapiro_p = stats.shapiro(residuals)
    
    # Levene's Test for Homoscedasticity across the primary visual groups
    group_neg = df[df['Visual'] == -1]['CPA']
    group_pos = df[df['Visual'] == 1]['CPA']
    _, levene_p = stats.levene(group_neg, group_pos)
    
    diagnostics = {
        'residuals_normal': bool(shapiro_p > 0.05),
        'shapiro_p_value': round(shapiro_p, 4),
        'constant_variance': bool(levene_p > 0.05),
        'levene_p_value': round(levene_p, 4)
    }
    return diagnostics