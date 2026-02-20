#pragma once
#include "config.h"

void ledInit();
void ledSet(uint8_t r, uint8_t g, uint8_t b);
void ledOff();
void ledBlink(uint8_t r, uint8_t g, uint8_t b, int count, int ms = 200);
