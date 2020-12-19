from PIL import Image

def otsu_threshold(gray_img):
    hist = gray_img.histogram()
    Imax = hist.index(max(hist))
    Imin = hist.index(min(hist))
    mu0 = sum(hist)/256
    
    s_max = 0
    threshold = -1
    
    print(Imax)
    print(Imin)
    for th in range(min(Imin, Imax), max(Imin, Imax)+1):
        # sum each pexels
        n1 = sum(hist[:th])
        n2 = sum(hist[th:])
        
        # mean of each class
        mu1 = sum([i * hist[i] for i in range(th)])/n1
        mu2 = sum([i * hist[i] for i in range(th, 256)])/n2
        
        # calc distribution between each class
        s = (n1*(mu1-mu0)**2 + n2*(mu2-mu0)**2)/(n1+n2)
        print(th)
        if s > s_max:
            s_max = s
            threshold = th
    print(threshold)
    # thresholding
    bin_img = gray_img.point(lambda x: 0 if x < threshold else 255)
    
    return bin_img