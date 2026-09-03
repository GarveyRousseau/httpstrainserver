# ДатаХост — HTTP Lab (TSTU) Dark

Сайт-датахост для HTTP запросов. Не клон fitulki.ru, а свой концепт: хостинг тестовых данных.

## Run
```bash
python3 server.py
# https://localhost:4443/  -> Advanced -> Proceed
```

## Что это
Хост для учёбы HTTP: жми любой файл → `GET /path HTTP/1.1` → смотри в F12 Network и в консоли сервера `server.py:12`.

Dark theme inspired by fitulki.ru (Unbounded+Inter, borders) but own DataHost layout: `index.html:1` — hero + stats + ticker + 6 hosts grid.

## Hosts `index.html`
- **01 Image Host** `/images/` 20 jpg/png 700KB
- **02 Text Host** `/texts/` 21 txt RU/EN/DE/FR/ZH + big.txt 55KB
- **03 Video Host** `/videos/` 2× mp4 947KB (Range/206)
- **04 API Host** `/data/` json/xml/yaml/csv
- **05 File Host** `/data/` pdf/zip/bin/mp3 + css
- **06 How to** curl / F12 / logs

Всего 55 files ~3MB hosted локально. `css/style.css:1` dark.
