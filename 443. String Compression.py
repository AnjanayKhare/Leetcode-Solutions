class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        cnt = 1
        last = chars[0]
        n = len(chars)
        for j in range(1, n):
            if last == chars[j]:
                cnt+=1
            else:
                print(i, )
                if cnt == 1:
                    chars[i] = last
                    i+=1
                else:
                    chars[i] = last
                    i+=1
                    for c in str(cnt):
                        chars[i] = c
                        i+=1
                cnt = 1
                last = chars[j]
        if cnt == 1:
            chars[i] = last
            i+=1
        else:
            chars[i] = last
            i+=1
            for c in str(cnt):
                chars[i] = c
                i+=1
        return i
