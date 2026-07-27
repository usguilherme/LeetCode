class Solution(object):
    def reverseString(self, s):
        metade = len(s) // 2
        tamanho = len(s) - 1
        for i in range(metade):
            s[i], s[tamanho] = s[tamanho], s[i]
            tamanho-= 1

        return s



if __name__ == "__main__":
    sol = Solution()
    resultado = sol.reverseString(["H","a","n","n","a","h"])
    print(resultado)