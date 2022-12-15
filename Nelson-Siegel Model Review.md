# Nelson-Siegel Models

factor interpolation of the term structure

The Nelson-Siegel model is widely used in practice for fitting the term structure of interest rates. Nelson-Sigel and its development Nelson-Siegel-Svensson curves provide a parameteric formula specifying the forward rate function. 


a grid search for an OLS approach using a fixed shape parameter are popular estimation procedures.

**Nelson-Siegel Curve:**

$$
y(t) = \beta_0 + \beta_1 \Bigg(\frac{1-e^{\frac{-t}{\tau_1}}}{t / \tau_1}\Bigg) + \beta_2 \Bigg(\frac{1-e^{\frac{-t}{\tau_1}}}{t / \tau_1} - e^{\frac{-t}{\tau_1}}\Bigg)
$$



This contains three components:

1. a constant $\beta_0$, specifying the long-term forward rate to converge, and this parameter must be positive.
2. an exponential rate  $\beta_1 \exp({-\frac{m}{\tau_1}})$, monotonically decreasing when $\beta_1$ is negative, and vice versa.
3. the third component is to generate a hump-shape when $\beta_2$ is positive, or a U-shape when $\beta_2$ is negative.



**Nelson-Siegel-Svensson Curve:**

Svensson (1994): development of nelson-siegel model, increasing the flexibiility of NS model via adding the fourth parameter, allowing for a second hump-shape or a U-shape

$$
y(t) = \beta_0 + \beta_1 \Bigg(\frac{1-e^{\frac{-t}{\tau_1}}}{t / \tau_1}\Bigg) + \beta_2 \Bigg(\frac{1-e^{\frac{-t}{\tau_1}}}{t / \tau_1} - e^{\frac{-t}{\tau_1}}\Bigg) + \beta_3 \Bigg(\frac{1-e^{\frac{-t}{\tau_2}}}{t / \tau_2} - e^{\frac{-t}{\tau_2}}\Bigg)
$$





## Model Implementation

The nelson-siegel curve can be interpreted as a factor model with three factors including the constant factor, while the nelson-siegel-svensson curve can be viewed as four factors with the constant factor.





## Model Calibration





## python

Fitting 中债登收益率key rate (bond_yield.py)





