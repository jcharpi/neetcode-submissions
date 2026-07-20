class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars(position.size());
        for (int i = 0; i < position.size(); i++) cars[i] = {position[i], speed[i]};

        sort(cars.begin(), cars.end(), greater<>());

        vector<double> pending_fleets;
        for (auto& car : cars) {
            int position = car.first;
            int speed = car.second;
            double time_to_dest = double(target - position) / speed;
            if (pending_fleets.empty() || pending_fleets.back() < time_to_dest) {
                pending_fleets.push_back(time_to_dest);
            }
        }

        return pending_fleets.size();
    }
};
