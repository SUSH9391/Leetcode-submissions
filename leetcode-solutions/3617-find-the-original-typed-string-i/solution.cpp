class Solution {
public:
    int possibleStringCount(string word) {
      int total = 1; // the unchanged word is always valid
    int n = word.size();
    int i = 0;

    while (i < n) {
        int j = i;
        while (j < n && word[j] == word[i]) j++;
        int len = j - i;
        if (len > 1) {
            total += (len - 1); // reducing this group gives (len - 1) new options
        }
        i = j;
    }

    return total;
    }
};
