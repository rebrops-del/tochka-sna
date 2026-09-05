from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old_css = '''.hero{background:radial-gradient(circle at 84% 15%,rgba(235,249,241,.22),transparent 31%),linear-gradient(135deg,#318e68,#55ae80 58%,#82c9a6);color:#fff}.hero .wrap{padding:58px 0 54px}.eyebrow{display:inline-flex;align-items:center;gap:8px;background:#ffffff16;border:1px solid #ffffff2d;border-radius:999px;padding:8px 12px;font-size:12px;font-weight:800;margin-bottom:18px}.eyebrow:before{content:"";width:8px;height:8px;border-radius:50%;background:#fff34f}.hero h1{font-size:clamp(40px,5vw,66px);letter-spacing:-.04em;line-height:1.02;margin:0 0 18px;max-width:880px}.hero p{font-size:17px;line-height:1.65;color:#e6f1ea;max-width:800px;margin:0 0 24px}.actions{display:flex;gap:12px;flex-wrap:wrap}.advantages{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:30px}.adv{padding:18px;border-radius:18px;background:#ffffff12;border:1px solid #ffffff27}.adv strong{display:block;font-size:17px;margin-bottom:6px}.adv span{font-size:13px;line-height:1.45;color:#dbece2}'''

new_css = '''.hero{background:linear-gradient(112deg,#eef8f3 0%,#f8fbf9 50%,#f5f0e9 100%);color:#0b3e3d;overflow:hidden;border-bottom:1px solid #e0ece5}.hero .wrap{padding:40px 0 38px;display:grid;grid-template-columns:minmax(0,1.07fr) minmax(420px,.93fr);gap:30px;align-items:stretch;min-height:520px}.hero-copy{min-width:0;display:flex;flex-direction:column;justify-content:center;padding:4px 0}.hero .eyebrow{display:inline-flex;align-items:center;align-self:flex-start;gap:9px;background:#4eb57f;color:#fff;border:0;border-radius:999px;padding:10px 16px;font-size:12px;font-weight:900;margin:0 0 22px;box-shadow:0 10px 26px rgba(42,140,94,.18)}.hero-pin{display:inline-grid;place-items:center;width:17px;height:17px;border:2px solid #fff;border-radius:50%;font-size:0;position:relative}.hero-pin:after{content:"";width:4px;height:4px;background:#fff;border-radius:50%}.hero h1{font-size:clamp(44px,4.25vw,62px);letter-spacing:-.045em;line-height:1.03;margin:0 0 17px;max-width:670px;color:#083f46}.hero p{font-size:16.5px;line-height:1.58;color:#345b59;max-width:620px;margin:0 0 25px}.hero .actions{display:flex;gap:12px;flex-wrap:wrap;align-items:center}.hero .btn{min-height:55px;border-radius:999px;padding:0 25px;box-shadow:none}.hero .hero-primary{background:#0a8d55;color:#fff;border:1px solid #0a8d55;box-shadow:0 10px 24px rgba(10,141,85,.18)}.hero .hero-avito{background:rgba(255,255,255,.94);color:#0b503f;border:1.5px solid #159663;box-shadow:none;gap:12px}.avito-dots{display:grid;grid-template-columns:repeat(2,8px);gap:2px;margin-left:2px}.avito-dots i{display:block;width:8px;height:8px;border-radius:50%}.avito-dots i:nth-child(1){background:#00aaff}.avito-dots i:nth-child(2){background:#ff4053}.avito-dots i:nth-child(3){background:#965eeb}.avito-dots i:nth-child(4){background:#04e061}.hero .advantages{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:30px}.hero .adv{padding:0;display:grid;grid-template-columns:42px minmax(0,1fr);gap:8px;align-items:center;background:transparent;border:0;border-radius:0;box-shadow:none;min-width:0}.hero .adv strong{display:block;font-size:12.2px;line-height:1.32;margin:0;color:#123f3e}.hero .adv span{font-size:inherit;line-height:normal;color:inherit}.hero-adv-icon{width:42px;height:42px;border-radius:50%;background:#ddf4e8;display:grid;place-items:center;color:#0c8b55}.hero-adv-icon svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}.hero-visual{position:relative;min-height:470px;overflow:hidden;background:#f1ece5;align-self:stretch}.hero-visual img{position:absolute;inset:0;width:100%;height:100%;display:block;object-fit:cover;object-position:center center}.hero-visual:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(247,251,248,.38) 0%,rgba(247,251,248,.08) 19%,transparent 42%);pointer-events:none}.hero-note{position:absolute;z-index:2;right:5%;top:6.5%;color:#08755f;font-family:"Segoe Print","Bradley Hand",cursive;font-size:clamp(24px,2.05vw,33px);line-height:1.2;font-weight:600;transform:rotate(-4deg);text-align:center;text-shadow:0 1px 1px rgba(255,255,255,.94)}.hero-note span{font-size:1.16em}.hero-free{position:absolute;z-index:2;right:8%;top:32%;color:#17494a;font-size:12px;line-height:1.45;background:rgba(255,255,255,.72);padding:6px 9px;border-radius:8px;backdrop-filter:blur(2px)}'''

