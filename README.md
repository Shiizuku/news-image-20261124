# news-image-20261124 — The World in One Image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Shiizuku/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Shiizuku/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-page broadsheet summing up the world's news of **Tuesday 24 November 2026**,
built for the [make.fun](https://make.fun/bounty/news-image-20261124) daily news-image bounty.

## The six stories

1. **Quake shakes Nepal** — a magnitude 5.3 earthquake struck Nepal at 07:02,
   20 km deep; tremors felt across India, Bhutan, Bangladesh and China.
2. **Crown on the line** — Game 1 of the World Chess Championship opens in Geneva:
   defending champion Gukesh Dommaraju, 20, vs challenger Javokhir Sindarov, 20,
   the youngest title match ever (14 games, $2.5m fund).
3. **Fiji shuts schools** — all schools close five days (30 Nov – 4 Dec) as the
   El Niño drought crisis deepens.
4. **An island moves out** — Kiribati evacuates Kanton Island; all 40–50 residents
   relocated to Tarawa with a day's notice.
5. **Solomons PM flies to Canberra** — PM Matthew Wale heads to Australia to sign
   a landmark treaty.
6. **Fuel march in Bangkok** — the People's Revolutionary Front marches 16 km from
   Government House to the Bangchak refinery over fuel prices.

Sources: NCS, Chess.com, FIDE, PINA, AAP, The Island Sun, Bangkok reports.

## Files

- `entry.png` — the broadsheet, 1024×823, 105,321 bytes.
- `draw_image.py` — draws `entry.png` from scratch (Pillow; run twice, byte-identical).
- `main.py` — the entry program (Python 3.13, stdlib only): copies `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png` after verifying its SHA-256.

## Run

```sh
python3 draw_image.py            # rebuild entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
