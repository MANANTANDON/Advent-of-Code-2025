docOne = ["52-75","71615244-71792700","89451761-89562523","594077-672686","31503-39016","733-976","1-20","400309-479672","458-635","836793365-836858811","3395595155-3395672258","290-391","5168-7482","4545413413-4545538932","65590172-65702074","25-42","221412-256187","873499-1078482","118-154","68597355-68768392","102907-146478","4251706-4487069","64895-87330","8664371543-8664413195","4091-5065","537300-565631","77-115","83892238-83982935","6631446-6694349","1112-1649","7725-9776","1453397-1493799","10240-12328","15873-20410","1925-2744","4362535948-4362554186","3078725-3256936","710512-853550","279817-346202","45515-60928","3240-3952"]
docTwo = ["3737332285-3737422568","5858547751-5858626020","166911-236630","15329757-15423690","753995-801224","1-20","2180484-2259220","24-47","73630108-73867501","4052222-4199117","9226851880-9226945212","7337-24735","555454-591466","7777695646-7777817695","1070-2489","81504542-81618752","2584-6199","8857860-8922218","979959461-980003045","49-128","109907-161935","53514821-53703445","362278-509285","151-286","625491-681593","7715704912-7715863357","29210-60779","3287787-3395869","501-921","979760-1021259"]

def StarThree():
    result = []
    total = 0
    for n in docTwo:
        rangeList = n.split("-")
        newStrRangeList = [str(i) for i in range(int(rangeList[0]), int(rangeList[1]) + 1)]
        for num in newStrRangeList:
            half = len(num) // 2
            if(len(num) % 2 == 0):
                left = num[:half]
                right = num[half:]
                if(left == right):
                    result.append(num)
    
    for r in result:
        total += int(r)
    print(f"Star Three: {total}")
                

def StarFour():
    result = []
    total = 0
    for n in docTwo:
        rangeList = n.split("-")
        newStrRangeList = [str(i) for i in range(int(rangeList[0]), int(rangeList[1]) + 1)]
        
        for num in newStrRangeList:
            n = len(num)
            is_invalid = False
            
            for pattern_len in range(1, n):
                if n % pattern_len == 0:  
                    pattern = num[:pattern_len]
                    if pattern * (n // pattern_len) == num:
                        is_invalid = True
                        break  
            
            if is_invalid:
                result.append(num)
    
    for r in result:
        total += int(r)
    print(f"Star Four: {total}")

if __name__ == "__main__":
    StarThree()
    StarFour()
