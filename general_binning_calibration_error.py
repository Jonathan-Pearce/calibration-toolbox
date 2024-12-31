#inputs
##numpy matrix of logits (require columns to sum to 1, i.e. probabilities)
##vector of answers
##bins (total or classwise)

#five properties of GCE
##class conditionality
##adaptive bin intervals
##max probability (note top k is from another paper)
##norm
##thresholding (how to work with top k above?)

#design decisions - class based?


def general_binning_calibration_error(prob, labels, n_bins = 15, class_cond = False, adaptive_bins = False, top_k_classes = 1, norm = 2, thresholding = 0.0):

    #validate
    ##class_cond boolean
    ##adaptive_bins boolean
    ##top_k integer (less than or equal to nrows of prob, or "all")
    ##norm non-negative integer or "inf"
    ##thresholding double [0,1)

    if(class_cond):

    if(adaptive_bins):
