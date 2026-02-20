#include "led.h"
#include <Adafruit_NeoPixel.h>

static Adafruit_NeoPixel pixel(1, PIN_NEOPIXEL, NEO_GRB + NEO_KHZ800);

void ledInit() {
    pixel.begin();
    pixel.setBrightness(20); // dim — not blinding in the dark
    pixel.clear();
    pixel.show();
}

void ledSet(uint8_t r, uint8_t g, uint8_t b) {
    pixel.setPixelColor(0, pixel.Color(r, g, b));
    pixel.show();
}

void ledOff() {
    pixel.clear();
    pixel.show();
}

void ledBlink(uint8_t r, uint8_t g, uint8_t b, int count, int ms) {
    for (int i = 0; i < count; i++) {
        ledSet(r, g, b);
        delay(ms);
        ledOff();
        delay(ms);
    }
}
