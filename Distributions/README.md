# Distribution Studies
In order to get a qualitative feel for the probability of a mean reversion based off the network features (i.e. momentum indicators), we need to look at the distributions of each, and perhaps joint distributions. This will give me a better picture of what my strategy entails and what the algorithm will have to learn.

I included the statistics for each distibution below (for now, all I have studied is the RSI). Check out the lPython notebook for more explanation, particularly on the statistics, and see the rest of the histograms in the folder for a visual.


Lag 2: P(X_t=x|x_{t-1} > 70 and x_{t-2} > 70):
N = 280
Mean of Conditional Distribution: 74.1509402277
Standard Deviation of Conditional Distribution: 6.12820741798

Kullback-Leibler (KL) Divergence of Conditional Distribution and Sample Distribution: 0.0298529967765
Normalized: 6.76004183654

Lag 3: P(X_t=x|x_{t-1} > 70 and x_{t-2} > 70) and x_{t-3} > 70):
N = 218
Mean of Conditional Distribution: 74.3784947677
Standard Deviation of Conditional Distribution: 6.36280279766

Kullback-Leibler (KL) Divergence of Conditional Distribution and Sample Distribution: 0.0295670529264
Normalized: 7.20410469743

Lag 4: P(X_t=x|x_{t-1} > 70 and x_{t-2} > 70) and x_{t-3} > 70 and x_{t-4} > 70):
N = 172
Mean of Conditional Distribution: 74.8091567825
Standard Deviation of Conditional Distribution: 6.3754052241

Kullback-Leibler (KL) Divergence of Conditional Distribution and Sample Distribution: 0.0337236525853
Normalized: 7.3630811672

Lag 5: P(X_t=x|x_{t-1} > 70 and x_{t-2} > 70) and x_{t-3} > 70 and x_{t-4} > 70 and x_{t-5} > 70):
N = 140
Mean of Conditional Distribution: 74.8297977048
Standard Deviation of Conditional Distribution: 6.65241979193

Kullback-Leibler (KL) Divergence of Conditional Distribution and Sample Distribution: 0.0238655867326
Normalized: 5.5090321031
