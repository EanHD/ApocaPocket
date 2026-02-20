---
id: l3-tech-digital-radio
title: "Digital Radio Modes: Data Communications Without Internet"
layer: L3_materials_technology
category: communications
tags:
  - digital_radio
  - APRS
  - Winlink
  - FT8
  - JS8Call
  - DMR
  - SSTV
  - data_communications
region_relevance:
  - global
summary: "Digital radio modes enable text messaging, email, GPS tracking, file transfer, and image transmission without internet. Covers APRS (position reporting, messaging), Winlink (email over HF/VHF), FT8/JS8Call (weak-signal keyboard chat), DMR/Fusion (digital voice), and SSTV (image transmission). Includes equipment requirements, software setup, operating procedures, and protocol specifications."
steps:
  - "Install digital mode interface between radio and computer: sound card interface ($30-80) or USB-based digital interface (SignaLink, RigBlaster, $100-150)"
  - "Download and configure mode-specific software (APRS: APRSdroid/Xastir, Winlink: Winlink Express, FT8: WSJT-X, JS8Call: JS8Call client)"
  - "Set audio levels to prevent overdriving (ALC should not activate, typical 30-50% audio output from computer)"
  - "Establish time synchronization (GPS or internet NTP) for time-critical modes (FT8, FT4) — accuracy within ±1 second required"
  - "Operate within mode-specific protocols (transmit timing, frequency allocations, message formatting)"
warnings:
  - "OVERDRIVING: Digital modes (especially FT8, PSK31, RTTY) generate constant-carrier signals at full power. Excessive audio levels cause splatter (interference on adjacent frequencies) and transmitter overheating. Monitor ALC meter — zero or minimal ALC activation during digital transmission"
  - "DUTY CYCLE: Digital modes have 50-100% duty cycle (continuous transmission) vs 20-40% for SSB voice. Transmitters rated for 100W SSB may overheat at 50-75W continuous digital. Reduce power 30-50% for digital modes or add cooling"
  - "TIME SYNC: FT8/FT4 require accurate system time (±1 second). Incorrect time prevents decoding. Use GPS time source, NTP internet sync (before emergency), or WWV time signal for synchronization"
  - "FREQUENCY ACCURACY: Digital modes require precise frequency control (±10 Hz for FT8, ±50 Hz for PSK31). Some older radios drift significantly — poor frequency stability prevents successful contacts"
  - "LEGAL: Winlink email content must be non-commercial, personal communications only (no business, no third-party traffic for non-licensed persons in some countries). Encryption prohibited in most countries for amateur radio"
  - "BANDWIDTH: Some digital modes (PACTOR, VARA) use wide bandwidth (2-3 kHz). Verify mode is legal on selected band/frequency. Narrow modes (PSK31, FT8) use 50-500 Hz bandwidth"
related_entries:
  - l3-tech-radio-basics
  - l3-tech-antenna-construction
  - l3-tech-propagation
  - l3-tech-emergency-comms
sources:
  - ARRL Handbook for Radio Communications
  - ARRL's HF Digital Handbook
  - Winlink Development Team documentation
  - WSJT-X User Guide (Princeton University)
  - DMR Association protocols
  - APRS Protocol Specification (APRS101.pdf)
audit_status: verified
last_verified: 2026-02-19
confidence: high
offline_assets: []
---

## Overview

**Digital radio modes** transmit data (text, position, files, images) over radio frequencies without internet infrastructure. Unlike analog voice communications, digital modes use error correction, automatic retries, and data compression to achieve reliable communications under poor conditions.

**Advantages of Digital Modes**:
- **Weak Signal Performance**: FT8 decodes signals 10-15 dB below noise floor (inaudible to human ear)
- **Error Correction**: Forward Error Correction (FEC) and Automatic Repeat reQuest (ARQ) ensure accurate message delivery
- **Precision**: GPS position accurate to 10 meters vs "approximately 5 miles north of town"
- **Store-and-Forward**: Winlink stores messages on servers, delivers when recipient connects (email-like)
- **Documentation**: Written log of all communications (vs relying on memory of voice QSO)
- **Automation**: Unattended operation (APRS beacons, Winlink polling) without operator presence

**Disadvantages**:
- **Equipment Complexity**: Requires computer, interface, software (vs simple microphone for voice)
- **Learning Curve**: Software configuration, protocol understanding, troubleshooting
- **Power Consumption**: Computer + radio (50-150W total) vs radio only (10-100W)
- **Time Sync Requirements**: Some modes (FT8) require accurate system time

This guide covers **six primary digital modes** for emergency communications:

1. **APRS** — GPS tracking, position reporting, short messaging (VHF)
2. **Winlink** — Email over radio (HF and VHF)
3. **FT8/FT4** — Extremely weak signal contacts, propagation monitoring (HF/VHF)
4. **JS8Call** — Keyboard-to-keyboard chat, messaging (HF)
5. **DMR/Fusion** — Digital voice with GPS and text messaging (VHF/UHF)
6. **SSTV** — Image transmission (photos, maps, documents)

## Hardware Requirements

### Radio-to-Computer Interface

**Option 1: Sound Card Interface** ($0-50, DIY to commercial)
Connects radio audio output to computer sound card input (mic/line-in), and computer audio output to radio mic input.

**Components**:
- **Audio cables**: 3.5mm stereo cables, adapters
- **Isolation transformer**: Prevents ground loops (hum, noise). Cheap solution: 1:1 audio transformer from Mouser/Digi-Key ($3-8)
- **PTT (Push-to-Talk) Control**: Key radio from computer
  - Serial port RTS/DTR line (older computers)
  - USB-to-serial adapter + VOX (voice-activated transmit)
  - GPIO from Raspberry Pi

**Advantages**: Low cost, works with most radios
**Disadvantages**: Ground loop noise, manual level adjustment, PTT control complexity

**Option 2: Commercial Sound Card Interface** ($80-150)
Pre-built interface with isolation, level controls, and PTT.

**Products**:
- **SignaLink USB**: $120-140, most popular, includes sound card + isolators + PTT
- **RigBlaster**: $100-200 (multiple models)
- **TigerTronics interfaces**: $100-180

**Advantages**: Clean audio, no ground loops, easy setup, PTT control included
**Disadvantages**: Cost

