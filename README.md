# Calibration Toolbox
A machine learning model calibration metrics library, built using NumPy. Evaluate model uncertainty using popular calibration metrics from deep learning research. Inspired by [Uncertainty Toolbox](https://github.com/uncertainty-toolbox/uncertainty-toolbox).


## Metrics
### General Calibration Error (GCE)
- Kull et al. (2019) - [Beyond temperature scaling: Obtaining well-calibrated multiclass probabilities with Dirichlet calibration](https://arxiv.org/abs/1910.12656)
- Nixon et al. (2020) - [Measuring Calibration in Deep Learning](https://arxiv.org/abs/1904.01685)


The (class conditional) general calibration error with $L^{p}$ norm can be expressed as:

```math
\Large GCE = \big (\displaystyle\sum_{k=1}^{K} \text{ } \sum_{b=1}^{B} \frac{n_{bk}}{NK} |acc(b,k) - conf(b,k)|^p \big )^\frac{1}{p}
```

Where $acc(b,k)$ and $conf(b,k)$ are the accuracy and confidence of bin $b$ for class label $k$; $n_{bk}$ is the number of predicitions in bin $b$ for class label $k$; and $N$ is the total number of data points. This Python library allows users to customize this flexible calibration formula to fit their needs using the following code:

```Python
general_calibration_error = GCE(prob, labels, bin = 15, class_conditional = True, adaptive_bins = False,
                                top_k_classes = 1, norm = 1, thresholding = 0.00)

```
Additionally, we provide a simpler interface to utilize commonly used metrics:
#### Expected Calibration Error (ECE)
- Naeini et al. (2015) - [Obtaining Well Calibrated Probabilities Using Bayesian Binning](https://ojs.aaai.org/index.php/AAAI/article/view/9602)

```Python
#wrapper function
expected_calibration_error = ECE(prob, labels)

#general function
expected_calibration_error = GCE(prob, labels, bin = 15, class_conditional = False, adaptive_bins = False,
                                  top_k_classes = 1, norm = 1, thresholding = 0.00) 
```

#### Root Mean Squared Calibration Error (RMSCE)
- Hendrycks et al. (2019) - [Deep Anomaly Detection with Outlier Exposure](https://arxiv.org/abs/1812.04606)

```Python
#wrapper function
root_mean_square_calibration_error = RMSCE(prob, labels)

#general function
root_mean_square_calibration_error = GCE(prob, labels, bin = 15, class_conditional = False, adaptive_bins = False,
                                          top_k_classes = 1, norm = 2, thresholding = 0.00) 
```

#### Maximum Calibration Error (MCE)
- Naeini et al. (2015) - [Obtaining Well Calibrated Probabilities Using Bayesian Binning](https://ojs.aaai.org/index.php/AAAI/article/view/9602)

```Python
#wrapper function
maximum_calibration_error = MCE(prob, labels)

#general function
maximum_calibration_error = GCE(prob, labels, bin = 15, class_conditional = False, adaptive_bins = False,
                                top_k_classes = 1, norm = 'inf', thresholding = 0.00) 
```

#### Adaptive Calibration Error (ACE)
- Nixon et al. (2020) - [Measuring Calibration in Deep Learning](https://arxiv.org/abs/1904.01685)

```Python
#wrapper function
adaptive_calibration_error = ACE(prob, labels)

#general function
adaptive_calibration_error = GCE(prob, labels, bin = 15, class_conditional = True, adaptive_bins = True,
                                  top_k_classes = 'all', norm = 1, thresholding = 0.00) 
```

#### Static Calibration Error (SCE)
- Nixon et al. (2020) - [Measuring Calibration in Deep Learning](https://arxiv.org/abs/1904.01685)

```Python
#wrapper function
static_calibration_error = SCE(prob, labels)

#general function
static_calibration_error = GCE(prob, labels, bin = 15, class_conditional = True, adaptive_bins = False,
                                top_k_classes = 'all', norm = 1, thresholding = 0.00) 
```

#### Top-r calibration error (ToprCE)
- Gupta et al. (2021) - [Calibration of Neural Networks using Splines](https://arxiv.org/abs/2006.12800)

```Python
#wrapper function
top_r_calibration_error = ToprCE(prob, labels)

#general function
top_r_calibration_error = GCE(prob, labels, bin = 15, class_conditional = True, adaptive_bins = False,
                              top_k_classes = r, norm = 1, thresholding = 0.00) 
```

## Upcoming Features

### Metrics
- [ ] Class-wise calibration error (CWCE), Kumar et al. (2019) - [Verified Uncertainty Calibration](https://arxiv.org/abs/1909.10155)
- [ ] Top-label calibration error (TCE), Kumar et al. (2019) - [Verified Uncertainty Calibration](https://arxiv.org/abs/1909.10155)
- [ ] Kolmogorov-Smirnov calibration error (KSCE), Gupta et al. (2021) - [Calibration of Neural Networks using Splines](https://arxiv.org/abs/2006.12800)
- [ ] Maximum mean calibration error (MMCE), Kumar et al. (2018) - [Trainable Calibration Measures for Neural Networks from Kernel Mean Embeddings](https://proceedings.mlr.press/v80/kumar18a.html)
- [ ] Kernel calibration error (KCE), Kull et al. (2020) - [Calibration tests in multi-class classification: A unifying framework](https://arxiv.org/abs/1910.11385v2)
- [ ] Over/Under confidence decomposition, Pearce et al. (2022) - [Adaptive Confidence Calibration](https://caiac.pubpub.org/pub/camnr5ix/release/1)

### Visualizations
- [ ] Reliability Diagram
- [ ] Confidence Histograms, Guo et al. (2017) - [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)

### Other 
- [ ] PyTorch recalibration library