old_header = '''<header class="hero" id="top"><div class="wrap"><div class="eyebrow">Екатеринбургский филиал федеральной онлайн-сети</div><h1>Комфортный сон начинается с правильного матраса</h1><p>«Точка Сна» работает в онлайн-формате: консультация и подбор — дистанционно, заказ оформляется через Avito. Екатеринбургский филиал обслуживает город и ближайшие районы, региональный склад расположен в г. Берёзовский.</p><div class="actions"><a class="btn light" href="#catalog">Смотреть каталог</a><a class="btn avito" target="_blank" rel="noopener">Получить консультацию в Avito</a></div><div class="advantages"><div class="adv"><strong>Подбор по параметрам</strong><span>Учитываем вес, позу сна, желаемую жёсткость и бюджет.</span></div><div class="adv"><strong>Сравнение конструкций</strong><span>Поможем разобраться в беспружинных моделях, TFK и MultiPocket.</span></div><div class="adv"><strong>Сужаем выбор</strong><span>Вместо десятков вариантов предложим 2–3 модели под ваш запрос.</span></div></div></div></header>'''

new_header = '''<header class="hero" id="top"><div class="wrap"><div class="hero-copy"><div class="eyebrow"><span class="hero-pin" aria-hidden="true"></span>Екатеринбургский филиал федеральной онлайн-сети</div><h1>Комфортный сон начинается с правильного матраса</h1><p>Поможем подобрать матрас под ваши потребности: консультация, честные рекомендации и быстрая доставка по Екатеринбургу и ближайшим районам.</p><div class="actions"><a class="btn hero-primary" href="#catalog">Перейти в каталог <span aria-hidden="true">→</span></a><a class="btn hero-avito avito" target="_blank" rel="noopener">Получить консультацию в Avito <span class="avito-dots" aria-hidden="true"><i></i><i></i><i></i><i></i></span></a></div><div class="advantages" aria-label="Преимущества"><div class="adv"><span class="hero-adv-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M20 4C13 4 7 6.8 5.1 12.3 3.8 16 5.2 19.2 5.2 19.2s3.3 1.2 6.8-.6C17.2 16 20 10.4 20 4Z"/><path d="M5 20c3-5 6.2-7.9 10.4-10.4"/></svg></span><strong>Качественные и безопасные материалы</strong></div><div class="adv"><span class="hero-adv-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9 7 7M17 17l2.1 2.1M19.1 4.9 17 7M7 17l-2.1 2.1"/></svg></span><strong>Современные технологии</strong></div><div class="adv"><span class="hero-adv-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 3 20 6v5c0 5.2-3.3 8.4-8 10-4.7-1.6-8-4.8-8-10V6l8-3Z"/><path d="m8.5 12 2.2 2.2 4.8-5"/></svg></span><strong>Гарантия качества</strong></div><div class="adv"><span class="hero-adv-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><ellipse cx="9" cy="7" rx="5" ry="2.5"/><path d="M4 7v4c0 1.4 2.2 2.5 5 2.5s5-1.1 5-2.5V7M4 11v4c0 1.4 2.2 2.5 5 2.5 1.2 0 2.3-.2 3.1-.5"/><ellipse cx="16" cy="15" rx="4" ry="2"/><path d="M12 15v3c0 1.1 1.8 2 4 2s4-.9 4-2v-3"/></svg></span><strong>Отличное соотношение цены и качества</strong></div></div></div><div class="hero-visual"><img src="assets/hero-consultant-mattress.webp?v=20260905-hero-final" alt="Консультант Точка Сна рядом с матрасом" width="720" height="678" loading="eager" fetchpriority="high"><div class="hero-note">Помогу выбрать<br>ваш идеальный<br>матрас <span>♡</span></div><div class="hero-free">Бесплатная консультация<br>в удобном формате</div></div></div></header>'''

