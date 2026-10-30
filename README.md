# Femboy Gary — MUGEN character prototype

## Downloads

- [Complete package: character, sprite sheets, and instructions](https://github.com/celerycore/femboygary/raw/refs/heads/main/femboygary-complete.zip)
- [MUGEN character only](https://github.com/celerycore/femboygary/raw/refs/heads/main/femboygary-mugen.zip)
- [Snail moveset sprite sheet](https://github.com/celerycore/femboygary/blob/main/assets/snail-moves.png)
- [FEMBOYS effect sprite sheet](https://github.com/celerycore/femboygary/blob/main/assets/femboys-effect.png)

If a direct ZIP link opens a GitHub file page, click **Download raw file**. For a private repository, sign in to GitHub first. File checksums are in `SHA256SUMS.txt`.

Pink snail and golden FEMBOYS effect based on the supplied reference. The generated artwork has 30 character poses and six text-effect frames. Uses MUGEN 1.0/1.1 SFF v1, AIR, CNS and CMD formats; should also be usable with IKEMEN GO. **Engine loading and live combat have not been verified in this environment.** This is an original, simplified MBAACC-inspired moveset, not an accurate port of MBAACC mechanics or frame data.

## Install

1. Copy `chars/femboygary` into your engine's `chars` directory.
2. Add `femboygary/femboygary.def` under `[Characters]` in `data/select.def`.
3. Start a versus or training match. The engine must include its standard `data/common1.cns` and default fight effects. No external character, sound archive, or palette file is required.

## Controls

Inputs use MUGEN button names, not keyboard keys; set your keyboard/gamepad bindings in the engine. Directions are relative to facing.

| Input | Action |
| --- | --- |
| x / y / z | Light / medium / heavy |
| Down + x/y/z | Crouching normals; heavy sweeps |
| Air x/y/z | Air normals |
| Up, then Up in the air | Jump / double jump |
| Forward, Forward | Run; air dash while airborne |
| Back, Back | Back hop; backward air dash while airborne |
| Hold back / down-back | Standard engine guard |
| a | Standing shield: 12-tick counter window, then recovery |
| Down, Down-forward, Forward + x | FEMBOYS text projectile |
| Down, Down-back, Back + y | Shell rush knockdown |
| Down, Forward, Down, Forward + z | Golden slogan super; costs 1000 power |

Light → medium → heavy chains on contact, including on guard. Standing normals can cancel on contact into specials or the super. One air dash per airtime. Shield does not counter throws or supers. Recovery uses the engine's standard x+y command. No custom AI, throws, audio, moon styles, heat/blood heat, reverse beat, or accurate MBAACC shield/guard systems are included.

## Artwork

- `assets/snail-sheet.png`: full transparent 6×6 generated master, 1254×1254.
- `assets/snail-moves.png`: five rows of character poses.
- `assets/femboys-effect.png`: separate six-frame effect strip.
- `assets/frames/`: 256×256 game frame PNGs, 128,232 sprite axes.
- `assets/frames.json`: group/image/axis mapping.
- `chars/femboygary/femboygary.air`: animation timing and collision boxes.

Rows in the master: idle/crawl; movement; light and medium attacks; heavy and aerial attacks; hurt/knockdown/getup/victory; text effect. Generated poses are concept-quality and may need alignment and hand cleanup. Collision boxes and balance are initial estimates. Sprites are rendered at 0.55 scale in a 320×240 local coordinate system.

## Rebuild

Python 3 and Pillow are needed only to rebuild assets, not to play. Use an isolated virtual environment if installing Pillow (`python -m pip install 'Pillow>=10,<14'`). From this repository:

```sh
python tools/write_states.py
python tools/build_character.py
python tools/validate_package.py
```

`write_states.py` regenerates the character text files; edit that source if retaining changes across rebuilds. `build_character.py` regenerates the indexed SFF and individual frames from the master image. Transparent palette entry zero is reserved; each PCX has its own palette.

## Validation status

The package validator checks every archived PCX, sprite references, required archive header fields, animation IDs, and file references. This verifies packaging, not engine parser compatibility or combat behavior. No MUGEN/IKEMEN engine is installed here. Before release, test both facing directions, all attacks and cancels, guarding and shield, air movement/landing, hit/KO/getup states, character-select portraits, and text projectile removal in your target engine.

Use the existing checkout for development; cloud tasks are isolated and do not need a separate Git worktree. No runtime services or credentials are needed for editing this package.
