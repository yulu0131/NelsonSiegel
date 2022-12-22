# Nelson-Siegel Model

*factor interpolation of the term structure, a grid search for an OLS approach using a fixed shape parameter are popular estimation procedures.*

The **initial proposa**l for Nelson-Siegel model (NS) is to represent the range of shapes generally associated with yield curves: **monotonic, humped and S-shaped**, highlighting the **simplicity** and **flexibility** of this model (Nelson and Siegel, 1987).

![Screenshot 2022-12-15 at 16.21.36](../../Library/Application%20Support/typora-user-images/Screenshot%202022-12-15%20at%2016.21.36.png)



The Nelson-Siegel model is widely used in practice for fitting the term structure of interest rates. Nelson-Sigel and its development Nelson-Siegel-Svensson curves provide a parameteric formula specifying the forward rate function. 




## Nelson-Siegel Curve

### Forward rate

The instantaneous forward rate function is given by the solution to a second-order differential equation with real and unreal roots. 
$$
r(\tau) = \beta_0 + \beta_1 e^{-\frac{\tau}{\lambda}} + \beta_2\frac{\tau}{\lambda} e^{-\frac{\tau}{\lambda}}
$$

where 
- $y(\tau)$ : yield with maturity of $\tau$-month
- $\beta_0$: **level**, **positive**, long-term forward rate to converge.
- $\beta_1$: **slope**, monotonically decreasing if negative, and vice versa, indicating the **short-term** component.
- $\beta_2$: **curvature**, generate a hump-shape if positive, or a U-shape if negative, indicating the **mid-term** contribution.

### Spot rate
The spot rate formula can be derived by integrating the instantaneous forward rate.

$$
\frac{\int_{0}^{m}{r(x)dx}}{m}
$$

$$
y(\tau) = \beta_0 + \beta_1 \Bigg(\frac{1-e^{-\frac{\tau}{\lambda}}}{\tau / \lambda}\Bigg) + \beta_2 \Bigg(\frac{1-e^{-\frac{\tau}{\lambda}}}{\tau / \lambda} - e^{-\frac{\tau}{\lambda}}\Bigg)
$$

where 

$\beta_0$, $\beta_1$, $\beta_2$ are level, slope and curvature respectively, while $\lambda$ is the decay factor.

![Screenshot 2022-12-15 at 16.55.05](../../Library/Application%20Support/typora-user-images/Screenshot%202022-12-15%20at%2016.55.05.png)

### noting

If $\tau \rightarrow 0$, the forward rate and the spot rate became
$$
f(0) = r(0) = \beta_0 + \beta_1
$$
If $\tau \rightarrow +\infty $, the forward and the spot rate take as limiting value:
$$
f(+\infty) = r(+\infty) = \beta_0
$$
![Screenshot 2022-12-15 at 16.55.14](../../Library/Application%20Support/typora-user-images/Screenshot%202022-12-15%20at%2016.55.14.png)



## Trival

### Estimation of decay factor

The most difficult part of the model estimation is the restrictions on parameter $\lambda_1$ and $\lambda_2$





## Development

**Nelson-Siegel-Svensson Curve:**

Svensson (1995) suggests an NSS model extended from NS model and this model is widely used in many central banks,  increasing the flexibiility of NS model via adding the fourth parameter, allowing for a second hump-shape or a U-shape.

The instantaneous forward rate is the solution to a second-order differential equation with two equal roots. 
$$
y(t) = \beta_0 + \beta_1 \Bigg(\frac{1-e^{\frac{-t}{\tau_1}}}{t / \tau_1}\Bigg) + \beta_2 \Bigg(\frac{1-e^{\frac{-t}{\tau_1}}}{t / \tau_1} - e^{\frac{-t}{\tau_1}}\Bigg) + \beta_3 \Bigg(\frac{1-e^{\frac{-t}{\tau_2}}}{t / \tau_2} - e^{\frac{-t}{\tau_2}}\Bigg)
$$



 

## Model Implementation

The nelson-siegel curve can be interpreted as a factor model with three factors including the constant factor, while the nelson-siegel-svensson curve can be viewed as four factors with the constant factor.





## Model Calibration

OLS based calibration might work well given the initial comparsion between trial results and library results

![Screenshot 2022-12-22 at 14.37.11](../../Library/Application%20Support/typora-user-images/Screenshot%202022-12-22%20at%2014.37.11.png)

After OLS based model calibration, the fitted curve fits better.

## python

implement a simple ns curve



## References

Nelson, C., and Siegel, A. F., 'Parsimonious Modeling of Yield Curves', Journal of Business, Vol. 60 (October 1987), 473-489.





