def searchInArray(array,string):
    for query in array:
        if query == string:
            print("The word",string,"has been found in the array")
    else:
        print("The word",string,"has not been found in the array")

searchInArray(["cat","dog","monkey","imguraffe","reddit alien","GNU sheep"], "cat")
