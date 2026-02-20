---
id: l3-tech-emergency-comms
title: "Emergency Communications Protocols: Operating Procedures"
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
summary: "Standardized emergency communication protocols ensure clear, efficient message exchange during crises. Covers NATO phonetic alphabet (pronunciation guide), brevity codes (10-codes, Q-codes, prowords), distress signals (MAYDAY, PAN-PAN, SÉCURITÉ urgency levels), radio discipline (clear speech, brevity, listening protocols), net control operations (check-ins, message traffic, priority handling), and integration with ARES/RACES amateur radio emergency services and ICS (Incident Command System)."
steps:
  - "Learn and practice NATO phonetic alphabet for spelling names, locations, callsigns without ambiguity (Alpha, Bravo, Charlie...)"
  - "Memorize essential brevity codes: 10-4 (acknowledged), 10-20 (location), 10-33 (emergency traffic), Q-codes for ham radio"
  - "Understand distress signal hierarchy: MAYDAY (life-threatening), PAN-PAN (urgent non-life-threatening), SÉCURITÉ (safety information)"
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

## Overview

**Emergency communications protocols** provide standardized procedures for clear, efficient radio operations during disasters. Protocols reduce confusion, ensure message accuracy, and enable interoperability between different organizations (ham radio, public safety, military).

**Why Protocols Matter**:
- **Clarity**: Phonetic alphabet eliminates spelling errors ("B" vs "D" vs "T" sound alike, "Bravo" vs "Delta" vs "Tango" are distinct)
- **Efficiency**: Brevity codes convey complex information in 2-3 words ("10-20" = "What is your location?" + response in seconds, not 20+ second conversation)
- **Priority**: Distress signals immediately identify life-threatening situations (MAYDAY = drop everything, respond now)
- **Interoperability**: Standardized procedures allow different groups to work together without confusion (ham ARES, fire, police, hospital all understand same protocols)
- **Error Reduction**: Structured message format (preamble, text, signature) ensures all critical information transmitted

This guide covers **six essential protocol categories**:

1. **Phonetic Alphabet**: Spelling without ambiguity
2. **Brevity Codes**: 10-codes, Q-codes, prowords
3. **Distress Signals**: MAYDAY, PAN-PAN, SÉCURITÉ
4. **Radio Discipline**: Clear speech, listening, brevity
5. **Net Control Operations**: Check-ins, message traffic, priority
6. **ARES/RACES Integration**: Amateur radio emergency services, ICS structure

## NATO Phonetic Alphabet

**Purpose**: Spell words letter-by-letter without confusion. Critical for callsigns, names, locations, grid coordinates.

**Alphabet**:
| Letter | Word | Pronunciation | Letter | Word | Pronunciation |
|--------|------|---------------|--------|------|---------------|
| **A** | Alpha | AL-FAH | **N** | November | NO-VEM-BER |
| **B** | Bravo | BRAH-VOH | **O** | Oscar | OSS-CAH |
| **C** | Charlie | CHAR-LEE | **P** | Papa | PAH-PAH |
| **D** | Delta | DELL-TAH | **Q** | Quebec | KEH-BECK |
| **E** | Echo | ECK-OH | **R** | Romeo | ROW-ME-OH |
| **F** | Foxtrot | FOKS-TROT | **S** | Sierra | SEE-AIR-AH |
| **G** | Golf | GOLF | **T** | Tango | TANG-GO |
| **H** | Hotel | HOH-TELL | **U** | Uniform | YOU-NEE-FORM |
| **I** | India | IN-DEE-AH | **V** | Victor | VIK-TAH |
| **J** | Juliett | JEW-LEE-ETT | **W** | Whiskey | WISS-KEY |
| **K** | Kilo | KEY-LOH | **X** | X-ray | ECKS-RAY |
| **L** | Lima | LEE-MAH | **Y** | Yankee | YANG-KEY |
| **M** | Mike | MIKE | **Z** | Zulu | ZOO-LOO |

**Numbers**:
| Number | Word | Pronunciation | Number | Word | Pronunciation |
|--------|------|---------------|--------|------|---------------|
| **0** | Zero | ZEE-RO | **5** | Five | FIFE |
| **1** | One | WUN | **6** | Six | SIX |
| **2** | Two | TOO | **7** | Seven | SEV-EN |
| **3** | Three | TREE | **8** | Eight | AIT |
| **4** | Four | FOW-ER | **9** | Nine | NIN-ER |

**Usage Examples**:

