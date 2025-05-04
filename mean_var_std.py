import numpy as np

def calculate(list):

    # check length of the list
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")

    # convert list to a numpy array and reshape to a 3x3
    arr = np.array(list).reshape(3,3)
    # print(arr)
    # print("\n")
    
    # calculate the mean
    
    mean_rows = np.mean(arr, axis=1)       # mean across rows
    mean_columns = np.mean(arr, axis=0)    # mean across columns
    mean_fltt = np.mean(arr)               # mean across flattened matrix
    
    # calculate the variance
    
    variance_rows = np.var(arr, axis=1)    # variance across rows
    variance_columns = np.var(arr, axis=0) # variance across columns
    variance_fltt = np.var(arr)            # variance across flattened matrix
    
    # calculate the standard deviation
    
    stdev_rows = np.std(arr, axis=1)       # standard deviation across rows   
    stdev_columns = np.std(arr, axis=0)    # standard deviation across columns
    stdev_fltt = np.std(arr)               # standard deviation across flattened matrix
    
    # find the max
    
    max_rows = np.max(arr, axis=1)         # max across rows
    max_columns = np.max(arr, axis=0)      # max across columns  
    max_fltt = np.max(arr)                 # max across flattened matrix  
    
    # find the min

    min_rows = np.min(arr, axis=1)         # min across rows  
    min_columns = np.min(arr, axis=0)      # min across columns  
    min_fltt = np.min(arr)                 # min across flattened matrix  
    
    # calculate the sum

    sum_rows = np.sum(arr, axis=1)        # sum across rows  
    sum_columns = np.sum(arr, axis=0)     # sum across columns  
    sum_fltt = np.sum(arr)                # sum across flattened matrix  
    
    calculations = {
            'mean': [mean_columns.tolist(), mean_rows.tolist(), float(mean_fltt)],
            'variance': [variance_columns.tolist(), variance_rows.tolist(), float(variance_fltt)],
            'standard deviation': [stdev_columns.tolist(), stdev_rows.tolist(), float(stdev_fltt)],
            'max': [max_columns.tolist(), max_rows.tolist(), float(max_fltt)],
            'min': [min_columns.tolist(), min_rows.tolist(), float(min_fltt)],
            'sum': [sum_columns.tolist(), sum_rows.tolist(), float(sum_fltt)]
           }
 
    print(calculations)

    return calculations