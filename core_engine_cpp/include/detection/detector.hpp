#pragma once
#include <string>
#include <vector>

struct Detection {
    int id;
    std::string label;
    std::vector<int> bbox; // x, y, w, h
    float score;
};

std::vector<Detection> detect_from_image(const std::string &image_path);
