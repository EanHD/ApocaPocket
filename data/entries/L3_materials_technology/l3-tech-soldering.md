---
id: l3-tech-soldering
title: Electronics Basics -
layer: L3_materials_technology
category: electronics
tags: [soldering, electronics, repair, through-hole, SMD, desoldering, flux]
difficulty: intermediate
time_to_read: 20 minutes
practical_time: 1-2 hours practice required
---

# Electronics Basics -

Soldering is a skill. Expect ugly joints for the first 50-100 attempts. Practice on scrap boards before critical repairs.

## Iron Selection

Budget pencil (10-25 dollars): no temperature control. Too hot, oxidizes tip quickly. Fine for through-hole only.
Adjustable station (40-150 dollars): temperature controlled, replaceable tips. Best for most work.

Temperature: 650-700 F for leaded solder. 700-750 F for lead-free. Higher for large ground planes.
Tip selection: chisel tip for through-hole and large pads (maximum heat transfer). Conical for SMD and fine work.
Never file or sand tips. This destroys the plating.

Tip maintenance: tin before first use. Clean on damp sponge or brass wool after each joint. Re-tin immediately after cleaning. Store with solder on tip.

## Solder Types

60/40 leaded (recommended for beginners): melts 361-460 F. Easy to work, good wetting. Wash hands after use.
63/37 eutectic: sharp melt point (361 F), no plastic state. Less chance of disturbing joint.
SAC305 lead-free: melts 422 F. Requires higher iron temp (700-750 F). Harder to work with.
Diameter: 0.020-0.031 inch for general work. Thinner for SMD, thicker for bulk work.

## Through-Hole Technique

Wrong: touch solder to iron tip, drip onto joint. Result = cold joint (solder does not bond).

Correct:
1. Heat the joint (pad and lead together, not the solder). 1-2 seconds.
2. Apply solder to the joint, opposite side from iron. Solder melts from joint heat.
3. Feed until joint fills (small volcano shape around lead). 1-2 seconds.
4. Remove solder wire.
5. Remove iron. Hold still until solidified (1-2 seconds). Do not disturb.

Total time: 3-5 seconds per joint. Longer = component damage and pad delamination.

Good joint: smooth, shiny surface (leaded), concave fillet, solder wicks up lead and across pad.
Cold joint: dull, grainy surface. Reheat properly and re-flow.
Bridge: solder connects adjacent pads. Remove with solder wick.
Lifted pad: copper separates from board. Repair by jumping wire to next trace point.

Flux: apply rosin paste or pen flux to difficult joints (large ground planes, corroded pads). Improves success rate dramatically.

## SMD Techniques

Component sizes: 1206 and 0805 = beginner. 0603 = intermediate. 0402 and smaller = advanced (magnification required).

One-pin method for 0805 and larger passives:
1. Pre-tin one pad (small solder dot).
2. Hold component with tweezers, reheat pad, slide component into molten solder.
3. Solder second pad normally.

Drag soldering for SOIC ICs:
1. Apply flux to all pins.
2. Tack one corner pin to hold IC. Verify alignment.
3. Load iron with solder, drag slowly across pin row. Flux prevents bridges.
4. Clean bridges with solder wick.

Hot air (350-400 C): apply flux, heat with circular motion until solder melts (shiny), lift with tweezers.
Shield nearby components with aluminum foil tape to prevent unintentional reflow.

## Desoldering

Solder wick: place on joint, press hot iron on top of wick. Solder wicks into braid via capillary action.
Move to fresh wick section for each joint. Add flux to wick for better absorption.

Solder sucker: cock pump, heat joint until molten, remove iron, place nozzle, trigger. May take 2-3 attempts.

Through-hole removal: desolder all joints, then pull component. If stuck, reheat and wiggle gently.
Never force removal. Breaks pads and traces.

## Common Errors

- Dripping solder from iron tip: heat the joint, not the solder.
- Iron on joint over 5 seconds: damages component, lifts pads.
- Disturbing joint before solid: creates cold joint.
- Dirty or oxidized tip: does not transfer heat. Clean and re-tin constantly.
- Using acid-core solder (plumbing type): corrodes circuit traces. Use rosin-core electronics solder only.
- No flux on difficult joints: solder balls up instead of wetting surface.
- Excess solder (blob): may bridge adjacent pins. Use wick to remove.

## Safety

Fumes: rosin flux smoke is a respiratory irritant. Use fume extractor or fan blowing across work area.
Burns: iron tip is 650-800 F. Use iron stand always. Components stay hot 15-30 seconds after soldering.
Lead: wash hands after using leaded solder. No eating or drinking at work area.

---
Last updated: 2026-02-19
Layer: L3 Materials and Technology
