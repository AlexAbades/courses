import pandas as pd
# There are 3 main ways of combining DataFrames together: Merging, Joining and Concatenating.

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
},
    index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
},
    index=[4, 5, 6, 7])

df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']
},
     index=[8, 9, 10, 11])
print(df1)
print('')
print(df2)
print('')
print(df3)
print('')

print('Ex 1: Concatenate rows')
print(pd.concat([df1, df2, df3]))
print('')

print('Ex 2: concatenate by columns')
# Concatenation basically glues together DataFrames. Keep in mind that dimensions should match along the axis you are
# concatenating on. You can use **pd.concat** and pass in a list of DataFrames to concatenate together:
print(pd.concat([df1, df2, df3], axis=1))
print('')

left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print(left)
print('')
print(right)
print('')

print('Ex 3: Merging dataFrames by a key in column. only 1 on key')
print(pd.merge(left,right, how= 'inner', on='key' ))
print('')
# We only cn merge rwo at a time, but we can specify more that one: on key

print('Ex 4: Merging DataFrames by key in column, two on key')
# The merge function allows you to merge DataFrames together using a similar logic as merging SQL Tables together.
# For example:
left1 = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right1 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print(pd.merge(left1, right1, on= ['key1', 'key2']))
print('')
print('Notice the difference with the concatenate method')
print(pd.concat([left1,right1], axis=1))
print('')

print('Ex 5: Joining')
# Joining is a convenient method for combining the columns of two potentially differently-indexed DataFrames into a
# single result DataFrame.
# It's very similar to merge, except they are actually joining on the index instead of a column

left2 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
},
    index=['K0', 'K1', 'K2'])

right2 = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
},
    index=['K0', 'K2', 'K3'])
print(left2.join(right2))
print('')
print(right2.join(left2))