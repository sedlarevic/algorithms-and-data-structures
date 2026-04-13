"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#intervals=[(5,10),(0,4),(4,5),(6,10),(12,15)]
#   0->4 4->5 5->10 12->15

import operator

"""
Operator biblioteka je korisna zato sto nam daje funkcije koje rade isto sto 
i operatori u Python-u.

a + b
operator.add(a, b)
a > b
operator.gt(a, b)
obj.x
operator.attrgetter('x')(obj)

Dakle attrgetter pravi funkciju koja za objekat vraca (obj,start,obj.end)
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        """
        operator.attrgetter('start','end') radi isto sto i ovo
        
        def key_func(obj):
            return (obj.start, obj.end)
        
        Dakle vraca tuple, a ne Interval(x,y).
        Sorted sada poredi po tuple-u, a ne po Interval objektu.
        
        Python sorted poredi tuple element ovako -> 
        Poredi prvi element, ako su isti, poredi drugi element i onda sortira.
        """
        sorted_intervals= sorted(intervals, key=operator.attrgetter('start', 'end'))

        i = 0
        until = len(sorted_intervals)-2
        while i<=until:
            if sorted_intervals[i].end >sorted_intervals[i+1].start:
                return False
            else:
                i += 1
        return True