responsive = '''
@media(max-width:1080px) and (min-width:901px){.hero .advantages{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:900px){.hero .wrap{grid-template-columns:1fr;min-height:0;padding:38px 0 40px;gap:28px}.hero-copy{order:1}.hero-visual{order:2;min-height:0;aspect-ratio:720/678}.hero .advantages{grid-template-columns:repeat(2,minmax(0,1fr))}.hero h1{max-width:720px}}
@media(max-width:620px){.hero .wrap{padding:32px 0 34px;gap:22px}.hero .eyebrow{font-size:11px;padding:9px 13px;margin-bottom:19px}.hero h1{font-size:clamp(37px,11vw,48px)}.hero p{font-size:15px;line-height:1.55}.hero .actions{display:grid;grid-template-columns:1fr}.hero .btn{width:100%;padding:0 18px;min-height:54px}.hero .advantages{grid-template-columns:1fr 1fr;gap:14px 10px;margin-top:26px}.hero .adv{grid-template-columns:40px minmax(0,1fr);gap:8px}.hero-adv-icon{width:40px;height:40px}.hero .adv strong{font-size:12px}.hero-visual{aspect-ratio:1/1.02}.hero-note{right:4%;top:5%;font-size:clamp(23px,7vw,31px)}.hero-free{right:5%;top:31%;font-size:11px}}
@media(max-width:430px){.hero .advantages{grid-template-columns:1fr}.hero-visual{aspect-ratio:1/1.08}}
'''

if s.count(old_css) != 1:
    raise SystemExit(f'Expected exactly one old hero CSS block, found {s.count(old_css)}')
if s.count(old_header) != 1:
    raise SystemExit(f'Expected exactly one old hero header, found {s.count(old_header)}')

# Guardrails: anything after the hero and the entire JS must remain byte-identical.
tail_before = s.split('</header>', 1)[1]
script_before = s.split('<script>', 1)[1]

s = s.replace(old_css, new_css, 1)
s = s.replace(old_header, new_header, 1)
if '\n</style>' not in s:
    raise SystemExit('Closing style marker not found')
s = s.replace('\n</style>', responsive + '\n</style>', 1)

tail_after = s.split('</header>', 1)[1]
script_after = s.split('<script>', 1)[1]
if tail_before != tail_after:
    raise SystemExit('Guardrail failed: content below hero changed')
if script_before != script_after:
    raise SystemExit('Guardrail failed: JS changed')

checks = [
    'Поможем подобрать матрас под ваши потребности',
    'Перейти в каталог',
    'Получить консультацию в Avito',
    'Качественные и безопасные материалы',
    'Современные технологии',
    'Гарантия качества',
    'Отличное соотношение цены и качества',
    'assets/hero-consultant-mattress.webp?v=20260905-hero-final',
    'Помогу выбрать',
    'Бесплатная консультация'
]
for marker in checks:
    if marker not in s:
        raise SystemExit(f'Missing hero marker: {marker}')

hero = s.split('<header class="hero"', 1)[1].split('</header>', 1)[0]
if 'berhouse' in hero.lower():
    raise SystemExit('Forbidden Berhouse marker found in hero')

p.write_text(s, encoding='utf-8')
