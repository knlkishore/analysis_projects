import numpy as np

def calculate(arr):
    print("---------------------------------------------1")
    #Checking if the passed list have 9 elements or not
    if len(arr) != 9:
        raise ValueError("List must contain nine numbers ")

    A = np.array(arr)
    A = A.reshape(3,3)
    
    return {'mean': [A.mean(axis = 0).tolist(), A.mean(axis=1).tolist(), A.mean()],
    'variance': [A.var(axis=0).tolist(), A.var(axis=1).tolist(), A.var()],
    'standard deviation': [A.std(axis=0).tolist(), A.std(axis=1).tolist(), A.std()],
    'max': [A.max(axis=0).tolist(), A.max(axis=1).tolist(), A.max()],
    'min': [A.min(axis=0).tolist(), A.min(axis=1).tolist(), A.min()],
    'sum': [A.sum(axis=0).tolist(), A.sum(axis=1).tolist(), A.sum()],
    }



A = [0,1,2,3,4,5,6,7,8]
Z =  calculate(A)
print("---------------------------------------------")
for i in Z:
    print(Z[i])

print("---------------------------------------------")

