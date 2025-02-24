import sys
import numpy as np

x = np.load('data/cifar10h-probs.npy')
print(x)

n_classes = np.size(x[1])
print(n_classes)
n_data = np.size(x)
print(np.size(x))

y = np.load('data/test.npy')
print(y)

y_2d = np.zeros_like(x)
print(y_2d)

desired_cols = y.flatten()
desired_rows = np.arange(len(desired_cols))
print(desired_cols)
print(desired_rows)
y_2d[desired_rows, desired_cols] = 1

print(y_2d)


z = x[1]

A = np.array([1, 7, 9, 2, 0.1, 17, 17, 1.5])
k = 3

idx = np.argpartition(A, -k)
print(idx)
print(A[idx[:-k]])

arr_threshold = np.max(A[idx[:-k]])
print(arr_threshold)

A[A <= arr_threshold] = -1

print(A)

k = 3
print(n_data-1)

#for index, value in np.ndenumerate(x):
#    print(index[0], value)

for i, inner_list in enumerate(x):
    #print(i, inner_list)

    A = inner_list
    
    idx = np.argpartition(A, -k)
    arr_threshold = np.max(A[idx[:-k]])
    A[A <= arr_threshold] = -1

    #print(A)

    x[i] = A

