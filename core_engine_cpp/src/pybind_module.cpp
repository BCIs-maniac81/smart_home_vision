#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // for returning std::vector / std::map
#include <string>
#include <vector>
#include <stdexcept>
#include "detection/detector.hpp"  // Include the header instead of redefining

namespace py = pybind11;

PYBIND11_MODULE(core_engine, m) {
    m.doc() = "Core detection engine";

    py::class_<Detection>(m, "Detection")
        .def_readonly("id", &Detection::id)
        .def_readonly("label", &Detection::label)
        .def_readonly("bbox", &Detection::bbox)
        .def_readonly("score", &Detection::score);

    m.def("detect_from_image", &detect_from_image, "Run detection on an image");
}
