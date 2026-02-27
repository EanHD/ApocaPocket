---
id: l3-tech-mesh-networks
title: Mesh Networks
layer: L3_materials_technology
category: communications
tags:
- mesh_networking
- Meshtastic
- LoRa
- WiFi_mesh
- Bluetooth_mesh
- OLSR
- Batman
- decentralized_networks
region_relevance:
- global
summary: "Mesh networking creates decentralized communication networks where each node relays data for others, eliminating single points of failure. Covers Meshtastic (LoRa, 5-50 mile range), Wi-Fi mesh (OLSR/Batman protocols, 100-500 meter range), Bluetooth mesh (10-100 meter range), node placement strategies, encryption, and emergency deployment for neighborhood-scale communications."
steps:
- "Select mesh technology based on range and bandwidth: Meshtastic/LoRa for long-range low-bandwidth (1-10 kbps), Wi-Fi mesh for medium-range high-bandwidth (1-50 Mbps), Bluetooth for short-range low-power"
- "Deploy minimum 3-5 nodes for reliable mesh (2 nodes = single point of failure, 3+ enables redundant paths)"
- "Optimize node placement for line-of-sight or near-line-of-sight between nodes (elevation, clear Fresnel zone)"
- "Configure mesh parameters: channel, encryption key, hop limit, routing protocol"
- "Test mesh connectivity and measure signal strength between nodes, add nodes to fill coverage gaps"
warnings:
- "LINE-OF-SIGHT: Mesh networks (especially LoRa, Wi-Fi) require line-of-sight or near-line-of-sight between nodes. Buildings, hills, dense foliage block signals. Deploy nodes on rooftops, hills, or elevated poles. A single blocked path can isolate entire neighborhood"
- "HOP LIMIT: Each relay (hop) adds latency (50-500ms per hop) and reduces effective bandwidth (50% per hop for Wi-Fi). Keep hop count <4 for usable real-time communications. 10-hop mesh has 10-20 second latency"
- "ENCRYPTION: Unencrypted mesh traffic is readable by anyone with compatible receiver. Always enable encryption (AES-256 for Meshtastic, WPA2/WPA3 for Wi-Fi mesh). Default encryption keys widely known  -  change immediately"
- "POWER: Mesh nodes require continuous power (solar + battery or grid). Single dead node can partition network. Plan battery capacity for 24-72 hours autonomy (LoRa: 1-5Ah, Wi-Fi: 20-100Ah)"
- "FREQUENCY REGULATIONS: LoRa operates on unlicensed ISM bands (915 MHz US, 868 MHz EU) with duty cycle limits (1-10% in EU, unlimited in US). Exceeding duty cycle violates regulations and degrades network performance"
- "BANDWIDTH LIMITS: Meshtastic/LoRa limited to 1-10 kbps (text messaging only, no voice/video). Wi-Fi mesh degrades rapidly with >10-20 active users per node. Bluetooth mesh limited to sensor data and short messages"
related_entries:
- l3-tech-radio-basics
- l3-tech-antenna-construction
- l3-tech-digital-radio
- l3-tech-propagation
sources:
- Meshtastic documentation (meshtastic.org)
- OLSR Protocol RFC 3626
- B.A.T.M.A.N. protocol documentation (open-mesh.org)
- LoRa Alliance specifications
- Bluetooth SIG mesh specifications
- FEMA AUXCOMM guidance on mesh networks
audit_status: verified
last_verified: 2026-02-19
confidence: high
offline_assets: []
---

# Mesh Networks

## What It Is

Mesh: every node relays data for others. No single point of failure. Works with no internet or cell service.

Three types:
- Meshtastic/LoRa: long range, low bandwidth. Text messages only. 1-50 miles per hop.
- Wi-Fi mesh: medium range, high bandwidth. 100-500 meters per node. Web and voice capable.
- Bluetooth mesh: short range, very low power. Sensors and short alerts only. 10-100 meters.

Use case: neighborhood communication when cell and internet are both down.

## Hardware Options

Meshtastic (best for disaster use):
- Heltec ESP32 LoRa v3: about $20. Compact, USB-programmable.
- LILYGO T-Beam: about $35. Built-in GPS and battery holder.
- RAK WisBlock: about $40. Modular, waterproof case options.
Frequency: 915 MHz in US. Pre-built units include antenna.

Wi-Fi mesh (neighborhood LAN):
- GL.iNet GL-AR750S: about $60. OpenWrt, dual-band, compact.
- TP-Link EAP series: about $50-100. Easy setup, managed interface.
- Ubiquiti airMAX: about $80-150. Long range, directional options available.

## Basic Setup

Meshtastic:
1. Flash firmware using Meshtastic web flasher (do this before any disaster).
2. Set region (US_915), channel name, and encryption key. All nodes must share the same key.
3. Pair to phone via Bluetooth. Use Meshtastic app to send and receive messages.
4. Nodes relay messages automatically up to default hop limit of 3.

Wi-Fi mesh (OpenWrt plus B.A.T.M.A.N.):
1. Flash OpenWrt on compatible router.
2. Install batman-adv package. Enable mesh interface on each node.
3. Nodes auto-discover neighbors. Present a single shared SSID to clients.
4. Connect any device to any node like normal Wi-Fi.

## Range Per Node

Meshtastic LoRa urban: 0.5-2 miles. Open terrain: 5-20 miles. Elevated: up to 50 miles.
Wi-Fi mesh outdoor: 200-500 meters between nodes. Indoor: 50-150 meters.
Bluetooth mesh: 10-30 meters typical.

Node density: plan one node per 0.5-1 mile in cities. Mount on rooftops or second floors.
Minimum viable network: 3 nodes. Two nodes is a single point of failure.

## Power Requirements

Meshtastic: 100-250 mA transmitting, 20-50 mA receiving. Small solar plus 10Ah battery = 24-72 hours.
Wi-Fi router node: 5-15W. 50Ah battery plus 50W solar panel = continuous operation.
Add 20% margin for cloudy days. Lithium batteries outperform lead-acid in cold weather.
A dead node can partition the network. Ensure power redundancy at critical relay positions.

## Disaster Use

Pre-position nodes at: community center, school, high-ground homes, any location with solar power.
Cover evacuation routes. Drop nodes at key intersections as network is built out.
Meshtastic requires zero power infrastructure. Fully self-contained with battery.
Change encryption key from default before deployment. The default key is publicly known.
Range-test nodes at intended positions before crisis. Walk each link and verify signal.
Combine with Winlink: HF Winlink gateway bridged to mesh gives email without internet.
