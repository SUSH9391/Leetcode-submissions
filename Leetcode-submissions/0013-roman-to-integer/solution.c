#include <stdio.h>

// function to convert a single Roman numeral character to an integer value
int romanCharToInt(char c) {
    switch (c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0; // return 0 for invalid characters
    }
}

// function to convert a Roman numeral string to an integer value
int romanToInt(char* s) {
    int result = 0;
    int i;

    for (i = 0; s[i] != '\0'; i++) {
        int current = romanCharToInt(s[i]);
        int next = romanCharToInt(s[i + 1]);

        if (next > current) {
            result += (next - current);
            i++; // skip the next character since we've already processed it
        } else {
            result += current;
        }
    }

    return result;
}


