

def expected_calibration_error(prob, labels, n_bins = 15):
    return(general_binning_calibration_error(prob, labels, n_bins, class_cond = False, adaptive_bins = False, top_k_classes = 1, norm = 1, thresholding = 0.0))

def maximum_calibration_error(prob, labels, n_bins = 15):
    return(general_binning_calibration_error(prob, labels, n_bins, class_cond = False, adaptive_bins = False, top_k_classes = 1, norm = "inf", thresholding = 0.0))