**Option 3: USB Digital Interface (Integrated)** ($150-400)
Radio with built-in USB sound card and data interface (no external box required).

**Radios with USB Audio**:
- Yaesu FT-891, FT-991A (HF)
- ICOM IC-7300, IC-7610 (HF with spectrum display)
- Yaesu FTM-400XDR, FTM-300DR (VHF/UHF mobile)

**Advantages**: Cleanest audio, no external interface needed, radio-specific software integration
**Disadvantages**: Higher cost (radio + interface), locked to specific radio brand

### Computer Requirements

**Minimum Specifications**:
- **CPU**: 1 GHz (APRS, Winlink, JS8Call), 2 GHz+ (FT8, SSTV decoding)
- **RAM**: 2 GB (4 GB recommended)
- **OS**: Windows 7+, macOS 10.12+, Linux (Ubuntu, Debian, Raspbian)
- **Sound Card**: Any (built-in adequate)
- **USB Ports**: 1-2 (interface, optional GPS)
- **Storage**: 10-50 GB (operating system, software, message archives)

**Recommended**: Laptop (portable operations), ruggedized if possible (Panasonic Toughbook, Dell Latitude Rugged). Netbook or tablet adequate for APRS/Winlink.

**Raspberry Pi**: Excellent for APRS iGate, Winlink RMS, lightweight digital modes. Pi 4 (4 GB RAM) handles FT8, JS8Call well. Cost: $50-100 complete.

### GPS Receiver (APRS, DMR)

**USB GPS** ($20-50):
- **VK-162** (GlobalSat BU-353S4 chipset): $25, USB, 1-5 meter accuracy
- **U-blox modules**: $30-50, high sensitivity, WAAS/EGNOS support

**Serial GPS** ($30-80):
- **Garmin GPS18x**: $80, marine-grade, rugged, NMEA output

**Built-in Radio GPS**:
- Many VHF/UHF radios (Yaesu FTM-400XDR, Kenwood TM-D710GA) include built-in GPS

**Requirements**: 
- NMEA 0183 output format
- USB or serial connection to computer
- Update rate: 1-5 seconds (faster for mobile APRS)

### Cables & Adapters

- **Audio Cables**: 3.5mm stereo to mono adapter (radio input typically mono)
- **Serial/USB Cable**: Radio control (CAT control for frequency/mode changes)
- **RF Coax**: Radio to antenna (standard coax, see l3-tech-antenna-construction.md)
- **Power**: 12V power supply for radio (20-30A for 100W HF, 5-8A for VHF/UHF mobile)

## Mode 1: APRS (Automatic Packet Reporting System)

**APRS** broadcasts position, status, weather, and short messages over VHF radio (144.390 MHz in North America). Stations receive and relay packets, creating mesh network.

### APRS Fundamentals

**Frequency**: 
- **North America**: 144.390 MHz (1200 baud AFSK)
- **Europe**: 144.800 MHz
- **Australia**: 145.175 MHz

**Packet Format**: AX.25 protocol (amateur radio X.25 derivative). Each packet contains:
- **Callsign**: Station identifier (e.g., W1ABC-9, -9 is SSID for mobile)
- **Position**: Latitude/longitude (degrees/minutes decimal)
- **Altitude**: Meters above sea level (optional)
- **Speed & Course**: MPH and degrees (mobile stations)
- **Status Text**: Up to 67 characters (e.g., "En route to shelter")
- **Symbol**: Icon on map (car, house, emergency, balloon, etc.)

**Network Architecture**:
- **Digipeaters**: Relay APRS packets (extend range from 5 miles direct to 50+ miles multi-hop)
- **iGates**: Internet-connected stations upload APRS packets to APRS-IS (APRS Internet Service, global aggregation server at aprs.fi, aprs2.net)
- **Mobile Stations**: Transmit position every 1-5 minutes while moving
- **Fixed Stations**: Transmit position/status every 10-30 minutes

### Equipment for APRS

**Option 1: Dedicated APRS Hardware**
- **Kenwood TM-D710GA**: VHF/UHF mobile with built-in APRS + GPS ($450)
- **Yaesu FTM-400XDR**: Dual-band mobile with APRS + GPS ($380)
- **Mobilinkd TNC3**: Bluetooth TNC connects to smartphone, $75 (requires VHF radio)

**Option 2: Software APRS (Computer + Radio)**
- VHF FM radio (any model, 144.390 MHz)
- Sound card interface (SignaLink $120 or DIY $20)
- GPS receiver (USB, $25)
- APRS software (see below)

**Option 3: Smartphone APRS**
- Android phone with APRSdroid app (free)
- Mobilinkd TNC3 ($75, Bluetooth TNC)
- Baofeng UV-5R radio ($25)
- **Total**: $100-150 mobile APRS station

### APRS Software

| Software | Platform | Cost | Features |
|----------|----------|------|----------|
| **APRSdroid** | Android | Free | Mobile APRS, GPS tracking, messaging |
| **APRS.fi** | Web | Free | View APRS traffic worldwide (requires internet) |
| **Xastir** | Linux | Free | Full-featured APRS client, mapping, weather |
| **UI-View32** | Windows | Free | Legacy but functional APRS client |
| **APRSIS32** | Windows | Free | Modern APRS client, messaging, mapping |
| **PinPoint APRS** | macOS | $30 | Native Mac APRS client |
| **Dire Wolf** | Linux/Windows/Mac | Free | Software TNC (audio modem) for APRS |

**Recommended Setup (Portable)**:
- **Raspberry Pi 4** + **Dire Wolf** + **Xastir**: Complete APRS station, $100-150
- Runs headless (no display), access via web browser

### APRS Configuration

**Step 1: Install Software**
- Example: APRSdroid on Android phone

**Step 2: Configure Callsign**
- Enter your callsign with SSID (e.g., W1ABC-9 for mobile)
- SSID conventions:
  - **-0**: Primary station (home)
  - **-7**: Handheld/walkie-talkie
  - **-9**: Mobile (vehicle)
  - **-10**: Internet gateway (iGate)
  - **-11**: Balloon/aircraft
  - **-15**: Generic or test

**Step 3: Set Position Source**
- GPS receiver (phone built-in or external USB GPS)
- Enable GPS, wait for fix (30-120 seconds outdoors)

