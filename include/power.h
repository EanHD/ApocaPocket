#pragma once
#include "config.h"

void powerInit();
void powerTouch();   // reset idle timer on any input
void powerTick();    // check dim/sleep, call each frame
bool powerSleeping();
void powerSleep();   // force sleep now
void powerWake();    // force wake
