#include <iostream>
#include <fstream>

std::string url = "../text_input/day1.txt";

int main() {
    char ch;
    std::ifstream infile(url);
    std::string data;

    int part1(std::string data);
    
    if (!infile) {
        std::cerr << "File not found\n";
        return 1;
    } else {
        std::getline(infile, data);
    }
    infile.close();
    std::cout << part1(data) << "\n";;
    return 0;
}

int part1(std::string data) {
    int floor = 0;
    int basement = 0;
    bool isFalse = false;
    for (int i = 0; i < data.size(); i++) {
        if (data[i] == '(') {
            floor++;
        } else if (data[i] == ')') {
            floor--;
        } else {
            continue;
        }
        // Part 2
        if (floor == -1 && !isFalse) {
            basement = i;
            isFalse = true; // setting the flag to false will ensure the loop won't run after the 1st time
        }
    }
    return floor, basement;
}