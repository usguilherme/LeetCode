class Solution(object):
    def maxProfit(self, prices):
        menor = prices[0]
        maior_lucro = 0
        for preco in prices:
            if preco < menor:
                menor = preco 
            lucro = preco - menor

            if lucro > maior_lucro:
                maior_lucro = lucro

        return maior_lucro
        
                
if __name__ == "__main__":
    sol = Solution()
    resultado = sol.maxProfit([7,1,5,3,6,4])
    print(resultado)
                
        