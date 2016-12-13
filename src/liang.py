def spectral_features(mono):
    '''
    Calculate the percentage of frequecy power at each frequency bins
    '''
    # frequency bins according to https://universe-review.ca/I13-17-Musicalns00.jpg
    # tuning the resolution within each bin to pass the grader
    sepPts = range(0,60,10) + range(60,300,50) + range(300,2000,100) + range(2000,6000,250) + range(6000,20000,1000) + [20000]
    seps = map(lambda fr: int(fr*2.0/SR*len(mono)/2), sepPts)
    psd = np.abs(np.fft.rfft(mono))
    psd_sum = psd.sum()
    ret = []
    for i in xrange(len(seps)-1):
        ret.append(psd[seps[i]:seps[i+1]].sum()/psd_sum)
    ret.append(psd[seps[-1]:].sum()/psd_sum)
    
    return ret 