**Spelling Callsign**:
- "My callsign is Whiskey One Alpha Bravo Charlie"
- (W1ABC)

**Spelling Name**:
- "My name is John, spelled: Juliett, Oscar, Hotel, November"
- (Avoids confusion: "Jon", "Jean", "Joan" all sound similar)

**Spelling Location**:
- "Location: Sierra Hotel Echo Lima Tango Echo Romeo"
- (SHELTER)

**Grid Square** (Maidenhead locator):
- "Grid square: Foxtrot November Four Two Delta Quebec"
- (FN42DQ)

### Common Mistakes

- ❌ **Using non-standard words**: "A as in Apple", "B as in Boy" (not universally understood, varies by language/culture)
- ✓ **Use NATO standard**: Alpha, Bravo (internationally recognized, consistent)
- ❌ **Rushing pronunciation**: "AlphBravCharliDelt" (blurs together, defeats purpose)
- ✓ **Slow, clear pronunciation**: Pause between each word, emphasize syllables
- ❌ **Mixing phonetic and plain letters**: "Alpha B Charlie" (inconsistent, confusing)
- ✓ **All phonetic or all plain**: If using phonetic alphabet, spell entire word phonetically

### Practice Drill

**Daily Practice** (5 minutes):
1. Spell your name using phonetic alphabet
2. Spell your callsign (if ham operator)
3. Spell your street address
4. Spell a random 6-character grid square
5. Listen to someone else spell word phonetically, write it down, verify accuracy

**Result**: After 1-2 weeks daily practice, phonetic alphabet becomes automatic (no conscious thought required).

## Brevity Codes

**Brevity codes** replace common phrases with short codes, saving time and reducing channel congestion.

### 10-Codes (Law Enforcement / Public Safety Origin)

**Common 10-Codes**:
| Code | Meaning | Usage |
|------|---------|-------|
| **10-4** | Acknowledged, understood | "10-4, message received" |
| **10-9** | Repeat, say again | "10-9, you were unreadable" |
| **10-20** | Location | "What is your 10-20?" = "Where are you?" |
| **10-33** | Emergency traffic | "10-33, need immediate assistance" |
| **10-36** | Correct time | "10-36 is 1530 hours" |
| **10-55** | Intoxicated driver | (Law enforcement specific) |
| **10-66** | Suspicious person | (Law enforcement specific) |
| **10-97** | Arrived at scene | "10-97 at shelter" |
| **10-98** | Completed assignment | "10-98, returning to base" |

**Limitations**:
- **Not standardized**: Meanings vary by region, agency, country (10-33 = emergency in some areas, 10-33 = traffic advisory in others)
- **Confusing in multi-agency operations**: Fire, police, EMS, ham operators may use different 10-code definitions
- **Decreasing use**: Many agencies moving away from 10-codes toward **plain language** (NIMS/ICS recommendation)

**Alternative**: Use **plain language** for emergency communications (e.g., "Emergency, need immediate assistance" instead of "10-33"). Clearer for multi-agency operations.

### Q-Codes (Amateur Radio Origin)

**Q-codes** originated in maritime radio, now used extensively in amateur radio. Internationally recognized.

**Common Q-Codes**:
| Code | Question | Answer/Statement |
|------|----------|------------------|
| **QRL** | Is this frequency in use? | This frequency is in use (QRL = "occupied") |
| **QRM** | Are you being interfered with? | I am being interfered with (by other stations) |
| **QRN** | Are you troubled by static? | I am troubled by static (atmospheric noise) |
| **QRP** | Shall I decrease power? | Decrease power / I am running low power (<10W) |
| **QRQ** | Shall I send faster? | Send faster (increase CW speed) |
| **QRS** | Shall I send slower? | Send slower (decrease CW speed) |
| **QRT** | Shall I stop sending? | Stop sending / I am shutting down station |
| **QRU** | Have you anything for me? | I have nothing for you |
| **QRV** | Are you ready? | I am ready |
| **QRX** | When will you call again? | I will call again at [time], stand by |
| **QRZ** | Who is calling me? | You are being called by [callsign] |
| **QSB** | Is my signal fading? | Your signal is fading |
| **QSL** | Can you acknowledge? | I acknowledge receipt (QSL card = confirmation) |
| **QSO** | Can you communicate with [station]? | I can communicate (QSO = contact, conversation) |
| **QSY** | Shall I change frequency? | Change frequency to [frequency] |
| **QTH** | What is your location? | My location is [city, grid square] |

