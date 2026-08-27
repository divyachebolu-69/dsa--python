class Solution:
    def compareStrings(self, str1, str22):
        return str1 == str22

if __name__ == "__main__":
    str1 = input()

    str2 = input()

    obj = Solution()

    if obj.compareStrings(str1, str2):
        print("Strings are equal")
    else:
        print("Strings are not equal")