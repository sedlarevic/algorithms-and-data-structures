class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)

        # svi intervali koji se ZAVRSAVAJU pre nego sto novi interval pocne
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # merge preklapanja -> svi intervali koji pocinju pre ili kada se novi interval zavrsi
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 3) ubaci
        res.append(newInterval)

        # 4) svi intervali koji su preostali, nakon preklapanja
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

    def insertMojNacin(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # 0 - pocetak
        # 1 - kraj

        def findBiggerIntervalIndex(newInterval,intervals,currentIndex):
            
            for i in range(currentIndex,len(intervals),1):
                if newInterval[1] < intervals[i][1]:
                    return i
                
            return -1

        i = 0
        length = len(intervals)
        if length == 0:
            return [newInterval]

        while i < length:
            print("In while loop")
            if newInterval[0] > intervals[i][1]:
                if i+1<len(intervals):
                    if newInterval[1] < intervals[i+1][0]:
                        # slucaj [3,5] -> [ [1,2] [6,7] ] -> [ [1,2], [3,5], [6,7] ]
                        print(1)
                        print("INDEX:", i)

                        intervals.insert(i+1,newInterval)
                        return intervals
                    if newInterval[1] == intervals[i+1][0]:
                        print(2)
                        print("INDEX:", i)
                        # slucaj [3,5] -> [ [1,2] [5,7] ] -> [ [1,2], [3,7] ]
                        intervals[i+1][0] = newInterval[0]
                        return intervals
                    if newInterval[1] > intervals[i+1][0]:
                        print(3)
                        print("INDEX:", i)
                        # idi dalje
                        i += 1
                        pass
                else:
                    intervals.append(newInterval)
                    return intervals
            if newInterval[0] == intervals[i][1]:
                if i+1<len(intervals):
                    if newInterval[1] < intervals[i+1][0]:
                        print(4)
                        print("INDEX:", i)
                        # slucaj [3,5] -> [ [2,3] [6,7] ] -> [ [2,5], [6,7] ]
                        intervals[i][1] = newInterval[1]
                        return intervals
                    if newInterval[1] == intervals[i+1][0]:
                        print(5)
                        print("INDEX:", i)
                        # slucaj [3,5] -> [ [2,3] [5,7] ] -> [ [2,7] ]
                        newInterval = [intervals[i][0],intervals[i+1][1]]
                        intervals.pop(i+1)
                        intervals.pop(i)
                        intervals.insert(i,newInterval)
                        return intervals
                else:
                    newInterval = [intervals[i][0],newInterval[1]]
                    intervals.pop(i)
                    intervals.insert(i,newInterval)
                    return intervals
                   

                #              index   0      1.     2.     3
                # slucaj [2,10] -> [ [1,2], [4,5], [7,8], [9,11]] -> vraca 3
                # slucaj [2,10] -> [ [1,2], [4,5], [7,8], [9,10]] -> vraca -1
                # slucaj [2,10] -> [ [1,2], [4,5], [6,7], [8,9]]  -> vraca -1
                # slucaj [2,6]  -> [ [1,2], [4,5], [6,7], [8,9]]  -> vraca 2
                indexOfIntervalBiggerThanNewInterval = findBiggerIntervalIndex(newInterval,intervals,i)
                if indexOfIntervalBiggerThanNewInterval == -1:
                    print(6)
                    print("INDEX:", i, "indexOfIntervalBiggerThanNewInterval", indexOfIntervalBiggerThanNewInterval)
                    # slucaj [2,10] -> [ [1,2], [4,5], [7,8], [9,10]] -> vraca -1
                    # slucaj [2,10] -> [ [1,2], [4,5], [6,7], [8,9]]  -> vraca -1

                    # if index is -1 -> meaning j (or end) of new interval is bigger than ending of any other interval
                    print(newInterval)
                    newInterval = [intervals[i][0], newInterval[1]]
                    print(intervals)
                    del intervals[i:len(intervals)]
                    print(intervals)
                    intervals.insert(i,newInterval)
                    print(intervals)
                    return intervals
                # slucaj [2,10] -> [ [1,2], [4,5], [7,8], [9,11]] -> vraca 3
                # slucaj [2,6]  -> [ [1,2], [4,5], [6,7], [8,9]]  -> vraca 2
                print(7)
                print("INDEX:", i, "indexOfIntervalBiggerThanNewInterval", indexOfIntervalBiggerThanNewInterval)
                if newInterval[1] < intervals[indexOfIntervalBiggerThanNewInterval][0]:
                    newOverrideInterval = [intervals[i][0],max(newInterval[1],intervals[indexOfIntervalBiggerThanNewInterval-1][1])]
                    del intervals[i:indexOfIntervalBiggerThanNewInterval]
                    intervals.insert(i,newOverrideInterval)
                    return intervals
                newOverrideInterval = [intervals[i][0],intervals[indexOfIntervalBiggerThanNewInterval][1]]
                del intervals[i:indexOfIntervalBiggerThanNewInterval+1]
                intervals.insert(i,newOverrideInterval)
                return intervals
            if newInterval[0] < intervals[i][1]:
                if newInterval[1] < intervals[i][0]:
                    intervals.insert(i,newInterval)
                    return intervals
                if newInterval[1] <= intervals[i][1]:
                    print(8)
                    print("INDEX:", i)
                    # slucaj [3,6] -> [ [1,2] [5,7] ] -> [ [1,2], [5,7]]
                    newIntervalOverride = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
                    intervals.pop(i)
                    intervals.insert(i,newIntervalOverride)
                    return intervals
                if newInterval[1] > intervals[i][1]:
                    # slucaj [3,10] -> [ [1,2] [5,7] ] -> [ [1,2], [3,10]]
                    # slucaj [3,10] -> [ [1,2] [5,7], [9,10], [12,15] ] -> [[1,2], [3,10], [12,15]]
                    # new interval je [min(newInterval[0],intervals[i][0])]
                    indexOfIntervalBiggerThanNewInterval = findBiggerIntervalIndex(newInterval,intervals,i)
                    if indexOfIntervalBiggerThanNewInterval == -1:
                        print(9)
                        print("INDEX:", i, "indexOfIntervalBiggerThanNewInterval", indexOfIntervalBiggerThanNewInterval)
                        
                        newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
                        print(newInterval)
                        print(intervals)
                        del intervals[i:len(intervals)]
                        print(intervals)
                        intervals.insert(i,newInterval)
                        print(intervals)
                        return intervals
                    else:
                        print(10)
                        print("INDEX:", i, "indexOfIntervalBiggerThanNewInterval", indexOfIntervalBiggerThanNewInterval)
                        if newInterval[1] < intervals[indexOfIntervalBiggerThanNewInterval][0]:
                            print(10.1)
                            newOverrideInterval = [min(intervals[i][0],newInterval[0]),max(intervals[indexOfIntervalBiggerThanNewInterval-1][1],newInterval[1])]
                            del intervals[i:indexOfIntervalBiggerThanNewInterval]
                            intervals.insert(i,newOverrideInterval)
                            return intervals                              
                        newOverrideInterval = [min(intervals[i][0],newInterval[0]),intervals[indexOfIntervalBiggerThanNewInterval][1]]
                        if indexOfIntervalBiggerThanNewInterval-i <= 1:
                            if newInterval[1] < intervals[indexOfIntervalBiggerThanNewInterval][0]:
                                print(11)
                                print("INDEX:", i, "indexOfIntervalBiggerThanNewInterval", indexOfIntervalBiggerThanNewInterval)

                                # intervals[i][1] = newInterval[1]
                                newOverrideInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
                                intervals.pop(i)
                                intervals.insert(i,newOverrideInterval)
                                return intervals
                            elif newInterval[1] >= intervals[indexOfIntervalBiggerThanNewInterval][0]:
                                print(12)
                                print("INDEX:", i, "indexOfIntervalBiggerThanNewInterval", indexOfIntervalBiggerThanNewInterval)

                                newOverrideInterval = intervals[indexOfIntervalBiggerThanNewInterval][1]
                                newOverrideInterval = [min(intervals[i][0],newInterval[0]),max(intervals[indexOfIntervalBiggerThanNewInterval][1],newInterval[1])]
                                del intervals[i:indexOfIntervalBiggerThanNewInterval+1]
                                intervals.insert(i,newOverrideInterval)
                                return intervals
                        del intervals[i:indexOfIntervalBiggerThanNewInterval+1]
                        intervals.insert(i,newOverrideInterval)
                        return intervals                        
                    
