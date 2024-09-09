#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"

char ssid[] = "oswNetw";
char pass[] = "gangTengah";

int main(){
    // Initialize library
    stdio_init_all();

    // Initialized the driver based on the country
    if(cyw43_arch_init_with_country(CYW43_COUNTRY('I', 'D', 0))){
        printf("Failed to initialise\n");
        return 1;
    }
    printf("Initialised\n");

    // Initialize the station mode
    cyw43_arch_enable_sta_mode();

    // Trying to connect to the WiFi Access Point
    if(cyw43_arch_wifi_connect_timeout_ms(ssid, pass, CYW43_AUTH_WPA2_AES_PSK, 10000)){
        printf("Failed to connect\n");
        return 1;
    }
    printf("Connected\n");
}