class ZigzagIterator {
public:
    vector<int> arr;
    int curr_index = 0;
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        while (curr_index < v1.size() && curr_index < v2.size()) {
            arr.push_back(v1[curr_index]);
            arr.push_back(v2[curr_index]);
            curr_index++;
        }

        while (curr_index < v1.size()) {
            arr.push_back(v1[curr_index]);
            curr_index++;
        }

        while (curr_index < v2.size()) {
            arr.push_back(v2[curr_index]);
            curr_index++;
        }

        curr_index = 0;
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
