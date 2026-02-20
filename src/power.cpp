#include "power.h"

static uint32_t lastActivity = 0;
static uint8_t blState = 2; // 2=full, 1=dim, 0=off

void powerInit() {
    pinMode(PIN_DISP_BL, OUTPUT);
    analogWrite(PIN_DISP_BL, BL_FULL);
    lastActivity = millis();
    blState = 2;
}

void powerTouch() {
    lastActivity = millis();
    if (blState < 2) {
        analogWrite(PIN_DISP_BL, BL_FULL);
        blState = 2;
    }
}

void powerTick() {
    uint32_t elapsed = millis() - lastActivity;
    if (blState == 2 && elapsed > DIM_TIMEOUT_MS) {
        analogWrite(PIN_DISP_BL, BL_DIM);
        blState = 1;
    } else if (blState >= 1 && elapsed > SLEEP_TIMEOUT_MS) {
        analogWrite(PIN_DISP_BL, BL_OFF);
        blState = 0;
    }
}

bool powerSleeping() {
    return blState == 0;
}

void powerSleep() {
    analogWrite(PIN_DISP_BL, BL_OFF);
    blState = 0;
}

void powerWake() {
    powerTouch();
}
