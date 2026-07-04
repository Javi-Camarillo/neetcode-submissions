class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import Counter
        cnt = Counter(students)           # counts of 0 and 1
        
        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
            else:
                break
        
        return cnt[0] + cnt[1]