class Solution:
    # problem strs empty and not empty evaluate to the same thing but should decode to different result
    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        encoded = f"{length}%%" + "%%".join(strs)
        print(encoded)

        return f"{length}%%" + "%%".join(strs)
        

    def decode(self, s: str) -> List[str]:
        text = s.split("%%")
        print(text)
        length = int(text[0])
        if length < 1:
            return []
        text.pop(0)
        return text
        
