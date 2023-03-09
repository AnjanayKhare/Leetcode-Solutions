class Solution:
    def findDuplicate(self, arr: List[int]) -> int:

        if len(arr) == 2:
            return 1
        

        slow = arr[arr[0]]
        fast = arr[arr[arr[0]]]
        


        while fast != slow:
            fast = arr[arr[fast]]
            slow = arr[slow]
        fast = arr[0]
        while fast !=slow:
            fast = arr[fast]
            slow = arr[slow]
        return fast
