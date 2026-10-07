class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire, radiant, n = deque(), deque(), len(senate)
        for i, senator in enumerate(senate):
            if senator == "R":
                radiant.append(i)
            else:
                dire.append(i)

        round = 1
        while dire and radiant:
            curr_dire = dire.popleft()
            curr_radiant = radiant.popleft()
            
            # vote off the radiant: add it back with + 2?
            if curr_dire < curr_radiant:
                dire.append(curr_dire + n)
            else:
                radiant.append(curr_radiant + n)
        return "Dire" if dire else "Radiant"
        