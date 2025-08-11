cmake_minimum_required(VERSION 3.14)
project(core_engine LANGUAGES CXX)

if(POLICY CMP0148)
    cmake_policy(SET CMP0148 NEW)
endif()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Enable more compiler warnings (optional)
add_compile_options(-Wall -Wextra -Wpedantic -Werror)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
# Detect pybind11 installation path
execute_process(
    COMMAND ${Python3_EXECUTABLE} -c "import pybind11; print(pybind11.__path__[0])"
    OUTPUT_VARIABLE PYBIND11_PATH
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE PYBIND11_RESULT
)

if(NOT PYBIND11_RESULT EQUAL 0)
    message(FATAL_ERROR "Failed to find pybind11 Python package")
endif()

set(pybind11_DIR "${PYBIND11_PATH}/share/cmake/pybind11")
message(STATUS "Using pybind11 from: ${pybind11_DIR}")

# Now find pybind11
find_package(pybind11 CONFIG REQUIRED)

# Include directories for headers
include_directories(${CMAKE_SOURCE_DIR}/include)

# Source files (for now only stub)
set(SOURCES
    src/detector.cpp
    src/pybind_module.cpp
)

# Create Python module
pybind11_add_module(core_engine MODULE ${SOURCES})

# Output .so to API core folder
set_target_properties(core_engine PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/../api_server/app/core
)

# If using OpenCV later
# find_package(OpenCV REQUIRED)
# target_link_libraries(core_engine PRIVATE ${OpenCV_LIBS})
