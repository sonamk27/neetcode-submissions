class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for ch in s1:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1

        for i in range(len(s1)):
            ch = s2[i]

            if ch in count2:
                count2[ch] += 1
            else:
                count2[ch] = 1

        if count1 == count2:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            ch = s2[right]

            if ch in count2:
                count2[ch] += 1
            else:
                count2[ch] = 1

            left_char = s2[left]
            count2[left_char] -= 1

            if count2[left_char] == 0:
                del count2[left_char]

            left += 1

            if count1 == count2:
                return True

        return False
        