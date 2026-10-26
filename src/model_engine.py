"""
ML Engine Module: Piecewise Linear RUL Regression & NASA Scoring
Trains XGBoost Regressor on dynamic rolling temporal features and evaluates
against the official NASA Asymmetric penalty metric.
"""
import numpy as np
import joblib
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def compute_nasa_asymmetric_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Computes the official NASA C-MAPSS Asymmetric Scoring metric.
    Penalizes late predictions (d >= 0) exponentially harder than early warnings (d < 0).
    """
    d = y_pred - y_true
    # d < 0 (early warning): exp(-d/13) - 1
    # d >= 0 (late failure): exp(d/10) - 1
    scores = np.where(d < 0, np.exp(-d / 13.0) - 1.0, np.exp(d / 10.0) - 1.0)
    return float(np.sum(scores))

class RULPredictor:
    def __init__(self, n_estimators=250, max_depth=6, learning_rate=0.04):
        self.model = XGBRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate,
            subsample=0.85,
            colsample_bytree=0.85,
            random_state=42,
            n_jobs=-1
        )
        self.feature_names = []

    def fit(self, X_train: np.ndarray, y_train: np.ndarray, feature_names: list = None):
        if feature_names:
            self.feature_names = feature_names
        self.model.fit(X_train, y_train)

    def predict(self, X: np.ndarray) -> np.ndarray:
        preds = self.model.predict(X)
        return np.maximum(preds, 0.0)

    def evaluate(self, X_test: np.ndarray, y_true: np.ndarray) -> dict:
        y_pred = self.predict(X_test)
        
        rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
        mae = float(mean_absolute_error(y_true, y_pred))
        r2 = float(r2_score(y_true, y_pred))
        nasa_score = compute_nasa_asymmetric_score(y_true, y_pred)
        
        # Accuracy within tolerance (+/- 15 cycles)
        within_15 = float(np.mean(np.abs(y_pred - y_true) <= 15.0) * 100.0)
        within_25 = float(np.mean(np.abs(y_pred - y_true) <= 25.0) * 100.0)
        
        # Mean asymmetric bias
        residuals = y_pred - y_true
        bias = float(np.mean(residuals))

        return {
            "rmse": round(rmse, 2),
            "mae": round(mae, 2),
            "r2_score": round(r2, 3),
            "nasa_score": round(nasa_score, 1),
            "accuracy_within_15_cycles_pct": round(within_15, 1),
            "accuracy_within_25_cycles_pct": round(within_25, 1),
            "mean_residual_bias": round(bias, 2),
            "y_pred": y_pred.tolist(),
            "y_true": y_true.tolist()
        }

    def save(self, filepath: str):
        payload = {
            "model": self.model,
            "feature_names": self.feature_names
        }
        joblib.dump(payload, filepath)

    @classmethod
    def load(cls, filepath: str):
        payload = joblib.load(filepath)
        instance = cls()
        instance.model = payload["model"]
        instance.feature_names = payload.get("feature_names", [])
        return instance
