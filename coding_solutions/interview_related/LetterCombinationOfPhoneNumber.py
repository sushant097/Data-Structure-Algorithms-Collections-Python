
dic = {
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
            "0":""
        }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        results = [""]
        for d in digits:
            chars = dic[d]
            new_results = []
            for c in chars:
                for r in results:
                    new_results.append(r+c)
            results = new_results
        
        return results
    