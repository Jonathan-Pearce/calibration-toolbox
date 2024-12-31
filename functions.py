
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

    #return bin_boundaries and have two small functions?
    #return these in a list
    bin_lowers = bin_boundaries[:-1]
    bin_uppers = bin_boundaries[1:]


def calc_bin_score():

def calc_norm(acc, conf, norm):
    return(numpy.linalg.norm(acc-conf,ord=norm))