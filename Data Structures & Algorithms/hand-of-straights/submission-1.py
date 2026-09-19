class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:   
        if len(hand) % groupSize != 0:
            return False
        
        card_counts = Counter(hand)
        for card_value in sorted(card_counts):
            card_count = card_counts[card_value]
            if card_count == 0:
                continue
            for offset in range(groupSize):
                card_needed = card_value + offset
                if card_counts[card_needed] < card_count:
                    return False
                card_counts[card_needed] -= card_count
        return True