import pandas as pd
import numpy as np

from bartpy.sklearnmodel import SklearnModel
from bartpy.plotting import plot_residuals, plot_modelled_against_actual


def run(alpha, beta, n_trees):
    x = np.sin(np.linspace(0, 5, 120000)).reshape((30000, 4))
    X = pd.DataFrame(x)
    y = np.random.normal(0, 0.1, size=30000) + x.mean(axis=1)

    model = SklearnModel(n_samples=200, n_burn=50, n_trees=n_trees, alpha=alpha, beta=beta)
    model.fit(X, y)
    predictions = model.predict()
    plot_residuals(model)
    plot_modelled_against_actual(model)

    return model, x, y


if __name__ == "__main__":
    print("here")
    import cProfile
    from datetime import datetime as dt
    print(dt.now())
    #run(0.95, 2., 50)
    cProfile.run("run(0.95, 2., 50)")
    print(dt.now())