---
id: l5-comm-encryption
title: Basic Encryption
category: L5_community_knowledge
subtopic: communications
tags:
- encryption
- security
- communications
region_relevance:
- global
confidence: high
difficulty: intermediate
summary: Caesar, Vigenere, and one-time pad ciphers protect message confidentiality.
warnings:
- Reused one-time pad keys break security completely; never reuse a pad
related_entries:
- l5-comm-morse-code
- l5-comm-runner-relay
sources:
- Kahn The Codebreakers
- Shannon Communication Theory of Secrecy
last_verified: '2026-02-24'
audit_status: verified
---

# Basic Encryption

## Overview

- Encryption: transform plaintext to
  unreadable ciphertext without the key
- Decryption: reverse with the key
- Authentication: proving message source
- Three levels: Caesar (weak), Vigenere
  (moderate), one-time pad (unbreakable)
- All require pre-shared key arrangement
- Enemy with key breaks any cipher; protect keys

## Caesar Cipher

- Shift each letter N positions in alphabet
- Key: a number 1-25
- A with key 3: A becomes D; B becomes E
- Decrypt: shift opposite direction
- Weakness: only 25 possible keys; crack in
  minutes by trying all shifts
- Use only for low-value messages
- Adequate for: basic privacy, not security

## Vigenere Cipher

- Key: a word or phrase
- Repeat key over message
- Each letter shifted by key letter value:
  A=0, B=1, C=2 ... Z=25
- M with key letter F (5): M+5 = R
- Much harder to break than Caesar
- Weakness: repeated key creates patterns;
  long keys are better
- Key length = message length: very strong

## One-Time Pad

- Key: random characters; same length as
  message; used exactly ONCE
- Encrypt: add key value to message value
  (modulo 26 for alphabet)
- Decrypt: subtract key value
- Mathematically unbreakable if:
  key is truly random, never reused,
  and kept secret
- Weakness: secure key distribution;
  pad must reach receiver safely

## Key Exchange

- Key must be exchanged in person or via
  trusted courier before encryption needed
- Written key: two copies; one each
- Destroy used portions of one-time pad
- Never send key and ciphertext together
- Verify delivery: confirm key received
  before operationally relying on it
- Change keys regularly; especially if
  exposure is suspected

## Message Authentication

- Simple: agreed prefix words or phrases
- Add hash: count total letters; include
  count in message; receiver verifies
- Agreed codebook words: "apple" = danger
- Challenge-response: pre-arranged Q&A
- Authentication prevents false orders
- Critical for command-and-control

## Long-Term Value

- Confidential records and messages
- Tactical communications security
- Protects medical and legal records
- Simple ciphers teachable quickly
- Cryptography is a community skill