**Step 4: Configure Beacon Rate**
- **Mobile**: 1-2 minutes (while moving rapidly), 5 minutes (slow)
- **Portable**: 10-30 minutes (conserve battery)
- **Fixed**: 30-60 minutes
- **SmartBeaconing**: Automatically adjusts rate based on speed and direction changes (recommended)

**Step 5: Set Symbol**
- Choose icon representing station (car, house, emergency vehicle, etc.)
- APRS has 180+ symbols

**Step 6: Connect to Radio**
- Hardware TNC: Connect TNC audio to radio mic input, radio speaker to TNC audio input
- Software TNC (Dire Wolf): Computer sound card to radio interface
- VOX or PTT: Configure transmit control

**Step 7: Test Transmission**
- Beacon once, check aprs.fi after 2-5 minutes (if iGate in range)
- Listen on 144.390 MHz — should hear digital bursts (packet sounds like short modem tones)

### APRS Messaging

APRS supports **short text messages** between stations.

**Message Format**:
```
:W1ABC   :Message text here{msg_id}
```
(Maximum 67 characters, padded spaces after callsign to 9 characters total)

**Sending Message**:
1. Select target callsign from station list (received stations)
2. Type message (67 char max)
3. Send — radio transmits message packet
4. Target station receives, sends ACK (acknowledgment)
5. If no ACK within 30 seconds, retry (up to 5 attempts)

**Use Cases**:
- Status updates to emergency net ("At shelter, 20 people, need water")
- Coordination ("Meet at waypoint 5")
- Welfare checks ("Family safe")

**Limitations**:
- Not real-time (packets may take 1-5 minutes to deliver via multi-hop)
- Short messages only (67 characters)
- No encryption (all messages public)

### APRS for Emergency Communications

**Scenario**: Hurricane evacuation, cell towers down, need to coordinate multiple vehicles.

**Setup**:
1. Each vehicle has APRS-capable radio (Kenwood TM-D710GA or smartphone + Mobilinkd + Baofeng)
2. All stations set to 144.390 MHz, APRS enabled, GPS active
3. Vehicles beacon position every 2-5 minutes (SmartBeaconing)

