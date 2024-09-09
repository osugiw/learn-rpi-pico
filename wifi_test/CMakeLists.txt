cmake_minimum_required(VERSION 3.13)

# Inlude PICO_SDK
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

# Declare the project requirements
project(wifi_test C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Initialise PICO_SDK library
pico_sdk_init()

# Source files
add_executable(wifi_test 
    main.c
)

# Enable USB and UART features
pico_enable_stdio_usb(wifi_test 1)
pico_enable_stdio_uart(wifi_test 1)

pico_add_extra_outputs(wifi_test)

# Include other file in the current directory
target_include_directories(wifi_test PRIVATE $(CMAKE_CURRENT_LIST_DIR))

# Link neccessary libraries to the project
target_link_libraries(wifi_test pico_cyw43_arch_lwip_threadsafe_background pico_stdlib)