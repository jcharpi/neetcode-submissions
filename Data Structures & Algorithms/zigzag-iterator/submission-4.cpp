class ZigzagIterator {
private:
    vector<int> arr;
    size_t curr_index = 0;
public:
    size_t i = 0;
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        arr.reserve(v1.size() + v2.size());

        while (i < v1.size() && i < v2.size()) {
            arr.push_back(v1[i]);
            arr.push_back(v2[i]);
            i++;
        }

        while (i < v1.size()) arr.push_back(v1[i++]);
        while (i < v2.size()) arr.push_back(v2[i++]);
    }

    int next() {
        return arr[curr_index++];
    }

    bool hasNext() {
        return curr_index < arr.size();
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */
