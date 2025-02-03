#include <iostream>
#include <fstream>

std::string url = "../text_input/day1.txt";

int main() {
    char ch;
    std::ifstream infile(url);
    std::string data;
    
    if (!infile) {
        std::cerr << "File not found\n";
        return 1;
    } else {
        std::getline(infile, data);
    }
    std::cout << data << "\n";

    infile.close();
    return 0;
}