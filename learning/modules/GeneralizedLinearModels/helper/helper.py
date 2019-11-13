import numpy as np
import pandas as pd

from erudition.learning.helpers.plots.plotly_render import render, scatter

def regression(df, power, linreg):

    predictors = ['x']

    if power >=2:
        predictors.extend(['x_%d'%i for i in range(2,power+1)])

    linreg.fit(df[predictors], df['y'])

    plot = scatter(df.x, linreg.predict(df[predictors]), 'Raw')

    #Return the result in pre-defined format
    rss = sum((linreg.predict(df[predictors])-df.y)**2)
    ret = [rss]
    ret.extend([linreg.intercept_])
    ret.extend(linreg.coef_)

    return plot, ret
