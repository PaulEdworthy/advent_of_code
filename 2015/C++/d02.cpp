#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

std::string url = "../input/day2.txt";
std::vector<int> split(const std::string& line);

// 2*l*w + 2*w*h + 2*h*l + area of the smallest side - my total 1588178

int main() {
    std::ifstream infile(url);
    std::string line;
    int total = 0;
    int ribbon = 0;

    if (!infile) {
        std::cerr << "File not found\n";
        return 1;
    }
    while (std::getline(infile, line)) {
        std::vector<int> dims = split(line);
        int l = dims[0];
        int w = dims[1];
        int h = dims[2];
        int a = l * w;
        int b = w * h;
        int c = h * l;
        int area = l * w * h;
        int smallestSide = std::min (a, std::min(b, c));
        // int smallestRibbon = std::min ((2 * a), std::min((2 * b), (2 * c)));

        total += ((2 * l * w) + (2 * w * h) + (2 * h * l) + smallestSide);
        // ribbon += area;
        // total += ribbon;
    }
    std::cout << "Total Area: " << total << "\n";
    return 0;

}
std::vector<int> split(const std::string& line) {
    std::vector<int> dimensions;
    std::stringstream ss(line);
    std::string dims;

    while (std::getline(ss, dims, 'x')) {
        dimensions.push_back(std::stoi(dims));
    }
    return dimensions;
}