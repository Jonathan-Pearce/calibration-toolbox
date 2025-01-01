
def get_bin_boundaries(prob, n_bins, adaptive_bins):
#uniform bin spacing
    if adaptive_bins:
        #size of bins 
        bin_n = int(prob.size/n_bins)
        prob_sort = np.sort(prob)  
        #there must be a one line way to do this
        bin_boundaries = np.array([])

        for i in range(0,self.n_bins):
            bin_boundaries = np.append(bin_boundaries,probabilities_sort[i*bin_n])
        bin_boundaries = np.append(bin_boundaries,1.0)
    
    #equidistant spaced bins of equal width
    else:
        bin_boundaries = np.linspace(0, 1, n_bins + 1)

    return(bin_boundaries)

def compute_bins(prob, labels, n_bins, bin_boundaries):
    bin_prop = np.zeros(n_bins)
    bin_acc = np.zeros(n_bins)
    bin_conf = np.zeros(n_bins)
    bin_score = np.zeros(n_bins)

    #return bin_boundaries and have two small functions?
    #return these in a list
    bin_lowers = bin_boundaries[:-1]
    bin_uppers = bin_boundaries[1:]

    for i, (bin_lower, bin_upper) in enumerate(zip(bin_lowers, bin_uppers)):
        # Calculated |confidence - accuracy| in each bin
        in_bin = np.greater(confidences,bin_lower.item()) * np.less_equal(confidences,bin_upper.item())
        bin_prop[i] = np.mean(in_bin)

        if bin_prop[i].item() > 0:
            bin_acc[i] = np.mean(accuracies[in_bin])
            bin_conf[i] = np.mean(confidences[in_bin])
            bin_score[i] = np.abs(bin_conf[i] - bin_acc[i])


def calc_bin_score():

def calc_norm(acc, conf, norm):
    return(numpy.linalg.norm(acc-conf,ord=norm))