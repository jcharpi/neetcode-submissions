public class Solution {
    public int NumRescueBoats(int[] people, int limit) {
        Array.Sort(people);
        Array.Reverse(people);

        
        foreach (int person in people) {
            Console.WriteLine(person);
        }

        int l = 0, r = people.Length - 1;
        int result = 0;
        while (l <= r) {
            if (people[l] + people[r] <= limit) {
                r--;
            }
            result++;
            l++;
        }
        return result;
    }
}