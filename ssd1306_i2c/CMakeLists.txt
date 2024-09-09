cmake_minimum_required(VERSION 3.13)

# Include PICO_SDK
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

# Declare the project requirements
project(ssd1306_i2c C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Initialise PICO_SDK library
pico_sdk_init()

add_executable(${PROJECT_NAME}
        ssd1306_i2c.c
)

# pull in common dependencies and additional i2c hardware support
target_link_libraries(${PROJECT_NAME} 
        pico_stdlib 
        hardware_i2c
)

# create map/bin/hex file etc.
pico_add_extra_outputs(${PROJECT_NAME})

# Enable USB and UART features
pico_enable_stdio_usb(${PROJECT_NAME} 1)
pico_enable_stdio_uart(${PROJECT_NAME} 0)