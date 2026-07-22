class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> entries;
    TimeMap() {};
    
    void set(string key, string value, int timestamp) {
        entries[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        // search entries for key
        // go through array until we find the latest timestamp possible
        // need to search through all timestamps in array (use binary search)
        // why can't we ensure ordering at insertion time?
        int left = 0, right = entries[key].size() - 1;
        string out = "";
        while (left <= right) {
            int mid = (left + right) / 2;
            pair<int, string> entry = entries[key][mid];
            if (timestamp >= entry.first) {
                out = entry.second;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return out;
    }
};
