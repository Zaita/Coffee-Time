import math

print("THIS IS NOT COMPLETE AND WILL NOT WORK")

buckets = []
buckets.append([])
buckets.append([])
buckets.append([])

start_value = 0

found_answer = False
while not found_answer:
    start_value += 1


    
    buckets[0].append(start_value)

    error = False
    
    for i in range(start_value, 14):
        print('i: ' + str(i))
        placed_i = False
        print('Buckets: ' + str(len(buckets)))
        for bucket in buckets:
            if len(bucket) == 0:
                print('Placing i in new bucket')
                bucket.append(i)
                break

            bad_match = False
            for value in bucket:
                for other_value in bucket:
                    if abs(other_value - value) == i:
                        bad_match = True
                        break

            if not bad_match:
                bucket.append(i)
                placed_i = True
                break
        if not placed_i:
            error = True
            break

    if not error:
        print("Found Answer")
        break

total_length = 0
for bucket in buckets:
    print("Bucket: " + ''.join(str(bucket)))
    total_length += len(bucket)
print("Total Length: " + str(total_length))
          
            
    
