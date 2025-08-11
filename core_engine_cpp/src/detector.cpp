#include "detection/detector.hpp"
#include <iostream>

std::vector<Detection> detect_from_image(const std::string& image_path) {
    std::cout << "Mock detect_from_image called with: " << image_path << std::endl;

    return {
        {1, "person", {100, 120, 60, 180}, 0.98f},
        {2, "dog",    {200, 150, 80, 120}, 0.87f}
    };
}
