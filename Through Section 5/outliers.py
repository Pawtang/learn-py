data = [4, 5, 104, 105, 110, 122, 112, 54, .05, 21, 104, 123, 144, 155,
       159, 151, 111, 50331, 431412, 1234, 132, 166, 175, 203, 255, 360]
#data = [] # Test edge case empty list
#data = [3, 313, 12] # Test with only outliers
#data = [105, 104, 111, 103, 170] # Only in range



# Corner case is like an edge case, but with more than one parameter involved.


data.sort()

min_valid = 100
max_valid = 200

#Safely removing values from a list
#Do not want to iterate over list if removing items, as the index won't capture elements correctly after deletion
#So, what's the right way?

#Process low values:
stop = 0
for index, value in enumerate(data):
    if value > min_valid:
        stop = index
        break

print(f"Data before trim start: {data}")
print(f"Stops at {stop}") #for debugging
del(data[:stop])
print(f"Data after trim start: {data}")

# Process high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        #Index of last item to keep.
        #Set Start to position of first item to delete
        start = index + 1
        break

print(f"Data before trim end: {data}")
print(f"Starts at {start}")
del data[start:]
print(f"Data after trim end: {data}")