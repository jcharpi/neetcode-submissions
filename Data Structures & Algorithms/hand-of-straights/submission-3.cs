public class Solution {
    public bool IsNStraightHand(int[] hand, int groupSize) {
        if (hand.Length % groupSize != 0) return false;

        Dictionary<int, int> cardCounts = new Dictionary<int, int>();
        foreach (int cardValue in hand) {
            cardCounts.TryGetValue(cardValue, out int currentCount);
            cardCounts[cardValue] = currentCount + 1;
        }

        foreach (int cardValue in cardCounts.Keys.Order()) {
            cardCounts.TryGetValue(cardValue, out int cardCount);
            if (cardCount == 0) continue;
            for (int offset = 0; offset < groupSize; offset++) {
                int cardNeeded = cardValue + offset;
                cardCounts.TryGetValue(cardNeeded, out int cardNeededCount);
                if (cardNeededCount < cardCount) return false;
                cardCounts[cardNeeded] -= cardCount;
            }
        }
        return true;
    }
}
