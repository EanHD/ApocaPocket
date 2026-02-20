#include "input.h"

Button btnUp, btnDn, btnBk, btnRt, btnOk;
static uint32_t comboStart = 0;
static bool comboFired = false;

void Button::init(uint8_t pin) {
    _pin = pin;
    pinMode(_pin, INPUT_PULLUP);
    _prev = true;
    _tap = false;
    _held = false;
    _heldFired = false;
    _downAt = 0;
    _lastTap = 0;
}

void Button::update() {
    bool v = !digitalRead(_pin);
    uint32_t now = millis();
    _tap = false;
    _held = false;

    // Just pressed
    if (v && !_prev) {
        _downAt = now;
        _heldFired = false;
    }
    // Held long enough
    if (v && _downAt > 0 && !_heldFired && (now - _downAt) > 500) {
        _held = true;
        _heldFired = true;
    }
    // Just released
    if (!v && _prev && _downAt > 0) {
        if (!_heldFired && (now - _lastTap) > 150) {
            _tap = true;
            _lastTap = now;
        }
        _downAt = 0;
    }
    _prev = v;
}

void Button::reset() {
    _prev = true;
    _tap = false;
    _held = false;
    _heldFired = false;
    _downAt = 0;
}

void inputInit() {
    btnUp.init(PIN_BTN_UP);
    btnDn.init(PIN_BTN_DN);
    btnBk.init(PIN_BTN_BK);
    btnRt.init(PIN_BTN_RT);
    btnOk.init(PIN_BTN_OK);
}

void inputUpdate() {
    btnUp.update();
    btnDn.update();
    btnBk.update();
    btnRt.update();
    btnOk.update();
}

bool emergencyCombo() {
    if (btnUp.down() && btnDn.down()) {
        if (comboStart == 0) comboStart = millis();
        else if (!comboFired && (millis() - comboStart) > 400) {
            comboFired = true;
            return true;
        }
    } else {
        comboStart = 0;
        comboFired = false;
    }
    return false;
}
