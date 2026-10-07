public class Solution {
    public string PredictPartyVictory(string senate) {
        Queue<int> dire = new(), radiant = new();
        int n = senate.Length;

        for (int i = 0; i < n; i++) {
            if (senate[i] == 'R') radiant.Enqueue(i);
            else dire.Enqueue(i);
        }

        while (dire.Count > 0 && radiant.Count > 0) {
            int currDire = dire.Dequeue(), currRadiant = radiant.Dequeue();
            if (currDire < currRadiant) dire.Enqueue(currDire + n);
            else radiant.Enqueue(currRadiant + n);
        }

        return dire.Count > 0 ? "Dire" : "Radiant";
    }
}