**Operations**:
- Track all vehicles on map (each vehicle sees others' positions)
- Send messages ("Shelter full, proceed to alternate location")
- Monitor net ("All stations check in via APRS message")

**Digipeater Network**: If operating >5 miles from base station, use digipeaters. Packet includes routing path:
```
WIDE1-1,WIDE2-2
```
- WIDE1-1: Single-hop digipeater (first digi relays once)
- WIDE2-2: Two-hop network (relayed by up to 2 digis)

**Typical range**: 5-10 miles direct, 50-100 miles via digipeater network.

### APRS Common Mistakes

- ❌ **Beacon rate too fast**: Every 10-30 seconds floods network, QRM (interference)
- ✓ **SmartBeaconing or 1-5 min rate**: Adequate for tracking, doesn't congest frequency
- ❌ **Wrong frequency**: 144.390 is North America only
- ✓ **Check regional APRS frequency**: 144.800 (EU), 145.175 (AU)
- ❌ **No digipeater path**: Limited to line-of-sight range
- ✓ **Use WIDE1-1,WIDE2-2**: Extended range via digipeater network
- ❌ **Excessive message retries**: Sending same message 20× (network congestion)
- ✓ **Limit retries to 5**: If no ACK, recipient not in range

## Mode 2: Winlink (Email Over Radio)

**Winlink** is global email system using amateur radio (HF and VHF) for transport. Store-and-forward architecture allows offline email exchange.

### Winlink Fundamentals

**Network Architecture**:
- **CMS** (Common Message Server): Central server stores messages (Seattle, Washington)
- **RMS** (Radio Message Server): Radio gateways connect to CMS, forward messages to/from RF
  - **RMS Relay**: HF gateway (worldwide coverage)
  - **RMS Packet**: VHF packet gateway (local coverage, 5-30 miles)
- **Client Software**: User runs Winlink Express on computer, connects to RMS via radio

**Use Cases**:
- Email to/from internet email addresses (Gmail, Yahoo, etc.)
- Peer-to-peer radio email (ham-to-ham, no internet)
- Form-based messages (ICS-213 incident reports, radiograms)
- File attachments (documents, small images)
- Weather forecasts (NOAA GRIB files for marine navigation)

**Legal Restrictions**:
- Non-commercial content only (FCC Part 97)
- No encryption (amateur radio rule)
- No third-party traffic for non-licensed persons (in U.S., some exemptions)

### Equipment for Winlink

**HF Winlink (Worldwide Coverage)**:
- **HF Radio**: 100W transceiver with SSB (3-30 MHz)
  - Yaesu FT-891 ($600), ICOM IC-7300 ($1100), Xiegu G90 ($450)
- **Antenna**: HF antenna (dipole, vertical, or end-fed half-wave, see l3-tech-antenna-construction.md)
- **Interface**: Sound card interface (SignaLink USB, $120) or radio with built-in USB
- **Computer**: Laptop with Winlink Express software (Windows)
- **Total**: $600-2000

**VHF Winlink (Local Coverage, 5-30 Miles)**:
- **VHF Radio**: FM transceiver (144-148 MHz)
  - Handheld (Baofeng UV-5R, $25) or mobile (Yaesu FTM-7250DR, $180)
- **TNC**: Terminal Node Controller for packet radio
  - Mobilinkd TNC3 ($75), Kantronics KPC-3+ ($150)
- **Antenna**: VHF ground plane or J-pole (see l3-tech-antenna-construction.md)
- **Computer**: Laptop with Winlink Express
- **Total**: $120-500

### Winlink Software Setup

**Step 1: Download Winlink Express**
- Website: winlink.org
- Platform: Windows (Linux via Wine, macOS not officially supported)
- Install: Run installer, follow prompts

**Step 2: Configure Callsign**
- Enter your callsign
- Optionally register account on winlink.org (not required, but enables additional features)

**Step 3: Add Radio Channel**

**For HF Winlink (Pactor, VARA)**:
1. Open Settings → Channel Setup → Add
2. Select modem type:
   - **PACTOR**: Proprietary, requires hardware modem (SCS PTC-IIe, $1200+). Very robust, 200-5000 bps
   - **VARA HF**: Software modem (free for ham use), 100-3000 bps, no additional hardware
   - **ARDOP**: Open-source modem, 200-2000 bps (less robust than VARA, more compatible)
3. Configure radio control (CAT control via USB/serial, frequency, PTT)
4. Set frequency: Scan list or specific RMS frequency
   - Winlink uses 3.5, 7, 10, 14, 18, 21 MHz bands (see frequency list in Winlink Express)

**For VHF Winlink (Packet)**:
1. Add packet channel (144-148 MHz)
2. Configure TNC connection (serial or USB)
3. Set frequency: 145.010 MHz (common VHF Winlink frequency in North America, varies by region)

**Step 4: Test Connection**
1. Select channel from list
2. Click **Open Session**
3. Winlink connects to RMS, logs in, downloads message headers, synchronizes
4. First connection may take 2-5 minutes (HF) or 30-60 seconds (VHF packet)

### Sending Winlink Email

**Step 1: Compose Message**
1. Click **New Message**
2. **To**: Email address (any internet email, e.g., friend@gmail.com) or tactical address (ICS-213, radiogram templates)
3. **Subject**: Brief (subject line transmitted, consumes bandwidth)
4. **Body**: Text message (recommended <5000 characters for HF, <1000 for VHF packet)
5. **Attachments**: Small files only (<100 KB for HF, <10 KB for VHF)

**Step 2: Post to Outbox**
- Click **Post to Outbox** (does not transmit yet)
- Message stored locally, queued for transmission

**Step 3: Open Session & Send**
1. Select channel (HF or VHF)
2. Click **Open Session**
3. Winlink connects to RMS, uploads outbox messages, downloads inbox messages
4. Session completes (30 seconds to 5 minutes depending on traffic and propagation)

**Step 4: Confirm Delivery**
- Check Winlink Express **Sent** folder
- Status: "Delivered to CMS" = message reached central server, will be forwarded to recipient's email

### Receiving Winlink Email

**Polling**: Open session to check for new messages (manually or on schedule)

**Automatic Polling**:
- Configure Winlink Express to poll every 1-12 hours
- Radio must remain on, connected, and in coverage of RMS

**When Message Arrives**:
1. Winlink downloads message from RMS
2. Notification appears (if enabled)
3. Message stored in **Inbox**
4. Read message, reply, or forward

### Winlink Emergency Communications

**Scenario**: Wildfire evacuation, internet down, need to send situation report (SITREP) to county emergency management.

**Setup**:
1. Laptop with Winlink Express, HF radio (50-100W), VARA HF modem
2. Antenna: 40m dipole or portable vertical
3. County EOC (Emergency Operations Center) has Winlink-capable station or internet email

**Operations**:
1. Compose ICS-213 form (built-in Winlink template)
   - Incident: Wildfire evacuation
   - Status: 150 evacuees at Red Cross shelter
   - Resources needed: Water (500 gallons), food (200 meals), medical supplies
2. Address to county email: eoc@county.gov
3. Post to Outbox
4. Open Winlink session on 40m band (7.100 MHz, VARA HF)
5. Message transmitted to RMS gateway, forwarded via internet to eoc@county.gov
6. Delivery time: 1-10 minutes (depending on propagation, RMS availability)

**Reply**:
- County replies via email (internet or Winlink)
- Reply received during next Winlink poll (check every 1-2 hours during emergency)

### Winlink Peer-to-Peer (No Internet)

**P2P Mode**: Send email directly between two Winlink stations without RMS (no internet required).

**Setup**:
1. Both stations on same frequency (pre-arranged)
2. Station A initiates P2P session
3. Station B responds, connection established
4. Messages exchanged directly (no CMS/RMS)

**Use Case**: Isolated area, no RMS gateway available, but two Winlink stations in range.

**Limitations**: 
- Both stations must be online simultaneously
- Messages not stored on CMS (no forwarding to internet email addresses unless later relayed)

### Winlink Common Mistakes

- ❌ **Large attachments**: Sending 5 MB PDF over HF (takes 30+ minutes, ties up frequency)
- ✓ **Compress/resize attachments**: <100 KB for HF, <10 KB for VHF packet, text preferred
- ❌ **Hourly polling**: Excessive RMS connection attempts (congests gateway)
- ✓ **Poll every 4-12 hours**: Adequate for non-urgent communications
- ❌ **Not checking propagation**: Trying to connect on 20m at midnight (no propagation)
- ✓ **Check propagation predictions**: Use 40m/80m at night, 20m/15m during day
- ❌ **Commercial content**: "Can you order supplies from Amazon for me?" (illegal)
- ✓ **Personal, non-commercial only**: FCC Part 97 rules

## Mode 3: FT8 / FT4 (Weak Signal Digital)

**FT8** (Franke-Taylor 8-FSK) and **FT4** (faster variant) are weak-signal digital modes developed by Joe Taylor (K1JT, Nobel Prize laureate) for amateur radio. Extremely robust, decodes signals 10-15 dB below noise floor.

### FT8/FT4 Fundamentals

**Characteristics**:
- **FT8**: 15-second transmission cycle, 50 Hz bandwidth, -24 dB SNR decode threshold
- **FT4**: 7.5-second transmission cycle (2× faster than FT8), similar sensitivity
- **Applications**: DX contacts, propagation monitoring, weak-signal work
- **Automated**: Software handles message exchange (callsigns, signal reports, grid squares)

**Transmission Cycle** (FT8):
```
:00 seconds — Receive period begins (listen)
:15 seconds — Transmit period begins (your turn to transmit, if configured)
:30 seconds — Receive period begins
:45 seconds — Transmit period begins
:00 seconds — Cycle repeats
```

**Time Synchronization**: **CRITICAL**. FT8/FT4 require system time accurate to **±1 second**. Use:
- Internet NTP (before emergency)
- GPS time source (GPS receiver provides accurate UTC time)
- WWV time signal (2.5, 5, 10, 15, 20 MHz voice time announcements)

**Message Exchange** (Typical FT8 QSO):
```
Station 1: CQ W1ABC FN42     (Calling CQ, grid square FN42)
Station 2: W1ABC K2XYZ FN32  (Responding, grid square FN32)
Station 1: K2XYZ W1ABC -15   (Signal report -15 dB SNR)
Station 2: W1ABC K2XYZ R-10  (Report received, your report -10 dB)
Station 1: K2XYZ W1ABC RRR   (Confirm, thank you)
Station 2: W1ABC K2XYZ 73    (Goodbye, QSO complete)
```

Total QSO time: 90 seconds (6× 15-second cycles).

### Equipment for FT8/FT4

**Radio**:
- **HF**: Any SSB transceiver (3-30 MHz, 5-100W)
- **VHF/UHF**: FM or SSB transceiver (144, 222, 432 MHz)

**Interface**:
- Sound card interface (SignaLink, RigBlaster, DIY)
- Radio with USB audio (ICOM IC-7300, Yaesu FT-891)

**Computer**:
- **Minimum**: 2 GHz CPU, 4 GB RAM (FT8 is CPU-intensive during decode)
- **Recommended**: Multi-core CPU, 8 GB RAM
- **Time Sync**: GPS USB receiver ($25) or internet NTP

**Software**: **WSJT-X** (free, Windows/macOS/Linux)
- Website: physics.princeton.edu/pulsar/k1jt/wsjtx.html
- Developed by K1JT (Joe Taylor)

### WSJT-X Setup

**Step 1: Install WSJT-X**
- Download from website, install

**Step 2: Configure Radio**
- Settings → Radio → Select radio model (if supported by CAT control)
- Configure serial/USB port, baud rate
- Test connection (radio frequency should display in WSJT-X)

**Step 3: Configure Audio**
- Settings → Audio → Select sound card input/output
- **Input**: Radio audio output to computer (speaker/line-out from radio)
- **Output**: Computer audio to radio mic input

**Step 4: Configure Station Info**
- Settings → General → Enter callsign, grid square (e.g., FN42, 4-character Maidenhead locator)
- Grid square: Find at levinecentral.com/ham/grid_square.php (enter ZIP/address)

**Step 5: Calibrate Audio Levels**
1. Tune radio to FT8 frequency (e.g., 14.074 MHz on 20m)
2. Listen — should hear warbling/chirping sounds every 15 seconds
3. Adjust radio volume so WSJT-X **waterfall** shows signals in green/yellow (not overdriven red)
4. Transmit test (generate tones, monitor ALC meter on radio)
5. Adjust WSJT-X **Pwr** slider (right side) to 30-50% — ALC should barely activate or remain at zero

**Step 6: Synchronize Time**
- Enable NTP (internet) or GPS time source
- WSJT-X displays time offset (should be <0.5 seconds)
- If offset >1 second, FT8 decodes will fail

### Operating FT8

**Step 1: Select Frequency**
- FT8 frequencies (USB mode):
  - **160m**: 1.840 MHz
  - **80m**: 3.573 MHz
  - **40m**: 7.074 MHz
  - **20m**: 14.074 MHz
  - **17m**: 18.100 MHz
  - **15m**: 21.074 MHz
  - **10m**: 28.074 MHz
  - **6m**: 50.313 MHz
  - **2m**: 144.174 MHz

**Step 2: Enable RX (Receive)**
- Click **Enable Rx** (monitor mode)
- WSJT-X displays decoded callsigns, grid squares, signal reports in **Band Activity** pane

**Step 3: Calling CQ**
1. Set **Tx** (transmit) frequency (typically 1000-2000 Hz offset, shown on waterfall)
2. Type message: `CQ W1ABC FN42` (automatically formatted)
3. Click **Enable Tx**
4. WSJT-X transmits during assigned time slot (odd or even 15-second periods)

**Step 4: Responding to CQ**
1. Double-click callsign in **Band Activity** pane (station calling CQ)
2. WSJT-X populates **Tx** message: `W1ABC K2XYZ FN32`
3. Click **Enable Tx**
4. Exchange continues automatically (signal reports, confirmation)
5. QSO completes after 6-8 transmissions (90-120 seconds)

**Step 5: Logging**
- WSJT-X logs QSO automatically (callsign, grid, frequency, mode, time)
- Export log to ADIF (Amateur Data Interchange Format) for upload to QRZ, LoTW (Logbook of the World)

### FT8 for Emergency Communications

**Limited Emergency Use**: FT8 is optimized for **weak signal DX contacts**, not real-time messaging. However, it's useful for:

**Propagation Monitoring**:
- Enable FT8 on 20m, 40m, monitor decoded stations
- Identify which bands are open (ionospheric propagation)
- Determine best frequency for voice or digital messaging (Winlink, JS8Call)

**Welfare Checks**:
- Send signal report to distant station (confirms radio path exists)
- Follow up with voice QSO or JS8Call for message exchange

**Not Suitable For**:
- Real-time messaging (FT8 messages are fixed-format signal reports, not free text)
- Multi-party nets (FT8 is point-to-point only)

### FT8 Common Mistakes

- ❌ **Incorrect time sync**: System time off by 2-3 seconds, no decodes
- ✓ **GPS time or NTP**: Keep time within ±0.5 seconds
- ❌ **Overdriving audio**: ALC pinned, splatter interference, signal distorted
- ✓ **Monitor ALC**: Zero or minimal activation during FT8 transmission
- ❌ **Transmitting on calling frequency**: CQ on exactly 14.074.000 (QRM)
- ✓ **Offset 1000-2000 Hz**: Transmit at 14.075.000-14.076.000 (dial + offset)

## Mode 4: JS8Call (Keyboard Chat)

**JS8Call** is digital mode derived from FT8, optimized for **keyboard-to-keyboard text messaging** instead of signal reports. Ideal for emergency messaging.

### JS8Call Fundamentals

**Characteristics**:
- **Weak signal performance**: Similar to FT8 (-24 dB SNR threshold)
- **Free-text messaging**: Type any message (not limited to callsigns/signal reports)
- **Store-and-forward**: Messages relayed via intermediate stations (mesh networking)
- **Modes**: Normal (15 sec), Fast (10 sec), Turbo (6 sec), Slow (30 sec)
- **Bandwidth**: 50 Hz (same as FT8, very narrow)

**Message Types**:
- **Directed**: Message to specific callsign (e.g., `@W1ABC Message text`)
- **Group**: Message to group (e.g., `@EMCOMM Status update`)
- **Relay**: Request another station relay message (`W1ABC>K2XYZ via W3DEF`)
- **Broadcast**: Message to all stations monitoring frequency

### Equipment for JS8Call

Same as FT8:
- HF or VHF/UHF radio with SSB
- Sound card interface or USB audio
- Computer with JS8Call software (free, Windows/macOS/Linux)
- Time synchronization (GPS or NTP, not as critical as FT8 but recommended)

### JS8Call Setup

**Step 1: Install JS8Call**
- Website: js8call.com
- Install (similar to WSJT-X, same developer)

**Step 2: Configure Radio & Audio**
- Same procedure as WSJT-X (see FT8 section above)
- Configure CAT control, audio input/output

**Step 3: Configure Station**
- Enter callsign, grid square
- Set profile: **Normal** speed (15-second transmissions, balance of speed and sensitivity)

**Step 4: Select Frequency**
- JS8Call frequencies (USB mode):
  - **160m**: 1.842 MHz
  - **80m**: 3.578 MHz
  - **40m**: 7.078 MHz
  - **20m**: 14.078 MHz
  - **30m**: 10.130 MHz (popular for JS8Call, no FT8 activity)
  - **17m**: 18.104 MHz
  - **15m**: 21.078 MHz
  - **10m**: 28.078 MHz

### Operating JS8Call

**Step 1: Monitor**
- JS8Call displays decoded messages in **Band Activity** and **Call Activity** panes
- See all stations transmitting, messages directed to you, and broadcast messages

**Step 2: Directed Message**
1. Click callsign in **Call Activity** (populates **Directed To** field)
2. Type message in **TX Text** box: `Message text here`
3. Click **Send Message** (or press Enter)
4. JS8Call transmits message in chunks (each 15-second transmission carries ~10-15 characters)
5. Long messages automatically segmented (multi-transmission)

**Step 3: Group Messaging**
1. Set **Directed To** field: `@EMCOMM` (or any group name, e.g., @ARES, @SKYWARN)
2. Type message
3. All stations monitoring `@EMCOMM` receive message

**Step 4: Store-and-Forward (Relay)**
- If distant station out of range, request relay:
  ```
  W1ABC>K2XYZ Message text via W3DEF
  ```
- W3DEF (intermediate station) relays message to K2XYZ
- Requires W3DEF to be monitoring and have relay enabled (Settings → Network → Enable Store and Forward)

**Step 5: Heartbeat & Auto-Reply**
- Enable **Heartbeat**: JS8Call automatically transmits position/status every 5-15 minutes (similar to APRS beacon)
- Auto-reply: Respond to queries automatically (e.g., "QUERY" message auto-returns status)

### JS8Call for Emergency Communications

**Scenario**: Power outage, need to coordinate with distant ham radio operators for supply delivery.

**Setup**:
- HF radio (40m band), JS8Call software, 50W power
- Antenna: 40m dipole (elevated, 30 feet)

**Operations**:
1. Tune to 7.078 MHz (40m JS8Call frequency)
2. Monitor **Band Activity** — identify active stations
3. Send directed message to supply coordinator:
   ```
   @W5XYZ Power out, shelter operational, need 50 gallons diesel for generator
   ```
4. W5XYZ receives message (may take 1-3 minutes depending on message length, propagation)
5. W5XYZ replies:
   ```
   @W1ABC Roger, diesel delivery scheduled 1800Z tomorrow
   ```
6. Confirm receipt:
   ```
   @W5XYZ Confirmed, standing by
   ```

**Advantages Over Voice**:
- Works in extremely weak signal conditions (voice unintelligible, JS8Call decodes)
- Written record (no misunderstandings from poor audio)
- Multi-station monitoring (everyone sees traffic, maintains situational awareness)

### JS8Call Common Mistakes

- ❌ **Not setting directed-to callsign**: Message transmitted as broadcast, may not be seen by intended recipient
- ✓ **Use directed messages**: `@CALLSIGN` or click callsign in pane
- ❌ **Long messages in fast mode**: Message fragmented, takes longer than slower mode
- ✓ **Use appropriate speed**: Normal for general use, Slow for weak signals, Fast for strong signals
- ❌ **Forgetting to enable store-and-forward**: Can't relay messages for others
- ✓ **Enable relay feature**: Help extend network range

## Mode 5: DMR / Fusion (Digital Voice)

**DMR** (Digital Mobile Radio) and **Fusion** (Yaesu System Fusion) are digital voice modes for VHF/UHF. Provide better audio quality, longer range, and integrated GPS/text messaging compared to analog FM.

### DMR Fundamentals

**Characteristics**:
- **Modulation**: 4-FSK (4-level Frequency Shift Keying)
- **Bandwidth**: 12.5 kHz (same as FM, compatible with existing channel allocations)
- **Audio Quality**: Clear and noise-free (within coverage), no static/hiss
- **Range**: 20-40% greater than analog FM (due to error correction and forward error correction)
- **Features**:
  - **Talkgroups**: Virtual channels (like chat rooms, e.g., Worldwide, Regional, Local)
  - **GPS**: Position transmitted with voice
  - **Text messaging**: Short SMS-like messages between radios
  - **ID**: Each radio has unique DMR ID (like phone number)

**DMR Tiers**:
- **Tier I**: Unlicensed (dPMR, not commonly used in amateur radio)
- **Tier II**: **Amateur radio DMR** (most ham DMR radios)
- **Tier III**: Commercial trunked systems (not used in amateur radio)

**Repeater Networks**:
- **Brandmeister**: Largest amateur DMR network, worldwide repeaters
- **DMR-MARC**: North American DMR network
- **Others**: Regional networks (YSF, NXDN)

### DMR Equipment

**Handheld Radios**:
- **Baofeng DM-1701**: $70, dual-band DMR (popular budget option)
- **Anytone AT-D878UV**: $180, color screen, GPS, Bluetooth
- **TYT MD-UV390**: $130, GPS, dual-band, large screen

**Mobile Radios**:
- **Anytone AT-D578UV**: $240, color touchscreen, APRS, GPS
- **TYT MD-9600**: $220, dual-band, GPS

**Repeater (RX/TX Gateway)**:
- MMDVM hotspot ($60-120): Low-power personal repeater, connects to internet-based DMR networks
- Full repeater ($1000-3000): High-power, connects multiple users to DMR network

### DMR ID Registration

**Required**: Each DMR user must register unique ID (like phone number).

**Registration**:
1. Visit radioid.net
2. Register account (free)
3. Enter callsign, name, location
4. Receive DMR ID (7-digit number, e.g., 3123456)
5. Program ID into radio (Settings → Radio ID)

### DMR Programming

**Codeplug**: DMR radios use "codeplug" (configuration file) containing channels, talk groups, contacts, zones.

**Programming Methods**:
1. **CPS (Customer Programming Software)**: PC software from radio manufacturer (e.g., Anytone CPS, TYT CPS)
2. **Editcp**: Third-party codeplug editor (more user-friendly, supports multiple radio brands)

**Programming Steps**:
1. Download CPS for your radio model
2. Connect radio to computer via USB cable
3. Read existing codeplug from radio
4. Add/edit channels:
   - **Channel Name**: "DMR Local Repeater"
   - **Frequency**: TX 442.000 / RX 447.000 MHz (example)
   - **Color Code**: 1 (repeater-specific, like CTCSS tone for DMR)
   - **Time Slot**: 1 or 2 (DMR repeaters multiplex two conversations on one frequency)
   - **Talk Group**: 31 (Worldwide), 3123 (North America), 3148 (California), etc.
5. Write codeplug to radio

### DMR Talk Groups

**Talk Groups** (TG) are virtual channels. Transmitting on a talk group sends your voice to all users on that TG (via repeater network).

**Common Talk Groups**:
| TG Number | Name | Scope |
|-----------|------|-------|
| **1** | Worldwide | Global (high traffic) |
| **2** | Local / Regional | Repeater-specific |
| **3** | North America | Continent-wide |
| **13** | Worldwide English | Global English-language |
| **31** | TAC 1 | Tactical / Simplex coordination |
| **3123** | North America Calling | Calling channel |
| **93** | EMCOMM | Emergency communications |
| **310** | TAC 310 | Tactical channel |

**Selecting Talk Group**:
1. Choose channel (programmed with repeater frequency and TG)
2. Press TG button (radio displays current TG, e.g., "TG 31")
3. Rotate knob to change TG (if radio supports dynamic TG switching)

### DMR Operation

**Step 1: Power On**
- Radio displays DMR mode, channel name, TG

**Step 2: Listen**
- Monitor TG for activity (like scanning CB channels)
- DMR displays **callsign of transmitting station** on screen

**Step 3: Transmit**
1. Press PTT (push-to-talk)
2. Wait for **beep** (1-second delay, repeater synchronization)
3. Speak normally (no need to over-enunciate)
4. Release PTT
5. Listen for response

**Step 4: GPS Position**
- If radio has GPS, position transmitted with voice automatically
- Other stations see your location on DMR network map (brandmeister.network map)

### DMR Text Messaging

**Send SMS**:
1. Menu → Messages → New Message
2. Enter recipient DMR ID (e.g., 3123456)
3. Type message (up to 144 characters)
4. Send (radio transmits via repeater)

**Receive SMS**:
- Alert tone, message icon appears
- Open Messages → Inbox → Read message

### Fusion (Yaesu System Fusion)

**Alternative to DMR**, developed by Yaesu. Similar features (digital voice, GPS, text).

**Differences**:
- **C4FM modulation** (continuous 4-level FM, different from DMR 4-FSK)
- **Wires-X**: Yaesu's internet-linked repeater system (like DMR Brandmeister)
- **Compatible radios**: Only Yaesu Fusion radios (not cross-compatible with DMR)

**Popular Fusion Radios**:
- Yaesu FT-70DR (handheld, $140)
- Yaesu FTM-400XDR (mobile, $380, includes APRS)

**Programming**: Simpler than DMR (no codeplug, program channels via radio keypad or Yaesu ADMS software)

### DMR/Fusion for Emergency Communications

**Use Cases**:
- **Incident nets**: TAC talk groups for event coordination
- **GPS tracking**: Real-time position display on network map
- **Text status updates**: "At shelter, 50 people, need water" (SMS to net control)
- **Clear audio**: Noise-free communications (better copy than analog FM in fringe areas)

**Limitations**:
- **Requires repeater or hotspot**: Simplex DMR/Fusion limited to 1-5 miles
- **Internet dependency**: Most DMR/Fusion networks require internet link to repeater (may fail during widespread outage)
- **Incompatibility**: DMR radios can't communicate with Fusion radios (different protocols)

### DMR Common Mistakes

- ❌ **Wrong color code**: Can't access repeater (like wrong CTCSS tone)
- ✓ **Match repeater color code**: Check repeaterbook.com for repeater details
- ❌ **Wrong time slot**: Transmitting on TS1, repeater expecting TS2
- ✓ **Program correct time slot**: Most repeaters use TS1 for local, TS2 for wide-area
- ❌ **Not registering DMR ID**: Radio transmits, but other users can't identify you
- ✓ **Register ID at radioid.net**: Takes 5 minutes, lasts lifetime

## Mode 6: SSTV (Slow Scan Television)

**SSTV** transmits still images over radio. Useful for sending maps, photos, documents, damage assessment images during emergencies.

### SSTV Fundamentals

**Characteristics**:
- **Transmission Time**: 30 seconds to 4 minutes per image (depends on mode and resolution)
- **Modulation**: FM audio tones (1500 Hz = sync, 1500-2300 Hz = brightness)
- **Modes**: Multiple formats
  - **Martin M1**: 114 seconds, 320×256 pixels, color (most common)
  - **Scottie S1**: 110 seconds, 320×256 pixels, color
  - **Robot 36**: 36 seconds, 320×240 pixels, color (faster, lower quality)
  - **PD120**: 126 seconds, 640×496 pixels, high quality

**Applications**:
- Damage assessment photos (post-disaster surveys)
- Maps with annotations (evacuation routes, hazard locations)
- Documents (ICS forms, supply inventories)
- Weather satellite images (NOAA APT images)

### Equipment for SSTV

**Radio**:
- HF SSB (3-30 MHz, 100W) or VHF/UHF FM
- SSTV most common on **14.230 MHz** (20-meter band, USB)

**Interface**:
- Sound card interface (same as FT8, Winlink)
- Audio: Radio speaker to computer line-in, computer speaker to radio mic

**Computer**:
- Windows, macOS, or Linux
- Webcam or image files

**Software**:
| Software | Platform | Cost | Features |
|----------|----------|------|----------|
| **MMSSTV** | Windows | Free | Most popular, full-featured SSTV |
| **QSSTV** | Linux | Free | Linux SSTV client |
| **MultiScan** | Windows | $35 | Commercial, advanced features |
| **Robot36** | Android | Free | Receive SSTV on smartphone |

### MMSSTV Setup (Windows)

**Step 1: Install MMSSTV**
- Download from hamsoft.ca/pages/mmsstv.php
- Install

**Step 2: Configure Audio**
- Options → Setup → Sound Card → Select input/output devices
- **Input**: Radio audio to computer
- **Output**: Computer audio to radio

**Step 3: Configure Radio**
- Set frequency: 14.230 MHz (20m, USB mode)
- Adjust audio levels (similar to FT8 setup)

**Step 4: Test Reception**
1. Listen on 14.230 MHz (busy on weekends, ISS SSTV events)
2. When SSTV signal heard (warbling tones), click **RX** (receive) in MMSSTV
3. Image appears line-by-line (top to bottom, 30-120 seconds)

### Sending SSTV Image

**Step 1: Select Image**
- File → Load Image (JPEG, PNG, BMP)
- Image displayed in MMSSTV preview window

**Step 2: Add Overlay Text**
- Edit → Add Text → Enter caption (e.g., "W1ABC, Shelter Status 2024-11-15")
- Text overlaid on image

**Step 3: Select SSTV Mode**
- Mode → Martin M1 (recommended, widely supported)

**Step 4: Transmit**
1. Key radio (press PTT or enable VOX)
2. Click **TX** (transmit) in MMSSTV
3. MMSSTV sends image as audio tones (114 seconds for Martin M1)
4. Receiving stations decode image in real-time

### SSTV for Emergency Communications

**Scenario**: Post-earthquake damage assessment, need to send photos of bridge damage to emergency management.

**Setup**:
- HF radio (20m band, 100W), MMSSTV software
- Digital camera or smartphone (transfer photos to laptop)

**Operations**:
1. Take photo of damaged bridge
2. Transfer to laptop, load into MMSSTV
3. Add text overlay: "W1ABC, Route 12 bridge damage, GPS: 37.123N 121.456W"
4. Tune to 14.230 MHz (20m SSTV frequency)
5. Announce on voice: "This is W1ABC, sending SSTV image in 10 seconds"
6. Transmit image (114 seconds)
7. Receiving stations (EOC, ARES net control) decode and forward image to officials

**Advantages**:
- Visual documentation (better than verbal description)
- Bandwidth-efficient (compared to satellite/cellular data)
- Works over HF (long-distance transmission without infrastructure)

### SSTV Common Mistakes

- ❌ **Wrong mode mismatch**: Transmitting Martin M1, receiver expecting Scottie S1 (image garbled)
- ✓ **Announce mode before transmission**: "Sending Martin M1 image"
- ❌ **Overdriving audio**: Image has slanted lines (timing errors from distortion)
- ✓ **Proper audio levels**: Same as FT8 (ALC zero or minimal)
- ❌ **Low-quality source image**: Pixelated, blurry result
- ✓ **Use high-resolution source**: 640×480+ (software downscales appropriately)

## Digital Mode Frequency Allocations

**HF Digital Mode Frequencies** (USB mode unless specified):
| Band | Mode | Frequency (MHz) | Notes |
|------|------|----------------|-------|
| **80m** | PSK31 | 3.580 | Popular digital calling frequency |
| **80m** | FT8 | 3.573 | |
| **80m** | RTTY | 3.590 | |
| **40m** | FT8 | 7.074 | Most active FT8 band |
| **40m** | JS8Call | 7.078 | |
| **40m** | PSK31 | 7.080 | |
| **40m** | RTTY | 7.045-7.080 | |
| **30m** | FT8 | 10.136 | |
| **30m** | JS8Call | 10.130 | Very popular JS8Call band |
| **20m** | FT8 | 14.074 | Daytime DX |
| **20m** | JS8Call | 14.078 | |
| **20m** | PSK31 | 14.070 | |
| **20m** | SSTV | 14.230 | Most active SSTV frequency |
| **20m** | RTTY | 14.085-14.095 | |
| **17m** | FT8 | 18.100 | |
| **15m** | FT8 | 21.074 | |
| **10m** | FT8 | 28.074 | |
| **2m** | FT8 | 144.174 | VHF propagation monitoring |
| **2m** | APRS | 144.390 | North America |

**Note**: All HF digital modes use **USB** (upper sideband), even on frequencies where LSB is normal for voice (e.g., 40m voice is LSB, but digital is USB).

## Conclusion

Digital radio modes provide critical capabilities for emergency communications:

- **APRS**: Real-time GPS tracking, position reporting, short messaging (VHF, local range)
- **Winlink**: Email without internet, store-and-forward messaging (HF worldwide, VHF local)
- **FT8/FT4**: Weak signal contacts, propagation monitoring (HF/VHF)
- **JS8Call**: Keyboard chat, free-text messaging, weak signal performance (HF)
- **DMR/Fusion**: Digital voice, GPS, text messaging, superior audio quality (VHF/UHF)
- **SSTV**: Image transmission, maps, photos, damage assessment (HF/VHF)

**Action Items**:
1. **Install software**: Winlink Express (email), WSJT-X (FT8), JS8Call (messaging)
2. **Build/buy interface**: Sound card interface ($30-120) or radio with USB audio
3. **Practice digital modes regularly**: Weekly Winlink check-in, FT8 contacts, JS8Call net
4. **Time synchronization**: GPS receiver ($25) or NTP (before emergency)
5. **Pre-program frequencies**: Save digital mode frequencies in radio memory channels

Digital modes require more setup than voice, but provide unmatched reliability, efficiency, and capabilities when infrastructure fails. Invest time learning before crisis.
