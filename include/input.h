#pragma once
#include "config.h"

class Button {
public:
    void init(uint8_t pin);
    void update();
    bool tapped() const { return _tap; }
    bool held() const   { return _held; }
    bool down() const   { return !digitalRead(_pin); }
    void reset();

private:
    uint8_t  _pin = 0;
    bool     _prev = true;
    bool     _tap = false;
    bool     _held = false;
    bool     _heldFired = false;
    uint32_t _downAt = 0;
    uint32_t _lastTap = 0;
};

// Global button instances
extern Button btnUp, btnDn, btnBk, btnRt, btnOk;

void inputInit();
void inputUpdate();      // call once per frame
bool emergencyCombo();   // UP+DN held > 400ms
