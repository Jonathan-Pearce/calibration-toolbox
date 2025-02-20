# Calibration-Toolbox
## Metrics
### General Calibration Error (GCE)
```Python
general_calibration_error = GCE(data, bin = 15, class_conditional = TRUE, adaptive_bins = TRUE,
                                top_n_prob = 1, norm = 1, thresholding = 0.01)

```
$\sum_{x=1}^n x=0$

#### ECE
```Python
#wrapper function
ECE = ECE(data)

#or from general function
ECE = GCE(data, norm = 1, top_n = 1) 
```

#### RMSCE (Root Mean Squared Calibration Error)
https://lightning.ai/docs/torchmetrics/stable/classification/calibration_error.html
https://arxiv.org/pdf/1812.04606
```Python
#wrapper function
RMSCE = RMSCE(data)

#or from general function
RMSCE = GCE(data, norm = 2, top_n = 1) 
```

#### MCE
```Python
#wrapper function
ECE = MCE(data)

#or from general function
ECE = GCE(data, norm = "inf", top_n = 1) 
```
#### ACE
#### SCE

### Other Metrics
-  CWCE
-  TCE
-  KS
-  MMCE
-  KCE

$\sum_{x=1}^n x=0$

## Jonathan Pearce, McGill University

A model calibration library currently under construction. Built for PyTorch models, this library enables users to evaluate their model's uncertainty estimates (probability estimates) using popular calibration metrics, train model wrappers that improve model calibration and generate data visualizations to identify where and how their model's are well calibrated or not.

![Diagram](plots/rel_diagram_test.png)

![Diagram2](plots/conf_histogram_test.png)

## References

### Metrics

ECE and MCE - [Obtaining Well Calibrated Probabilities Using Bayesian Binning](http://people.cs.pitt.edu/~milos/research/AAAI_Calibration.pdf)

SCE, ACE and TACE - [Measuring Calibration in Deep Learning](https://arxiv.org/abs/1904.01685)

### Recalibration Methods

Tempurature Scaling - [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)

### Visualizations

Reliability Diagram and Confidence Histograms - [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)
