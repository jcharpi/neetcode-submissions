class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Given
        # int hand[i] == value of ith card
        # int groupSize = target size of a group

        # Goal
        # create groups of cards from hand
        # - each group must be groupSize
        # - cards in group must increase consecutively by 1

        # return true if it is possible to arrange cards in this way, else false

        # Gut reaction
        # immediately thinking bool dp, dp[i] = can we make groups while considering hand[0:i]
        # - when we think dp, we should consider Greedy

        # Questions
        # What is the decision we are making at each index?
        # - sort values first, then we can arrange min elements into groups
        # -- this is because if a value is already part of a group, and there are no smaller elements, then we need it to be the start of another group i.e. it will never fit as anything else
        # --- aim to put min element into a group if group needs more to == groupSize, otherwise start a new group

        # Solution
        # - if len(hand) % groupSize != 0, return False
        # - how do we actually code this?
        # -- what do we need to know at each step?
        # -- track counts of each value in hash map val : count
        # --- for each count we need count, count + 1 ... count + groupSize
        # ---- can check if we have that, if we dont, return false; if we do, decrement count for each val
        
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        val_counts = Counter(hand)
        print(val_counts)
        for i, val in enumerate(hand):
            if val_counts[val] == 0:
                continue
            elif val_counts[val] > 0:
                count = val_counts[val]
                for offset in range(groupSize):
                    if val_counts[val + offset] < count:
                        return False
                    val_counts[val + offset] -= count
        return True