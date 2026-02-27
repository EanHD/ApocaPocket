---
id: l3-tech-emergency-comms
title: Emergency Commss
layer: L3_materials_technology
category: communications
tags:
- emergency_communications
- protocols
- phonetic_alphabet
- brevity_codes
- net_control
- ARES
- RACES
- ICS
region_relevance:
- global
summary: "Standardized emergency communication protocols ensure clear, efficient message exchange during crises. Covers NATO phonetic alphabet (pronunciation guide), brevity codes (10-codes, Q-codes, prowords), distress signals (MAYDAY, PAN-PAN, SCURIT urgency levels), radio discipline (clear speech, brevity, listening protocols), net control operations (check-ins, message traffic, priority handling), and integration with ARES/RACES amateur radio emergency services and ICS (Incident Command System)."
steps:
- "Learn and practice NATO phonetic alphabet for spelling names, locations, callsigns without ambiguity (Alpha, Bravo, Charlie...)"
- "Memorize essential brevity codes: 10-4 (acknowledged), 10-20 (location), 10-33 (emergency traffic), Q-codes for ham radio"
- "Understand distress signal hierarchy: MAYDAY (life-threatening), PAN-PAN (urgent non-life-threatening), SCURIT (safety information)"
- "Practice radio discipline: Listen before transmitting, speak clearly and slowly, use brevity, avoid unnecessary transmissions"
- "Participate in practice nets weekly: Learn net control procedures, check-in protocols, message handling (preamble, text, signature)"
- "Complete ICS training (ICS-100, ICS-200, ICS-700) for integration with formal emergency management (FEMA free online courses)"
warnings:
- "FALSE DISTRESS CALLS: Transmitting MAYDAY or activating EPIRB (Emergency Position Indicating Radio Beacon) when no emergency exists is federal crime (FCC/Coast Guard fine $10,000-100,000, possible imprisonment). Use correct urgency level: MAYDAY = life-threatening only, PAN-PAN = urgent but not life-threatening"
- "HOAX EMERGENCY TRAFFIC: Falsely claiming emergency status to gain priority on frequency disrupts real emergencies and violates FCC Part 97.113. Penalties include license revocation and criminal prosecution"
- "EAVESDROPPING ON EMERGENCY TRAFFIC: Legal to monitor, but DO NOT retransmit/relay without authorization (violates third-party traffic rules in many jurisdictions). Exception: Immediate life-threatening situation where you are the only relay available"
- "OPERATIONAL SECURITY (OPSEC): Never transmit sensitive information unencrypted (locations of resources, personnel names, medical details, security plans). Use coded messages, pre-arranged brevity codes, or secure communications (Winlink with AES, phone via VOIP). Adversaries/criminals monitor emergency frequencies"
- "NET DISCIPLINE VIOLATIONS: Transmitting out of turn, interrupting net control, excessive transmissions (rag-chewing) degrades emergency net efficiency. Follow net control instructions exactly. If you must interrupt for emergency, use 'BREAK BREAK BREAK' prefix only"
- "FATIGUE & ERRORS: Extended net operations (12-24+ hour shifts) cause operator fatigue, increased errors (wrong frequencies, missed messages, poor copy). Rotate operators every 4-6 hours, enforce rest periods, maintain alertness"
related_entries:
- l3-tech-radio-basics
- l3-tech-antenna-construction
- l3-tech-digital-radio
- l3-tech-propagation
sources:
- ARRL Emergency Communications Handbook
- FEMA ICS training materials (ICS-100, ICS-200, ICS-700, ICS-800)
- ARRL ARES Field Resources Manual
- FEMA AUXCOMM guidance
- ITU Radio Regulations Appendix (phonetic alphabet, Q-codes)
- U.S. Coast Guard Communications Manual
audit_status: verified
last_verified: 2026-02-19
confidence: high
offline_assets: []
---

# Emergency Comms

## Priority Channels

FRS (no license): channels 1-14, 462-467 MHz. Range 0.5-2 miles. Default group channel: 1 at 462.5625 MHz.
GMRS (license $35): channels 1-22. Up to 50W. Range 5-25 miles. Repeater access on channels 15-22.
MURS (no license): 5 VHF channels, 151-154 MHz. 2W max. Better building penetration than FRS.
  Ch 1: 151.820 / Ch 2: 151.880 / Ch 3: 151.940 / Ch 4: 154.570 / Ch 5: 154.600
CB (no license): channel 9 = emergency and motorist assist. Channel 19 = truckers and highway. 4W AM.
Marine VHF (vessels): channel 16 at 156.800 MHz = international distress and calling. Monitor always.
Ham simplex: 146.520 MHz national 2m calling. License required to transmit.

## Emergency Freqs

156.800 MHz       - Marine Ch 16 (distress, Coast Guard monitored)
462.675 MHz       - GMRS Ch 20 (national emergency and calling)
146.520 MHz       - 2m ham simplex national calling
27.065 MHz        - CB channel 9 (emergency)
155.340 MHz       - National Interop (public safety)
162.400-162.550   - NOAA Weather (7 channels, scan for strongest)

## Phonetic Alphabet

A=Alpha   B=Bravo   C=Charlie  D=Delta   E=Echo    F=Foxtrot  G=Golf
H=Hotel   I=India   J=Juliet   K=Kilo    L=Lima    M=Mike     N=November
O=Oscar   P=Papa    Q=Quebec   R=Romeo   S=Sierra  T=Tango    U=Uniform
V=Victor  W=Whiskey X=X-ray    Y=Yankee  Z=Zulu

## Calling for Help

MAYDAY call (voice, life-threatening emergency):
"MAYDAY MAYDAY MAYDAY, this is [callsign/name], [location], [nature of emergency], [number of persons], requesting [assistance]."
Repeat 3 times. Release PTT. Listen for response. Repeat every few minutes if no answer.

PAN-PAN: urgent but not life-threatening. Same format, replace MAYDAY with PAN-PAN.
SECURITE: safety broadcast only (navigation hazard). Use on Marine channel 16.
CB emergency: "BREAK BREAK, this is [vehicle] at [location], need emergency assistance."
FRS/MURS: state location first. Keep transmissions under 30 seconds. Speak slowly and clearly.

## Simplex vs Repeater

Simplex: direct radio-to-radio. No infrastructure. Works when all infrastructure is down. Range is line-of-sight.
Repeater: receives on one frequency, retransmits on another. Extends range to 50-100 or more miles.
  2m offset: plus or minus 600 kHz. 70cm offset: plus or minus 5 MHz.
  CTCSS/PL tone required to access most repeaters. Common tones: 100.0, 127.3, 136.5 Hz.
  Repeater down: switch to its input frequency for short-range simplex use.

Net check-in: "NET CONTROL, this is [callsign], [location], [traffic or no traffic]."
Emergency break: say BREAK BREAK BREAK then state emergency. All stations clear frequency.