**Usage Examples**:

**Before Transmitting**:
- "QRL?" (Is this frequency in use?)
- Response: "QRL, frequency is in use" or "Frequency is clear"

**During QSO**:
- "Your signal is QSB" (Your signal is fading)
- "QRX 5 minutes" (Stand by, I'll be back in 5 minutes)
- "QRT for dinner" (I'm shutting down station to eat)

**Interference**:
- "Heavy QRM from local station" (Interference from another radio station)
- "QRN makes copy difficult" (Atmospheric static/noise)

**Ending Contact**:
- "QSL?" (Do you confirm receipt?)
- "QSL, 73" (Confirmed, best regards/goodbye)

### Prowords (Procedural Words)

**Prowords** are voice procedure words used to structure radio transmissions. Military and aviation origin.

**Common Prowords**:
| Proword | Meaning |
|---------|---------|
| **Over** | My transmission is ended, I expect a response (like "your turn" in conversation) |
| **Out** | My transmission is ended, I do not expect a response (end of conversation) |
| **Roger** | I have received all of your last transmission (NOT "yes" or "I agree") |
| **Wilco** | I have received your message, understand it, and will comply (WILl COmply) |
| **Say Again** | Repeat your last transmission (not "repeat" — "repeat" means "fire again" in military) |
| **Break** | I am separating portions of my message (indicates pause, next part coming) |
| **Break Break Break** | I have urgent traffic, all other stations cease transmissions |
| **Correction** | An error has been made in this transmission, the correct version is... |
| **Read Back** | Repeat the message back to me exactly as received (for verification) |
| **Wait** | I must pause, stand by for a few seconds |
| **Wait Out** | I must pause for longer than a few seconds, I will call you when ready |
| **This is** | This transmission is from the station whose callsign immediately follows |
| **From** | Message originator (in formal message handling) |
| **To** | Message addressee (in formal message handling) |
| **Time** | The time immediately following is UTC (Coordinated Universal Time) |
| **Figures** | Numbers follow (alerts listener to write down numbers) |
| **Spell** | Phonetic spelling follows |

**Usage Examples**:

**Basic Exchange**:
```
Station A: "Station Bravo, this is Station Alpha, over"
Station B: "Station Alpha, this is Station Bravo, go ahead, over"
Station A: "Request your 10-20, over"
Station B: "My location is shelter Delta, over"
Station A: "Roger, out"
```

**Urgent Traffic**:
```
Station C: "Break break break, emergency traffic, all stations stand by"
Net Control: "All stations stand by, Station Charlie go ahead with emergency traffic"
Station C: "Medical emergency at shelter Alpha, request immediate evacuation, over"
Net Control: "Roger, dispatching evacuation team, over"
Station C: "Wilco, standing by, over"
```

**Message with Numbers**:
```
"Figures: We need 2-5 (two-five) gallons of water, 1-0-0 (one-zero-zero) meals ready-to-eat, over"
```

**Spelling**:
```
"Location is, spell: Hotel, Oscar, Sierra, Papa, India, Tango, Alpha, Lima, over"
(HOSPITAL)
```

### Common Mistakes

- ❌ **Using "repeat" instead of "say again"**: "Repeat" means "fire again" in military (artillery command)
- ✓ **Use "say again"**: Unambiguous request for retransmission
- ❌ **Saying "over and out"**: Contradictory (over = expecting reply, out = not expecting reply)
- ✓ **Say "over" OR "out"**: Not both
- ❌ **Roger = yes/agreement**: "Roger" means "received", not "I agree" or "I will comply"
- ✓ **Use "Roger" for receipt, "Wilco" for compliance**

## Distress Signals

**Distress signals** indicate emergency urgency level. Three levels:

### MAYDAY (Distress)

**Use**: **Life-threatening emergency** (immediate danger to life or property)

**Examples**:
- Sinking boat, flooding compartment
- Aircraft engine failure, forced landing imminent
- Fire with persons trapped
- Medical emergency (heart attack, severe trauma)
- Imminent threat (armed attack, kidnapping in progress)

**Procedure** (voice):
1. **Select emergency frequency**:
   - Marine: Channel 16 (156.8 MHz)
   - Aviation: 121.5 MHz (civilian), 243.0 MHz (military)
   - Ham radio: Calling frequency (146.520 MHz VHF, 7.285 MHz HF)
2. **Transmit**:
   ```
   "MAYDAY, MAYDAY, MAYDAY"
   "This is [callsign/vessel name], [callsign/vessel name], [callsign/vessel name]"
   "MAYDAY [callsign]"
   "Position: [GPS coordinates or description]"
   "Nature of distress: [sinking, fire, medical emergency]"
   "Number of persons: [count]"
   "Description: [vessel/vehicle/location details]"
   "Over"
   ```
3. **Wait for response** (15-30 seconds)
4. **Repeat if no response**
5. **Once response received**: Provide additional details, follow instructions

**Example**:
```
"MAYDAY, MAYDAY, MAYDAY"
"This is sailing vessel Sea Bird, Sea Bird, Sea Bird"
"MAYDAY Sea Bird"
"Position: 37 degrees 45 minutes North, 122 degrees 30 minutes West"
"Nature of distress: Taking on water, engine room flooding"
"Six persons on board"
"35-foot white sailboat, blue canvas dodger"
"Over"
```

**Digital Distress** (DSC):
- Press red **DISTRESS** button on VHF/HF radio (hold 3-5 seconds)
- Radio automatically transmits distress alert with MMSI, GPS position, nature of distress
- Coast Guard and nearby vessels alerted immediately

**EPIRB** (Emergency Position Indicating Radio Beacon):
- Satellite distress beacon (406 MHz, monitored by COSPAS-SARSAT satellites)
- Activated manually or automatically (water-activated)
- Transmits GPS position, vessel registration
- Search and rescue dispatched (may take 1-6 hours depending on location)

### PAN-PAN (Urgency)

**Use**: **Urgent situation, not immediately life-threatening** (requires assistance but not immediate danger)

**Examples**:
- Engine failure but no immediate danger (sailing, drifting)
- Medical situation requiring doctor advice (non-critical illness/injury)
- Navigation equipment failure (GPS, compass lost)
- Request priority routing (storm avoidance)
- Disabled vehicle requiring tow

**Procedure** (voice):
1. **Select emergency frequency** (same as MAYDAY)
2. **Transmit**:
   ```
   "PAN-PAN, PAN-PAN, PAN-PAN"
   "All stations, this is [callsign/vessel name]"
   "Position: [location]"
   "Nature of urgency: [describe situation]"
   "Request: [assistance needed]"
   "Over"
   ```

**Example**:
```
"PAN-PAN, PAN-PAN, PAN-PAN"
"All stations, this is motor vessel Pacific Wind"
"Position: 10 miles west of Golden Gate Bridge"
"Nature of urgency: Engine failure, drifting toward rocks"
"Request: Immediate tow assistance"
"Three persons on board, no injuries"
"Over"
```

### SÉCURITÉ (Safety)

**Use**: **Safety information** (important navigational or meteorological information, no immediate danger)

**Pronunciation**: "SAY-CURE-EE-TAY"

**Examples**:
- Navigation hazard (debris, logs, shipping container in water)
- Severe weather warning
- Disabled vessel (not in distress, just informing other traffic)
- Notice to mariners (channel closure, dredging operations)

**Procedure** (voice):
1. **Select working frequency** (may use emergency frequency if critical)
2. **Transmit**:
   ```
   "SÉCURITÉ, SÉCURITÉ, SÉCURITÉ"
   "All stations, this is [callsign/vessel name]"
   "Following is a safety message:"
   [Describe hazard, location, recommended action]
   "Out"
   ```

**Example**:
```
"SÉCURITÉ, SÉCURITÉ, SÉCURITÉ"
"All stations, this is Coast Guard Station San Francisco"
"Following is a safety message:"
"Large shipping container adrift, position 37 degrees 48 minutes North, 122 degrees 24 minutes West"
"All vessels exercise caution, maintain sharp lookout"
"Out"
```

### Distress Signal Hierarchy & Response

**Priority Order**:
1. **MAYDAY** (distress): All stations immediately cease non-emergency traffic, listen for distress details
2. **PAN-PAN** (urgency): Priority over routine traffic, stations with non-urgent traffic wait
3. **SÉCURITÉ** (safety): Information only, routine traffic may continue after announcement

**If You Hear Distress Signal**:
1. **Stop transmitting immediately** (do not interfere with distress traffic)
2. **Listen** for distress details (position, nature, assistance requested)
3. **Record information** (write down position, description, time)
4. **If you can assist**: Wait for distress station to finish transmission, then respond: "Station in distress, this is [your callsign], I can assist, over"
5. **If you cannot assist**: Remain silent, monitor frequency in case relay needed
6. **Relay if necessary**: If distress station weak/unreadable and you hear clearly, relay to Coast Guard/authorities

**False Distress Penalties**:
- FCC: $10,000-25,000 fine per violation
- Coast Guard: $5,000-100,000 fine, possible criminal prosecution
- Revocation of radio license
- Reimbursement of search and rescue costs ($10,000-500,000+)

## Radio Discipline

**Radio discipline** ensures efficient use of limited frequencies and prevents confusion during emergency operations.

### Before Transmitting

**Listen First** ("LISTEN, THEN TRANSMIT"):
1. Monitor frequency for 10-30 seconds before transmitting
2. Ensure frequency is clear (no one else transmitting)
3. If frequency in use, wait for conversation to end
4. On ham radio, ask: "Is this frequency in use?" or "QRL?"

**Why**: Prevents "doubling" (two stations transmitting simultaneously, neither heard clearly).

### During Transmission

**Speak Clearly**:
- **Pace**: Slow, deliberate (conversational speed × 0.7)
- **Enunciation**: Pronounce each word distinctly (avoid mumbling, rushing)
- **Tone**: Normal speaking voice (don't shout, don't whisper)
- **Microphone Distance**: 1-2 inches from lips (not touching, not 6 inches away)

**Be Brief**:
- **Get to the point**: State purpose in first sentence
- **Avoid unnecessary words**: "Um", "uh", "like", "you know" waste time
- **Use brevity codes**: "10-20" instead of "Can you please tell me your current location?"
- **One topic per transmission**: Don't ramble, make your point, say "over"

**Structure**:
1. **Who you're calling**: "Station Bravo, this is Station Alpha"
2. **Your message**: Brief, clear statement or question
3. **End proword**: "Over" (expecting reply) or "Out" (not expecting reply)

**Avoid**:
- **Long-winded stories**: Save for later, keep frequency clear
- **Personal chit-chat**: Emergency net is not social hour
- **Arguments**: If disagreement, take it off-frequency (switch to another channel or discuss later)

### After Transmission

**Listen for Response**:
- Wait 5-10 seconds for reply
- If no reply, repeat (once or twice)
- If still no reply, called station may not hear you (try different frequency, increase power, or move to better location)

**Acknowledge Receipt**:
- Use "Roger" (received and understood) or "Wilco" (will comply)
- Don't leave other station wondering if you heard them

### Example of Good Radio Discipline

**Station Alpha** (following all protocols):
```
[Listens for 15 seconds, frequency is clear]
"Net Control, this is Station Alpha, over"
[Waits 5 seconds]

Net Control: "Station Alpha, Net Control, go ahead, over"

Station Alpha: "Request supply status at shelter Delta, over"
[Brief, clear, single question]

Net Control: "Stand by, checking... Shelter Delta reports 50 gallons water, 100 meals remaining, over"

Station Alpha: "Roger, 50 gallons water, 100 meals, thank you, out"
[Confirms receipt, ends transmission]
```

**Time Elapsed**: 30 seconds (efficient, clear, complete exchange).

### Example of Poor Radio Discipline

**Station Charlie** (violating multiple protocols):
```
[No listening, transmits immediately]
"Hey, uh, this is Charlie, um, I was wondering, uh, like, if anybody knows, um, what's going on with the, uh, shelter situation? I mean, like, I heard there was, you know, some problems with, uh, water or something, I don't know, and, uh, I'm just curious, you know, what's happening, so, uh, yeah, if somebody could, like, let me know, that would be, uh, great, I guess, over"
[50+ seconds of rambling, unclear question, filled with filler words]

Net Control: "Station Charlie, please be brief, what is your specific question? Over"

Station Charlie: "Oh, uh, sorry, yeah, I mean, like, I just want to know about the water situation, I guess, over"

Net Control: "Roger, which shelter? Over"

Station Charlie: "Uh, I don't know, just, like, in general, I guess, over"
[Wasted 2+ minutes, unclear communication]
```

**Time Elapsed**: 2-3 minutes (inefficient, unclear, ties up frequency).

## Net Control Operations

**Net** (short for "network"): Organized group of stations operating on common frequency under direction of **Net Control Station** (NCS).

**Purpose**: Coordinate multiple stations, manage message traffic, maintain order on frequency.

### Net Types

**Emergency Net**: Activated during disaster, handles emergency traffic (resource requests, status reports, evacuation coordination)

**Training Net**: Weekly practice net, maintains operator proficiency, tests equipment

**Traffic Net**: Handles formal written messages (radiograms, ICS-213 forms)

### Net Control Station (NCS) Responsibilities

**NCS** coordinates net operations:
1. **Open net**: Announce net purpose, frequency, operating procedures
2. **Take check-ins**: Maintain roster of stations
3. **Handle traffic**: Relay messages between stations, prioritize by urgency
4. **Maintain order**: Enforce radio discipline, prevent interference
5. **Close net**: Announce end of operations, thank participants

### Net Check-In Procedure

**NCS Opens Net**:
```
"This is W1ABC, Net Control, opening the Emergency Communications Net on 146.520 MHz. All stations with emergency or priority traffic, check in now. Over"
[Waits 5-10 seconds]

"Any stations with routine traffic or status updates, check in now. Over"
[Waits 5-10 seconds]

"All other stations wishing to check in, call in alphabetical order by suffix. Stations with callsign suffix beginning with A through M, check in now. Over"
```

**Station Check-In**:
```
Station K7XYZ: "K7XYZ, portable at shelter Bravo, over"
[Brief: Callsign, location/status]

NCS: "Roger, K7XYZ, you are number 5 on the roster. Stand by. Over"
```

**After Check-Ins Complete**:
```
NCS: "All check-ins complete. 12 stations checked in. Net is now open for traffic. Any station with traffic for another station, call Net Control. Over"
```

### Message Handling

**Formal Message Format** (ICS-213, radiogram):

**Preamble**:
- Message number (sequential, unique per day)
- Precedence (EMERGENCY, PRIORITY, ROUTINE)
- Date and time (UTC or local with time zone)
- Originator (callsign, name, organization)

**Text**: Message body (clear, concise, complete)

**Signature**: Sender name, position, contact info

**Example Message Transmission**:
```
Station A to NCS: "Net Control, Station Alpha, I have priority traffic for Station Bravo, over"

NCS: "Station Alpha, send your traffic, over"

Station A: "Message number 15, priority, time 1430 UTC, from shelter Alpha to shelter Bravo. Text as follows: 'Request immediate evacuation of 2-0 (two-zero) persons, medical emergencies, heat exhaustion. Stand by for pickup at coordinates to follow.' Figures: 3-7 (three-seven) point 7-5 (seven-five) North, 1-2-2 (one-two-two) point 3-0 (three-zero) West. Signature: John Doe, Shelter Coordinator, callsign W1ABC. End of message. Over"

NCS: "Roger, message number 15, priority traffic, to Station Bravo. Station Bravo, do you copy? Over"

Station Bravo: "Station Bravo copies, ready to copy, over"

NCS: "Station Alpha, send message to Station Bravo, over"

Station A: [Repeats message to Station Bravo]

Station Bravo: "Roger, message received, 2-0 persons evacuation, medical emergency, coordinates received. Dispatching vehicle now. Over"

NCS: "Message acknowledged and action taken. Any further traffic? Over"

Station A: "Negative, out"
Station Bravo: "Negative, out"

NCS: "Roger, net is clear, standing by for further traffic. Over"
```

### Message Precedence

**Four Levels** (ICS/FEMA standard):

| Precedence | Use | Example |
|------------|-----|---------|
| **EMERGENCY** | Life-threatening, immediate action required | "EMERGENCY: Fire spreading, immediate evacuation shelter Alpha" |
| **PRIORITY** | Urgent, time-sensitive, not immediately life-threatening | "PRIORITY: Medical supplies low, request resupply within 4 hours" |
| **WELFARE** | Personal status, family notifications, non-operational | "WELFARE: Please notify family of John Doe (address), he is safe" |
| **ROUTINE** | Administrative, informational, no time constraint | "ROUTINE: Daily status report, all facilities operating normally" |

**Handling Order**: EMERGENCY → PRIORITY → WELFARE → ROUTINE

**Preemption**: EMERGENCY traffic interrupts all other traffic. PRIORITY interrupts WELFARE and ROUTINE.

### Net Discipline Enforcement

**NCS Actions for Violations**:

**Unauthorized Transmission**:
```
NCS: "Station transmitting out of turn, please wait for Net Control to call you. Over"
```

**Long-Winded Transmission**:
```
NCS: "All stations, please keep transmissions brief. Station Charlie, state your traffic in 1-2 sentences. Over"
```

**Off-Topic Discussion**:
```
NCS: "All stations, this net is for emergency traffic only. Non-emergency discussions, please move to [alternate frequency]. Over"
```

**Interference**:
```
NCS: "Station causing interference, you are not authorized on this frequency. Cease transmissions immediately. All other stations, ignore interfering station, continue operations. Over"
```

## ARES & RACES Integration

**ARES** (Amateur Radio Emergency Service): ARRL-sponsored volunteer program providing emergency communications.

**RACES** (Radio Amateur Civil Emergency Service): FCC-recognized program providing government emergency communications.

### ARES Structure

**Organization**:
- **Section Emergency Coordinator (SEC)**: State/section level (e.g., California SEC)
- **District Emergency Coordinator (DEC)**: Multi-county district
- **Emergency Coordinator (EC)**: County level
- **Assistant Emergency Coordinators (AEC)**: Specialized roles (VHF, HF, digital, logistics)
- **ARES Members**: Registered volunteers

**Served Agencies**: Red Cross, hospitals, emergency management, public health, shelters

**Activation**: By Emergency Coordinator or served agency (during disaster, exercise, public event)

### RACES Structure

**Organization**:
- **Radio Officer**: Government-appointed official (county/state emergency management)
- **RACES Members**: Licensed hams enrolled in RACES (application process)

**Activation**: Only by government authority (mayor, county executive, governor)

**Purpose**: Government-to-government communications during emergencies (NOT public service, NOT served agencies like Red Cross)

**Difference from ARES**:
- **ARES**: Volunteer-initiated, serves non-government agencies (Red Cross, hospitals)
- **RACES**: Government-initiated, serves government only (EOC, fire, police, public works)

**Dual Enrollment**: Most hams join both ARES and RACES (separate activations, but often same people)

### ICS Integration

**ICS** (Incident Command System): Standardized emergency management structure (FEMA/NIMS standard).

**Communications Unit (COMU)**:
- Part of ICS Planning Section (Logistics Section in small incidents)
- **COML** (Communications Unit Leader): Manages all incident communications (radio, phone, internet)
- **COMT** (Communications Technician): Installs, maintains, repairs equipment
- **RADO** (Radio Operator): Operates radio equipment, handles message traffic
- **ITAO** (Auxiliary Communications**: Amateur radio operators (ARES/RACES) integrate here

**Ham Radio Roles in ICS**:
- **Tactical Communications**: Direct support to incident operations (fire, rescue, medical)
- **Resource Communications**: Coordination between incident command and supply sources
- **Emergency Public Information**: Disseminate public info (shelter locations, evacuations)
- **Administrative**: Health/welfare messages, logistics coordination

**ICS Forms** (Common for ARES/RACES):
- **ICS-213**: General message form (most common, used for all routine message traffic)
- **ICS-214**: Activity log (operator time on/off duty, messages handled, notes)
- **ICS-309**: Communications log (all transmissions, times, frequencies, stations contacted)

**Training Requirements**:
- **ICS-100**: Introduction to ICS (2 hours, free online at training.fema.gov)
- **ICS-200**: ICS for Single Resources (3 hours)
- **ICS-700**: National Incident Management System (NIMS) Introduction (3 hours)
- **ICS-800**: National Response Framework (NRF) Introduction (3 hours)

**Recommendation**: All ARES/RACES members complete ICS-100, ICS-200, ICS-700, ICS-800 (10-12 hours total, certificates issued).

### AUXCOMM (Auxiliary Communications)

**AUXCOMM**: Federal program integrating volunteer communicators (ham radio, GMRS, CB, aviation, marine) into emergency response.

**Tiers**:
- **Tier 1**: Local level (county ARES/RACES)
- **Tier 2**: Regional level (multi-county, state)
- **Tier 3**: National level (deployable teams, multi-state disasters)

**Deployment**: AUXCOMM teams deploy to major disasters (hurricanes, earthquakes) to augment local communications.

**Equipment**: Standardized comm kits (HF, VHF, satellite, portable towers, generators).

**Qualification**: ICS training + technical proficiency + background check (FEMA credentials).

## Emergency Communications Best Practices

### Pre-Event Preparation

**Equipment Check** (Weekly):
1. Power on radio, verify function (transmit, receive)
2. Check battery charge (handheld), fuel level (generator)
3. Test antenna SWR (HF), check coax connections
4. Program emergency frequencies, verify repeater access
5. Update firmware/software (digital modes)

**Skills Practice** (Weekly):
1. Participate in practice net (ARES, club net, informal)
2. Send/receive formal messages (ICS-213 practice)
3. Practice phonetic alphabet (spell random words)
4. Test digital modes (Winlink check-in, FT8 contacts)

**Documentation** (Quarterly):
1. Update contact list (Net Control, EC, served agencies)
2. Review frequency plan (primary + backups)
3. Update equipment inventory (what you have, where it is)
4. Refresh ICS training (review ICS-213 format, NIMS guidelines)

### During Event

**Activation Procedure**:
1. Monitor emergency net frequency (announced in advance, or 146.520 MHz VHF, 7.285 MHz HF)
2. Check in when NCS calls for check-ins
3. Provide brief status (location, resources, equipment)
4. Follow NCS instructions, stand by for assignments

**Operational Discipline**:
1. Listen more than transmit (80% listening, 20% transmitting)
2. Keep transmissions <30 seconds (exception: formal messages)
3. Use brevity codes, phonetic alphabet
4. Write down all messages (don't rely on memory)
5. Log all activity (ICS-309 log: time, frequency, station contacted, message summary)

**Shift Length**:
- **4-6 hours**: Optimal for maintaining alertness
- **12 hours**: Maximum before mandatory rest (8 hours off)
- **24+ hours**: Emergency only, rotate operators every 2-4 hours within shift

**Fatigue Management**:
- Hydration (water every hour)
- Snacks (avoid heavy meals, prefer light carbs/protein)
- Breaks (5-10 minutes every 2 hours, walk around, stretch)
- Alertness checks (buddy system, co-operator verifies messages)

### Post-Event

**Debrief**:
1. Participate in after-action review (AAR)
2. Document lessons learned (what worked, what didn't)
3. Submit ICS-214 activity log, ICS-309 communications log

**Equipment Maintenance**:
1. Recharge batteries (discharge to 40-60%, recharge fully)
2. Refuel generator (run dry, add stabilizer, store)
3. Inspect antennas (damage from weather, animals)
4. Update equipment list (note failures, recommend replacements)

**Training Updates**:
1. Review protocols that caused confusion (brief NCS/EC)
2. Update SOPs (Standard Operating Procedures) if protocols changed
3. Schedule training on identified gaps (antenna construction, digital modes, ICS forms)

## Common Emergency Communications Mistakes

- ❌ **Not listening before transmitting**: Doubling over other stations, missed traffic
- ✓ **Listen 10-30 seconds, ensure frequency clear**
- ❌ **Using plain language callsigns**: "This is John calling Mary" (no accountability, hard to log)
- ✓ **Always use callsigns**: "W1ABC calling K2XYZ" (FCC requires identification)
- ❌ **Transmitting sensitive information unencrypted**: Locations of valuables, security plans, medical details
- ✓ **Use coded messages or secure comms** (Winlink, phone, in-person)
- ❌ **Rag-chewing (casual conversation) on emergency net**: Ties up frequency
- ✓ **Keep transmissions brief and on-topic** during emergency operations
- ❌ **Not logging activity**: Relying on memory, no documentation for AAR
- ✓ **Log every message** (ICS-309): Time, frequency, stations, summary
- ❌ **Operating beyond fatigue point**: 16+ hours straight, making errors
- ✓ **Rotate operators, enforce rest periods** (maximum 12-hour shifts with breaks)

## Conclusion

**Emergency communications protocols** ensure clarity, efficiency, and interoperability during crises:

1. **Phonetic Alphabet**: Eliminates spelling errors, internationally recognized
2. **Brevity Codes**: Saves time, reduces channel congestion (Q-codes, 10-codes, prowords)
3. **Distress Signals**: Immediately conveys urgency (MAYDAY, PAN-PAN, SÉCURITÉ)
4. **Radio Discipline**: Maintains order on frequency (listen first, be brief, acknowledge)
5. **Net Control Operations**: Coordinates multiple stations, manages message traffic
6. **ARES/RACES Integration**: Interfaces volunteer communicators with professional emergency management (ICS structure)

**Action Items**:
1. **Memorize phonetic alphabet** (daily practice, 1-2 weeks)
2. **Learn essential brevity codes** (10-4, QSL, QTH, Over/Out)
3. **Complete ICS training** (ICS-100, ICS-200, ICS-700 — free at training.fema.gov)
4. **Participate in weekly practice net** (ARES, club net, informal group)
5. **Join ARES** (contact county EC via arrl.org/ares)
6. **Practice formal message handling** (ICS-213 forms, radiogram format)

Emergency communications is **skill-based, perishable competency**. Weekly practice maintains proficiency. Train before crisis, operate effectively during crisis.
