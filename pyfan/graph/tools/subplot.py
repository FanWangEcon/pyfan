'''
Created on Aug 6, 2018

@author: fan

Design page subplot

'''


def subplot_design(plot_count=10, base_multiple=4, base_multiple_high_frac = 0.60):
    """subplot grid and size given total plot count
    
    figsize = (width height)
    
    Examples
    --------
    import Support.graph.subplot as sup_graph_subplot
    figsize, rows, cols = sup_graph_subplot.subplot_design(plot_count=10, base_multiple=4, base_multiple_high_frac = 0.60)        
    """
    
    if plot_count == 1:
        figsize = (base_multiple*1,base_multiple*1)
        rows = 1
        cols = 1
    elif plot_count <= 2:    
        figsize = (base_multiple*2,base_multiple*1)
        rows = 1
        cols = 2
    elif plot_count <= 4:
        figsize = (base_multiple*2,base_multiple*2)
        rows = 2
        cols = 2
    elif plot_count <= 6:
        figsize = (base_multiple*3,base_multiple*2)
        rows = 2
        cols = 3
    elif plot_count <= 9:
        figsize = (base_multiple*3,base_multiple*3)
        rows = 3
        cols = 3        
    elif plot_count <= 12:
        figsize = (base_multiple*4,base_multiple*3)
        rows = 3
        cols = 4        
    elif plot_count <= 16:
        figsize = (base_multiple*4,base_multiple*4)
        rows = 4
        cols = 4
    elif plot_count <= 20:
        figsize = (base_multiple*5,base_multiple*4)
        rows = 4
        cols = 5
    elif plot_count <= 25:
        figsize = (base_multiple*5,base_multiple*5)
        rows = 5
        cols = 5
    else:
                
        lessthan = True        
        sqr_ctr = 1
        while lessthan:
            sqr_ctr += 1
            if (sqr_ctr**2 >= plot_count):
                lessthan = False
                minus_one_row = False
                if (sqr_ctr*(sqr_ctr-1) >= plot_count):
                    minus_one_row = True
                    
        rows = sqr_ctr
        if (minus_one_row):
            rows = rows - 1
        cols = sqr_ctr
    
        figsize_width = max(20, int(base_multiple*base_multiple_high_frac*rows))
        figsize_width = max(20, int(base_multiple*base_multiple_high_frac*cols))
        figsize = (figsize_width, figsize_width)
    
    return figsize, rows, cols

if __name__ == "__main__":
    for plot_count in range(100):
        print('plot_count:', plot_count, ', result:', subplot_design(plot_count=plot_count))
    
