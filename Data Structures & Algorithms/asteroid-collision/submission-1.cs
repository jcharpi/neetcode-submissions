public class Solution {
    public int[] AsteroidCollision(int[] asteroids) {
        Stack<int> survivingAsteroids = new();

        foreach (int asteroid in asteroids) {
            int incomingSize = Math.Abs(asteroid);
            bool isIncomingDestroyed = false;

            while (!isIncomingDestroyed && survivingAsteroids.Count > 0 && WillCollide(survivingAsteroids.Peek(), asteroid)) {
                int topSize = survivingAsteroids.Peek();
                if (topSize <= incomingSize) {
                    survivingAsteroids.Pop();
                }
                isIncomingDestroyed = topSize >= incomingSize;
            }

            if (!isIncomingDestroyed) {
                survivingAsteroids.Push(asteroid);
            }
        }

        int[] result = survivingAsteroids.ToArray();
        Array.Reverse(result);
        return result;
    }

    private static bool WillCollide(int leftAsteroid, int rightAsteroid) {
        return leftAsteroid > 0 && rightAsteroid < 0;
    }
}