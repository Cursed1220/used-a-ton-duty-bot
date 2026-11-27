<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Used-A-Ton Customer Price List</title>
<style>
:root {
  --bg: #0b0d10;
  --panel: rgba(23, 26, 31, .92);
  --panel-2: #1b1f25;
  --gold: #d6a64a;
  --gold-light: #f0ca78;
  --text: #f6f2e9;
  --muted: #a9adb4;
  --line: rgba(214,166,74,.18);
  --shadow: 0 18px 50px rgba(0,0,0,.32);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 34px 22px 60px;
  font-family: Inter, "Segoe UI", Tahoma, sans-serif;
  color: var(--text);
  text-align: center;
  background:
    radial-gradient(circle at 15% 0%, rgba(214,166,74,.10), transparent 28%),
    radial-gradient(circle at 85% 12%, rgba(151,92,38,.08), transparent 24%),
    linear-gradient(180deg, #101318 0%, var(--bg) 45%, #080a0c 100%);
  min-height: 100vh;
}
.page-layout { max-width: 1500px; margin: 0 auto; }
.main-content {
  position: relative;
  padding: 30px;
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 26px;
  background: linear-gradient(180deg, rgba(27,31,37,.88), rgba(14,16,20,.92));
  box-shadow: var(--shadow);
  backdrop-filter: blur(14px);
  overflow: hidden;
}
.main-content::before {
  content: "";
  position: absolute; inset: 0 0 auto 0; height: 4px;
  background: linear-gradient(90deg, transparent, var(--gold), var(--gold-light), var(--gold), transparent);
}
h2#logo {
  margin: 6px 0 0;
  font-size: clamp(38px, 5vw, 62px);
  line-height: .95;
  letter-spacing: .11em;
  font-weight: 900;
  text-transform: uppercase;
  color: #fff9ed;
  text-shadow: 0 6px 26px rgba(0,0,0,.45);
}
h2#logo span {
  color: var(--gold-light);
  text-shadow:
    0 0 5px rgba(255, 214, 137, .28),
    0 0 12px rgba(211, 163, 73, .20),
    0 0 24px rgba(211, 163, 73, .10);
}
h1 {
  margin: 10px 0 24px;
  font-size: 14px;
  letter-spacing: .32em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 700;
}
.total {
  max-width: 520px;
  margin: 0 auto 18px;
  padding: 20px 26px;
  border-radius: 18px;
  border: 1px solid rgba(214,166,74,.25);
  background: linear-gradient(145deg, rgba(214,166,74,.12), rgba(255,255,255,.025));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.05), 0 12px 35px rgba(0,0,0,.22);
  font-size: 24px;
  font-weight: 800;
  color: var(--gold-light);
}
button {
  appearance: none;
  padding: 11px 22px;
  margin: 3px 4px 15px;
  border: 1px solid rgba(214,166,74,.35);
  border-radius: 12px;
  background: linear-gradient(180deg, #272b31, #1a1d22);
  color: #f8e8c5;
  font-weight: 750;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(0,0,0,.18);
  transition: transform .18s ease, border-color .18s ease, background .18s ease;
}
button:hover { transform: translateY(-2px); border-color: var(--gold-light); background: #2d3137; }
#searchBar {
  display: block;
  width: min(760px, 100%);
  margin: 6px auto 22px;
  padding: 15px 18px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.10);
  outline: none;
  background: rgba(7,9,11,.72);
  color: white;
  font-size: 15px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
  transition: border-color .18s ease, box-shadow .18s ease;
}
#searchBar:focus { border-color: rgba(214,166,74,.65); box-shadow: 0 0 0 4px rgba(214,166,74,.08); }
#searchBar::placeholder { color: #747982; }
.tabs {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px;
  margin: 0 auto 22px;
  padding: 7px;
  width: fit-content;
  max-width: 100%;
  border-radius: 16px;
  background: rgba(7,9,11,.55);
  border: 1px solid rgba(255,255,255,.06);
}
.tab {
  padding: 10px 15px;
  border-radius: 10px;
  cursor: pointer;
  color: #b9bdc4;
  font-size: 14px;
  font-weight: 700;
  transition: .18s ease;
}
.tab:hover { color: white; background: rgba(255,255,255,.045); }
.tab.active {
  color: #18130b;
  background: linear-gradient(135deg, var(--gold-light), var(--gold));
  box-shadow: 0 7px 18px rgba(214,166,74,.20);
}
.tab-content { display: none; }
.tab-content.active { display: block; }
table {
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
  border-spacing: 0;
  overflow: hidden;
  margin: 0;
  border: 1px solid rgba(255,255,255,.065);
  border-radius: 16px;
  background: rgba(12,14,17,.72);
  box-shadow: 0 14px 36px rgba(0,0,0,.18);
}
th {
  padding: 14px 12px;
  color: #e8c67e;
  background: #171a1f;
  border-bottom: 1px solid rgba(214,166,74,.18);
  font-size: 12px;
  letter-spacing: .09em;
  text-transform: uppercase;
}
td {
  padding: 11px 12px;
  border-bottom: 1px solid rgba(255,255,255,.045);
  color: #e8e8e8;
  transition: background .15s ease;
}
tbody tr:last-child td { border-bottom: 0; }
tbody tr:hover td { background: rgba(214,166,74,.055); }
table th:nth-child(1), table td:nth-child(1) { width: 55%; text-align: left; }
table th:nth-child(2), table td:nth-child(2) { width: 20%; text-align: center; }
table th:nth-child(3), table td:nth-child(3) { width: 25%; text-align: center; }
input[type="number"] {
  width: 82px;
  padding: 8px 7px;
  border-radius: 9px;
  border: 1px solid rgba(255,255,255,.12);
  outline: none;
  background: #0b0d10;
  color: white;
  text-align: center;
  font-weight: 700;
  transition: border-color .18s ease, box-shadow .18s ease;
}
input[type="number"]:focus { border-color: var(--gold); box-shadow: 0 0 0 3px rgba(214,166,74,.09); }
table td:nth-child(2) input[type="number"] { display: block; margin: 0 auto; }
#searchResults { display: none; width: 100%; }
body.searching .tabs { opacity: .58; }
body.searching .tab-content { display: none !important; }
body.searching #searchResults { display: block; }
#searchResults table { width: 100%; table-layout: fixed; }
#searchResults th:nth-child(1), #searchResults td:nth-child(1) { width: 55%; text-align: left; }
#searchResults th:nth-child(2), #searchResults td:nth-child(2) { width: 20%; text-align: center; }
#searchResults th:nth-child(3), #searchResults td:nth-child(3) { width: 25%; text-align: center; }
#searchResults .no-results { padding: 28px; color: var(--muted); text-align: center; }
@media (max-width: 700px) {
  body { padding: 14px 9px 30px; }
  .main-content { padding: 22px 10px; border-radius: 18px; }
  h2#logo { letter-spacing: .06em; }
  h1 { letter-spacing: .18em; font-size: 11px; }
  .total { font-size: 20px; }
  .tabs { gap: 5px; padding: 5px; }
  .tab { padding: 8px 9px; font-size: 12px; }
  th, td { padding: 9px 5px; font-size: 12px; }
  input[type="number"] { width: 66px; }
}

/* Used-A-Ton customer price list brand theme */
:root {
  color-scheme: dark;
  --bg: #080609;
  --panel: rgba(20, 10, 18, .94);
  --panel-2: #1a1019;
  --gold: #f2a52c;
  --gold-light: #ffd375;
  --pink: #ff168e;
  --pink-light: #ff69c4;
  --text: #fff8fc;
  --muted: #c8b5c3;
  --line: rgba(255, 39, 159, .28);
  --shadow: 0 24px 70px rgba(0,0,0,.58);
}
body {
  padding: 28px 20px 64px;
  background:
    radial-gradient(ellipse at 50% -12%, rgba(255,22,142,.24), transparent 42%),
    radial-gradient(circle at 8% 28%, rgba(242,165,44,.10), transparent 24%),
    radial-gradient(circle at 92% 40%, rgba(255,22,142,.09), transparent 27%),
    repeating-linear-gradient(135deg, rgba(255,255,255,.012) 0 1px, transparent 1px 7px),
    linear-gradient(180deg, #160b15 0%, #09070b 46%, #050407 100%);
}
.page-layout { max-width: 1440px; }
.main-content {
  padding: clamp(18px, 3vw, 42px);
  border: 1px solid rgba(255,96,183,.35);
  border-radius: 28px;
  background: linear-gradient(150deg, rgba(28,15,27,.97), rgba(9,8,12,.97) 58%, rgba(24,13,18,.98));
  box-shadow: var(--shadow), 0 0 42px rgba(255,22,142,.10), inset 0 1px rgba(255,255,255,.06);
}
.main-content::before { height: 3px; background: linear-gradient(90deg, transparent, var(--pink), var(--gold-light), #fff, var(--gold), var(--pink), transparent); }
h2#logo { margin: 0 auto; line-height: 0; }
h2#logo img { display: block; width: min(100%, 380px); height: auto; margin: 0 auto; filter: drop-shadow(0 12px 24px rgba(255,0,128,.17)); }
h1 { margin: 9px 0 24px; color: #f5d9e9; letter-spacing: .24em; font-size: 12px; }
h1::after { content: "✦  BUY  •  SELL  •  TRADE  •  TREASURE  ✦"; display: block; margin: 10px auto 0; color: var(--gold-light); font-size: 10px; letter-spacing: .22em; text-shadow: 0 0 15px rgba(255,168,55,.32); }
.total {
  border-color: rgba(255,192,90,.48);
  background: linear-gradient(135deg, rgba(255,22,142,.16), rgba(255,255,255,.035) 48%, rgba(242,165,44,.12));
  box-shadow: inset 0 1px rgba(255,255,255,.08), 0 12px 35px rgba(0,0,0,.28), 0 0 24px rgba(255,22,142,.08);
  color: var(--gold-light);
}
button { border-color: rgba(255,80,174,.45); background: linear-gradient(145deg, #382031, #1a111a); color: #fff1fa; }
button:hover { border-color: var(--pink-light); background: linear-gradient(145deg, #53213e, #25121f); }
button:focus-visible, .tab:focus-visible { outline: 2px solid var(--gold-light); outline-offset: 3px; }
#searchBar { background: rgba(8,6,10,.88); border-color: rgba(255,255,255,.13); }
#searchBar:focus { border-color: var(--pink-light); box-shadow: 0 0 0 4px rgba(255,22,142,.12); }
.tabs { background: rgba(7,5,9,.78); border-color: rgba(255,84,171,.19); }
.tab { color: #d0bdca; }
.tab:hover { color: #fff; background: rgba(255,22,142,.10); }
.tab.active { color: #260b1a; background: linear-gradient(135deg, #ffb6e1, #ff3fac 54%, #ffb94e); box-shadow: 0 7px 20px rgba(255,22,142,.24); }
table { background: rgba(10,7,12,.82); border-color: rgba(255,255,255,.09); }
th { color: #ffd78f; background: linear-gradient(180deg, #281622, #1b1019); border-bottom-color: rgba(255,67,165,.30); }
td { color: #f1eaf0; border-bottom-color: rgba(255,255,255,.055); }
tbody tr:hover td { background: rgba(255,22,142,.075); }
input[type="number"] { background: #0a080c; border-color: rgba(255,255,255,.16); }
input[type="number"]:focus { border-color: var(--pink-light); box-shadow: 0 0 0 3px rgba(255,22,142,.12); }
@media (max-width: 700px) {
  body { padding: 12px 8px 30px; }
  .main-content { padding: 18px 10px; border-radius: 19px; }
  h1 { letter-spacing: .14em; }
  h1::after { font-size: 8px; letter-spacing: .12em; }
}
</style>
</head>
<body>
<div class="page-layout">
<div class="main-content">
<h2 id="logo"><img alt="Used-A-Ton Pawnshop" src="used-a-ton-logo.png"/></h2>
<h1>Pawnshop Price List</h1>
<div class="total" id="totalPrices">
    Total: $0.00
</div>
<button onclick="calculatePrices()">Calculate</button>
<button onclick="clearPrices()" type="button">Clear</button>
<input id="searchBar" oninput="searchItems()" placeholder="Search..." type="text"/>
<div class="tabs">
<div class="tab active" data-tab="jewelry" onclick="switchTab('jewelry', this)">
        Jewelry
    </div>
<div class="tab" data-tab="electronics" onclick="switchTab('electronics', this)">
        Electronics
    </div>
<div class="tab" data-tab="eggs" onclick="switchTab('eggs', this)">
        Eggs
    </div>
<div class="tab" data-tab="metal" onclick="switchTab('metal', this)">
        Metal Detecting
    </div>
<div class="tab" data-tab="relics" onclick="switchTab('relics', this)">
        Relics &amp; Art
    </div>
<div class="tab" data-tab="misc" onclick="switchTab('misc', this)">
        Miscellaneous
    </div>
<div class="tab" data-tab="heist" onclick="switchTab('heist', this)">
        Heist
    </div>
</div>
<!-- =====================================================
     SEARCH RESULTS
     ===================================================== -->
<div id="searchResults">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody id="searchResultsBody"></tbody>
</table>
</div>
<!-- =====================================================
     JEWELRY
     ===================================================== -->
<div class="tab-content active" id="jewelry">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Buying Price</th>
</tr>
</thead>
<tbody id="jewelryItems"><tr><td>10K Gold Chain</td><td><input min="0" name="10K Gold Chain" type="number" value="0"/></td><td>$2,800.00</td></tr><tr><td>Asylum Gold Necklace</td><td><input min="0" name="Asylum Gold Necklace" type="number" value="0"/></td><td>$4,400.00</td></tr><tr><td>Asylum Prime Necklace</td><td><input min="0" name="Asylum Prime Necklace" type="number" value="0"/></td><td>$5,200.00</td></tr><tr><td>Canary Diamond Necklace</td><td><input min="0" name="Canary Diamond Necklace" type="number" value="0"/></td><td>$16,800.00</td></tr><tr><td>Canary Diamond Necklace Silver</td><td><input min="0" name="Canary Diamond Necklace Silver" type="number" value="0"/></td><td>$16,720.00</td></tr><tr><td>Diamond</td><td><input min="0" name="Diamond" type="number" value="0"/></td><td>$480.00</td></tr><tr><td>Diamond Bar</td><td><input min="0" name="Diamond Bar" type="number" value="0"/></td><td>$1,600.00</td></tr><tr><td>Diamond Earring / Silver</td><td><input min="0" name="Diamond Earring / Silver" type="number" value="0"/></td><td>$720.00</td></tr><tr><td>Diamond Necklace</td><td><input min="0" name="Diamond Necklace" type="number" value="0"/></td><td>$3,680.00</td></tr><tr><td>Diamond Ring Silver</td><td><input min="0" name="Diamond Ring Silver" type="number" value="0"/></td><td>$720.00</td></tr><tr><td>Dragon Ring</td><td><input min="0" name="Dragon Ring" type="number" value="0"/></td><td>$1,280.00</td></tr><tr><td>Emerald</td><td><input min="0" name="Emerald" type="number" value="0"/></td><td>$320.00</td></tr><tr><td>Emerald Earring / Silver</td><td><input min="0" name="Emerald Earring / Silver" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Emerald Ring / Silver</td><td><input min="0" name="Emerald Ring / Silver" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Gemstone Necklace</td><td><input min="0" name="Gemstone Necklace" type="number" value="0"/></td><td>$3,800.00</td></tr><tr><td>Gemstone Necklace Silver</td><td><input min="0" name="Gemstone Necklace Silver" type="number" value="0"/></td><td>$3,720.00</td></tr><tr><td>Gold Chain</td><td><input min="0" name="Gold Chain" type="number" value="0"/></td><td>$480.00</td></tr><tr><td>Gold Earring / Ingot</td><td><input min="0" name="Gold Earring / Ingot" type="number" value="0"/></td><td>$320.00</td></tr><tr><td>Gold Ring</td><td><input min="0" name="Gold Ring" type="number" value="0"/></td><td>$400.00</td></tr><tr><td>Goldbar</td><td><input min="0" name="Goldbar" type="number" value="0"/></td><td>$1,400.00</td></tr><tr><td>Rolex/Golden Watch</td><td><input min="0" name="Rolex/Golden Watch" type="number" value="0"/></td><td>$320.00</td></tr><tr><td>Ruby</td><td><input min="0" name="Ruby" type="number" value="0"/></td><td>$280.00</td></tr><tr><td>Ruby Chain</td><td><input min="0" name="Ruby Chain" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Ruby Earring</td><td><input min="0" name="Ruby Earring" type="number" value="0"/></td><td>$560.00</td></tr><tr><td>Ruby Earring Silver</td><td><input min="0" name="Ruby Earring Silver" type="number" value="0"/></td><td>$559.20</td></tr><tr><td>Ruby Ring / Silver</td><td><input min="0" name="Ruby Ring / Silver" type="number" value="0"/></td><td>$560.00</td></tr><tr><td>Ruby Wolf Earrings</td><td><input min="0" name="Ruby Wolf Earrings" type="number" value="0"/></td><td>$1,280.00</td></tr><tr><td>Sapphire</td><td><input min="0" name="Sapphire" type="number" value="0"/></td><td>$240.00</td></tr><tr><td>Sapphire Earring</td><td><input min="0" name="Sapphire Earring" type="number" value="0"/></td><td>$480.00</td></tr><tr><td>Sapphire Necklace</td><td><input min="0" name="Sapphire Necklace" type="number" value="0"/></td><td>$960.00</td></tr><tr><td>Sapphire Necklace Silver</td><td><input min="0" name="Sapphire Necklace Silver" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Sapphire Ring / Silver</td><td><input min="0" name="Sapphire Ring / Silver" type="number" value="0"/></td><td>$480.00</td></tr><tr><td>Silver Chain</td><td><input min="0" name="Silver Chain" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Silver Earring long</td><td><input min="0" name="Silver Earring long" type="number" value="0"/></td><td>$320.00</td></tr><tr><td>Silver Ring</td><td><input min="0" name="Silver Ring" type="number" value="0"/></td><td>$520.00</td></tr><tr><td>Skull Ring</td><td><input min="0" name="Skull Ring" type="number" value="0"/></td><td>$1,280.00</td></tr><tr><td>Sovereign Pendant</td><td><input min="0" name="Sovereign Pendant" type="number" value="0"/></td><td>$9,600.00</td></tr><tr><td>Uncut Diamond</td><td><input min="0" name="Uncut Diamond" type="number" value="0"/></td><td>$80.00</td></tr><tr><td>Uncut Emerald</td><td><input min="0" name="Uncut Emerald" type="number" value="0"/></td><td>$56.00</td></tr><tr><td>Uncut Ruby</td><td><input min="0" name="Uncut Ruby" type="number" value="0"/></td><td>$48.00</td></tr><tr><td>Uncut Sapphire</td><td><input min="0" name="Uncut Sapphire" type="number" value="0"/></td><td>$40.00</td></tr></tbody>
</table>
</div>
<!-- =====================================================
     ELECTRONICS
     ===================================================== -->
<div class="tab-content" id="electronics">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Buying Price</th>
</tr>
</thead>
<tbody id="electronicsItems"><tr><td>All-in-One Printer</td><td><input min="0" name="All-in-One Printer" type="number" value="0"/></td><td>$4,000.00</td></tr><tr><td>Astronomy Telescope</td><td><input min="0" name="Astronomy Telescope" type="number" value="0"/></td><td>$4,800.00</td></tr><tr><td>Audio System</td><td><input min="0" name="Audio System" type="number" value="0"/></td><td>$4,400.00</td></tr><tr><td>Camera</td><td><input min="0" name="Camera" type="number" value="0"/></td><td>$4,400.00</td></tr><tr><td>Classic Microwave</td><td><input min="0" name="Classic Microwave" type="number" value="0"/></td><td>$3,600.00</td></tr><tr><td>Classic Toaster</td><td><input min="0" name="Classic Toaster" type="number" value="0"/></td><td>$800.00</td></tr><tr><td>Coffee Maker</td><td><input min="0" name="Coffee Maker" type="number" value="0"/></td><td>$2,400.00</td></tr><tr><td>CRT Television</td><td><input min="0" name="CRT Television" type="number" value="0"/></td><td>$2,800.00</td></tr><tr><td>Data Drive</td><td><input min="0" name="Data Drive" type="number" value="0"/></td><td>$4,400.00</td></tr><tr><td>Digital Scales</td><td><input min="0" name="Digital Scales" type="number" value="0"/></td><td>$1,600.00</td></tr><tr><td>Electric Kettle</td><td><input min="0" name="Electric Kettle" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Gaming Console</td><td><input min="0" name="Gaming Console" type="number" value="0"/></td><td>$6,000.00</td></tr><tr><td>Gang Tablet</td><td><input min="0" name="Gang Tablet" type="number" value="0"/></td><td>$28,000.00</td></tr><tr><td>iPhone 13</td><td><input min="0" name="iPhone 13" type="number" value="0"/></td><td>$280.00</td></tr><tr><td>Laptop</td><td><input min="0" name="Laptop" type="number" value="0"/></td><td>$6,800.00</td></tr><tr><td>Laptop (Black with blue screen)</td><td><input min="0" name="Laptop (Black with blue screen)" type="number" value="0"/></td><td>$440.00</td></tr><tr><td>LCD Monitor</td><td><input min="0" name="LCD Monitor" type="number" value="0"/></td><td>$3,600.00</td></tr><tr><td>LED Television</td><td><input min="0" name="LED Television" type="number" value="0"/></td><td>$5,200.00</td></tr><tr><td>Microwave</td><td><input min="0" name="Microwave" type="number" value="0"/></td><td>$3,600.00</td></tr><tr><td>Modern Microwave</td><td><input min="0" name="Modern Microwave" type="number" value="0"/></td><td>$4,400.00</td></tr><tr><td>Modern Toaster</td><td><input min="0" name="Modern Toaster" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Music Dock</td><td><input min="0" name="Music Dock" type="number" value="0"/></td><td>$1,600.00</td></tr><tr><td>Portable Boombox</td><td><input min="0" name="Portable Boombox" type="number" value="0"/></td><td>$2,000.00</td></tr><tr><td>Professional Hair Dryer</td><td><input min="0" name="Professional Hair Dryer" type="number" value="0"/></td><td>$1,600.00</td></tr><tr><td>PS5</td><td><input min="0" name="PS5" type="number" value="0"/></td><td>$4,400.00</td></tr><tr><td>Radio Cassette Player</td><td><input min="0" name="Radio Cassette Player" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Samsung Phone</td><td><input min="0" name="Samsung Phone" type="number" value="0"/></td><td>$4,400.00</td></tr><tr><td>Smart Television</td><td><input min="0" name="Smart Television" type="number" value="0"/></td><td>$7,600.00</td></tr><tr><td>Stand Mixer</td><td><input min="0" name="Stand Mixer" type="number" value="0"/></td><td>$3,200.00</td></tr><tr><td>Stolen Computer</td><td><input min="0" name="Stolen Computer" type="number" value="0"/></td><td>$1,240.00</td></tr><tr><td>Stolen TV</td><td><input min="0" name="Stolen TV" type="number" value="0"/></td><td>$1,240.00</td></tr><tr><td>Tablet</td><td><input min="0" name="Tablet" type="number" value="0"/></td><td>$440.00</td></tr><tr><td>VCR Player</td><td><input min="0" name="VCR Player" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Xbox X</td><td><input min="0" name="Xbox X" type="number" value="0"/></td><td>$4,400.00</td></tr></tbody>
</table>
</div>
<!-- =====================================================
     EGGS
     ===================================================== -->
<div class="tab-content" id="eggs">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Buying Price</th>
</tr>
</thead>
<tbody id="eggsItems"><tr><td>Asylum Gold Egg</td><td><input min="0" name="Asylum Gold Egg" type="number" value="0"/></td><td>$80,000.00</td></tr><tr><td>Asylum Prime Egg</td><td><input min="0" name="Asylum Prime Egg" type="number" value="0"/></td><td>$120,000.00</td></tr><tr><td>Ballas Egg</td><td><input min="0" name="Ballas Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Boerboel Egg</td><td><input min="0" name="Boerboel Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Boertjies Egg</td><td><input min="0" name="Boertjies Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Cartel Egg</td><td><input min="0" name="Cartel Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Dino Egg</td><td><input min="0" name="Dino Egg" type="number" value="0"/></td><td>$12,000.00</td></tr><tr><td>GSF Egg</td><td><input min="0" name="GSF Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Lost Egg</td><td><input min="0" name="Lost Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Mafia Egg</td><td><input min="0" name="Mafia Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Marabunta Egg</td><td><input min="0" name="Marabunta Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>SOA Egg</td><td><input min="0" name="SOA Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Vagos Egg</td><td><input min="0" name="Vagos Egg" type="number" value="0"/></td><td>$44,000.00</td></tr><tr><td>Yakhuza Egg</td><td><input min="0" name="Yakhuza Egg" type="number" value="0"/></td><td>$44,000.00</td></tr></tbody>
</table>
</div>
<!-- =====================================================
     METAL DETECTING
     ===================================================== -->
<div class="tab-content" id="metal">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Buying Price</th>
</tr>
</thead>
<tbody id="metalItems"><tr><td>Ancient Coin</td><td><input min="0" name="Ancient Coin" type="number" value="0"/></td><td>$1,040.00</td></tr><tr><td>Black Watch</td><td><input min="0" name="Black Watch" type="number" value="0"/></td><td>$520.00</td></tr><tr><td>Bottlecap</td><td><input min="0" name="Bottlecap" type="number" value="0"/></td><td>$8.00</td></tr><tr><td>Broken Junk</td><td><input min="0" name="Broken Junk" type="number" value="0"/></td><td>$80.00</td></tr><tr><td>Copper Nugget</td><td><input min="0" name="Copper Nugget" type="number" value="0"/></td><td>$360.00</td></tr><tr><td>Crushed Can</td><td><input min="0" name="Crushed Can" type="number" value="0"/></td><td>$160.00</td></tr><tr><td>Diamond Necklace Gold</td><td><input min="0" name="Diamond Necklace Gold" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Diamond Ring Gold</td><td><input min="0" name="Diamond Ring Gold" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Earpod</td><td><input min="0" name="Earpod" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Gold Dollar</td><td><input min="0" name="Gold Dollar" type="number" value="0"/></td><td>$1,040.00</td></tr><tr><td>Gold Earrings</td><td><input min="0" name="Gold Earrings" type="number" value="0"/></td><td>$960.00</td></tr><tr><td>Gold Necklace</td><td><input min="0" name="Gold Necklace" type="number" value="0"/></td><td>$1,120.00</td></tr><tr><td>Gold Nugget</td><td><input min="0" name="Gold Nugget" type="number" value="0"/></td><td>$1,400.00</td></tr><tr><td>Gold Ounce</td><td><input min="0" name="Gold Ounce" type="number" value="0"/></td><td>$1,480.00</td></tr><tr><td>Gold Ring</td><td><input min="0" name="Gold Ring" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Half Dollar</td><td><input min="0" name="Half Dollar" type="number" value="0"/></td><td>$680.00</td></tr><tr><td>Iron Nugget</td><td><input min="0" name="Iron Nugget" type="number" value="0"/></td><td>$600.00</td></tr><tr><td>Lighter</td><td><input min="0" name="Lighter" type="number" value="0"/></td><td>$9.60</td></tr><tr><td>Metal Can</td><td><input min="0" name="Metal Can" type="number" value="0"/></td><td>$11.20</td></tr><tr><td>Nails</td><td><input min="0" name="Nails" type="number" value="0"/></td><td>$14.40</td></tr><tr><td>Needle</td><td><input min="0" name="Needle" type="number" value="0"/></td><td>$16.00</td></tr><tr><td>Nickle</td><td><input min="0" name="Nickle" type="number" value="0"/></td><td>$240.00</td></tr><tr><td>Nutails</td><td><input min="0" name="Nutails" type="number" value="0"/></td><td>$17.60</td></tr><tr><td>Old Shotgunshell</td><td><input min="0" name="Old Shotgunshell" type="number" value="0"/></td><td>$20.00</td></tr><tr><td>Paperclip</td><td><input min="0" name="Paperclip" type="number" value="0"/></td><td>$22.40</td></tr><tr><td>Platinum Nugget</td><td><input min="0" name="Platinum Nugget" type="number" value="0"/></td><td>$1,360.00</td></tr><tr><td>Presidential Watch</td><td><input min="0" name="Presidential Watch" type="number" value="0"/></td><td>$1,120.00</td></tr><tr><td>Pulltab</td><td><input min="0" name="Pulltab" type="number" value="0"/></td><td>$28.00</td></tr><tr><td>Quarter</td><td><input min="0" name="Quarter" type="number" value="0"/></td><td>$480.00</td></tr><tr><td>Relic Revolver</td><td><input min="0" name="Relic Revolver" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Rusty Ball</td><td><input min="0" name="Rusty Ball" type="number" value="0"/></td><td>$36.00</td></tr><tr><td>Rusty Iron Ball</td><td><input min="0" name="Rusty Iron Ball" type="number" value="0"/></td><td>$44.00</td></tr><tr><td>Rusty Junk</td><td><input min="0" name="Rusty Junk" type="number" value="0"/></td><td>$56.00</td></tr><tr><td>Rusty Nails</td><td><input min="0" name="Rusty Nails" type="number" value="0"/></td><td>$72.00</td></tr><tr><td>Rusty Pliers</td><td><input min="0" name="Rusty Pliers" type="number" value="0"/></td><td>$88.00</td></tr><tr><td>Rusty Ring</td><td><input min="0" name="Rusty Ring" type="number" value="0"/></td><td>$160.00</td></tr><tr><td>Rusty Scissors</td><td><input min="0" name="Rusty Scissors" type="number" value="0"/></td><td>$176.00</td></tr><tr><td>Rusty Screwdriver</td><td><input min="0" name="Rusty Screwdriver" type="number" value="0"/></td><td>$184.00</td></tr><tr><td>Rusty Spring</td><td><input min="0" name="Rusty Spring" type="number" value="0"/></td><td>$200.00</td></tr><tr><td>Screw</td><td><input min="0" name="Screw" type="number" value="0"/></td><td>$216.00</td></tr><tr><td>Silver Dime</td><td><input min="0" name="Silver Dime" type="number" value="0"/></td><td>$520.00</td></tr><tr><td>Silver Earrings Hoops</td><td><input min="0" name="Silver Earrings Hoops" type="number" value="0"/></td><td>$800.00</td></tr><tr><td>Silver Ounce</td><td><input min="0" name="Silver Ounce" type="number" value="0"/></td><td>$960.00</td></tr><tr><td>Silver Ring</td><td><input min="0" name="Silver Ring" type="number" value="0"/></td><td>$800.00</td></tr><tr><td>Wheat Penny</td><td><input min="0" name="Wheat Penny" type="number" value="0"/></td><td>$224.00</td></tr></tbody>
</table>
</div>
<!-- =====================================================
     RELICS & ART
     ===================================================== -->
<div class="tab-content" id="relics">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Buying Price</th>
</tr>
</thead>
<tbody id="relicsItems"><tr><td>Art 1</td><td><input min="0" name="Art 1" type="number" value="0"/></td><td>$9,200.00</td></tr><tr><td>Art Painting</td><td><input min="0" name="Art Painting" type="number" value="0"/></td><td>$9,200.00</td></tr><tr><td>Asylum Doll</td><td><input min="0" name="Asylum Doll" type="number" value="0"/></td><td>$28,000.00</td></tr><tr><td>Fancy Kitty Art</td><td><input min="0" name="Fancy Kitty Art" type="number" value="0"/></td><td>$9,200.00</td></tr><tr><td>Presidential Kitty Art</td><td><input min="0" name="Presidential Kitty Art" type="number" value="0"/></td><td>$9,200.00</td></tr><tr><td>Obi Jesus Painting</td><td><input min="0" name="Obi Jesus Painting" type="number" value="0"/></td><td>$9,200.00</td></tr><tr><td>Captain Skull</td><td><input min="0" name="Captain Skull" type="number" value="0"/></td><td>$140,000.00</td></tr><tr><td>Captain Skull - KW</td><td><input min="0" name="Captain Skull - KW" type="number" value="0"/></td><td>$150,000.00</td></tr><tr><td>Decorated Pot</td><td><input min="0" name="Decorated Pot" type="number" value="0"/></td><td>$1,920.00</td></tr><tr><td>E Chain</td><td><input min="0" name="E Chain" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Fossil</td><td><input min="0" name="Fossil" type="number" value="0"/></td><td>$1,080.00</td></tr><tr><td>Mythic Fossil</td><td><input min="0" name="Mythic Fossil" type="number" value="0"/></td><td>$1,120.00</td></tr><tr><td>Onyx Relic</td><td><input min="0" name="Onyx Relic" type="number" value="0"/></td><td>$960.00</td></tr><tr><td>Panther</td><td><input min="0" name="Panther" type="number" value="0"/></td><td>$60,000.00</td></tr><tr><td>Pot</td><td><input min="0" name="Pot" type="number" value="0"/></td><td>$920.00</td></tr><tr><td>Prince Ruby</td><td><input min="0" name="Prince Ruby" type="number" value="0"/></td><td>$1,280.00</td></tr><tr><td>Rare Fossil</td><td><input min="0" name="Rare Fossil" type="number" value="0"/></td><td>$1,200.00</td></tr><tr><td>Relic</td><td><input min="0" name="Relic" type="number" value="0"/></td><td>$1,000.00</td></tr><tr><td>Skull</td><td><input min="0" name="Skull" type="number" value="0"/></td><td>$840.00</td></tr><tr><td>Slate Tablet</td><td><input min="0" name="Slate Tablet" type="number" value="0"/></td><td>$1,440.00</td></tr><tr><td>Time Capsule</td><td><input min="0" name="Time Capsule" type="number" value="0"/></td><td>$2,160.00</td></tr><tr><td>Canary Diamond</td><td><input min="0" name="Canary Diamond" type="number" value="0"/></td><td>$16,000.00</td></tr></tbody>
</table>
</div>
<!-- =====================================================
     MISCELLANEOUS
     ===================================================== -->
<div class="tab-content" id="misc">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Buying Price</th>
</tr>
</thead>
<tbody id="miscItems"><tr><td>Deluxe Treasure Map</td><td><input min="0" name="Deluxe Treasure Map" type="number" value="0"/></td><td>$720.00</td></tr><tr><td>Dirty Money (enter amount)</td><td><input min="0" name="Dirty Money (enter amount)" type="number" value="0"/></td><td>$0.80</td></tr><tr><td>Perlemoen</td><td><input min="0" name="Perlemoen" type="number" value="0"/></td><td>$8,000.00</td></tr><tr><td>Pogo</td><td><input min="0" name="Pogo" type="number" value="0"/></td><td>$60,000.00</td></tr><tr><td>Premium Treasure Map</td><td><input min="0" name="Premium Treasure Map" type="number" value="0"/></td><td>$640.00</td></tr><tr><td>Treasure Map</td><td><input min="0" name="Treasure Map" type="number" value="0"/></td><td>$520.00</td></tr><tr><td>Warehouse Key</td><td><input min="0" name="Warehouse Key" type="number" value="0"/></td><td>$400.00</td></tr></tbody>
</table>
</div>
<!-- =====================================================
     HEIST
     ===================================================== -->
<div class="tab-content" id="heist">
<table>
<thead>
<tr>
<th>Item</th>
<th>Quantity</th>
<th>Selling Price</th>
</tr>
</thead>
<tbody id="heistItems"><tr><td>HEIST - C4 Bomb</td><td><input min="0" name="HEIST - C4 Bomb" type="number" value="0"/></td><td>$80,000.00</td></tr><tr><td>HEIST - Drill</td><td><input min="0" name="HEIST - Drill" type="number" value="0"/></td><td>$9,000.00</td></tr><tr><td>HEIST - Big Drill</td><td><input min="0" name="HEIST - Big Drill" type="number" value="0"/></td><td>$20,000.00</td></tr><tr><td>HEIST - Gas Cutter</td><td><input min="0" name="HEIST - Gas Cutter" type="number" value="0"/></td><td>$20,000.00</td></tr><tr><td>HEIST - Cutter</td><td><input min="0" name="HEIST - Cutter" type="number" value="0"/></td><td>$25,000.00</td></tr><tr><td>HEIST - Large Drill</td><td><input min="0" name="HEIST - Large Drill" type="number" value="0"/></td><td>$15,000.00</td></tr><tr><td>HEIST - Blue Bag</td><td><input min="0" name="HEIST - Blue Bag" type="number" value="0"/></td><td>$6,500.00</td></tr><tr><td>HEIST - Bolt Cutter</td><td><input min="0" name="HEIST - Bolt Cutter" type="number" value="0"/></td><td>$16,000.00</td></tr><tr><td>HEIST - USB Pink</td><td><input min="0" name="HEIST - USB Pink" type="number" value="0"/></td><td>$9,000.00</td></tr><tr><td>HEIST - Green Laptop</td><td><input min="0" name="HEIST - Green Laptop" type="number" value="0"/></td><td>$25,000.00</td></tr><tr><td>HEIST - Advanced Drill</td><td><input min="0" name="HEIST - Advanced Drill" type="number" value="0"/></td><td>$15,000.00</td></tr><tr><td>HEIST - Plasma Cutter</td><td><input min="0" name="HEIST - Plasma Cutter" type="number" value="0"/></td><td>$15,000.00</td></tr><tr><td>HEIST - Gold Laptop</td><td><input min="0" name="HEIST - Gold Laptop" type="number" value="0"/></td><td>$35,000.00</td></tr><tr><td>HEIST - Hacking Laptop</td><td><input min="0" name="HEIST - Hacking Laptop" type="number" value="0"/></td><td>$35,000.00</td></tr><tr><td>HEIST - Advanced Lockpick</td><td><input min="0" name="HEIST - Advanced Lockpick" type="number" value="0"/></td><td>$10,000.00</td></tr><tr><td>HEIST - Lockpick</td><td><input min="0" name="HEIST - Lockpick" type="number" value="0"/></td><td>$12,000.00</td></tr><tr><td>HEIST - Doorlockpick</td><td><input min="0" name="HEIST - Doorlockpick" type="number" value="0"/></td><td>$12,000.00</td></tr><tr><td>HEIST - Ammunation Pass</td><td><input min="0" name="HEIST - Ammunation Pass" type="number" value="0"/></td><td>$10,000.00</td></tr><tr><td>HEIST - PD Pass</td><td><input min="0" name="HEIST - PD Pass" type="number" value="0"/></td><td>$10,000.00</td></tr><tr><td>HEIST - Thermite</td><td><input min="0" name="HEIST - Thermite" type="number" value="0"/></td><td>$30,000.00</td></tr><tr><td>HEIST - Gatecrack</td><td><input min="0" name="HEIST - Gatecrack" type="number" value="0"/></td><td>$8,000.00</td></tr><tr><td>HEIST - Bandage x10</td><td><input min="0" name="HEIST - Bandage x10" type="number" value="0"/></td><td>$40,000.00</td></tr><tr><td>HEIST - Hacking Device</td><td><input min="0" name="HEIST - Hacking Device" type="number" value="0"/></td><td>$8,000.00</td></tr><tr><td>HEIST - Software USB</td><td><input min="0" name="HEIST - Software USB" type="number" value="0"/></td><td>$8,000.00</td></tr><tr><td>HEIST - USB Device</td><td><input min="0" name="HEIST - USB Device" type="number" value="0"/></td><td>$8,000.00</td></tr><tr><td>HEIST - Switch Blade</td><td><input min="0" name="HEIST - Switch Blade" type="number" value="0"/></td><td>$15,000.00</td></tr></tbody>
</table>
</div>
</div>
</div>
<script>

/* ========================================================
   CLEAR
   Clears:
   - All quantities
   - Search bar
   - Search results
   - Total
   ======================================================== */

function clearPrices() {

    document
        .querySelectorAll('.tab-content input[type="number"]')
        .forEach(input => {
            input.value = 0;
        });

    const searchBar = document.getElementById('searchBar');

    if (searchBar) {
        searchBar.value = '';
    }

    document.body.classList.remove('searching');

    const searchResultsBody =
        document.getElementById('searchResultsBody');

    if (searchResultsBody) {
        searchResultsBody.innerHTML = '';
    }

    restoreActiveTab();

    updateTotal();
}


/* ========================================================
   RESTORE ACTIVE TAB
   ======================================================== */

function restoreActiveTab() {

    const sections =
        document.querySelectorAll('.tab-content');

    sections.forEach(section => {
        section.classList.remove('active');
    });

    let activeTab =
        document.querySelector('.tab.active');

    if (!activeTab) {

        activeTab =
            document.querySelector('.tab');

        if (activeTab) {
            activeTab.classList.add('active');
        }

    }

    if (!activeTab) {
        return;
    }

    const tabId =
        activeTab.dataset.tab;

    const selected =
        document.getElementById(tabId);

    if (selected) {
        selected.classList.add('active');
    }
}


/* ========================================================
   TAB SWITCHING
   ======================================================== */

function switchTab(tab, el) {

    document.querySelectorAll('.tab').forEach(t => {
        t.classList.remove('active');
    });

    if (el) {
        el.classList.add('active');
    }

    /*
       If there is text in the search bar,
       stay in search mode.
    */

    const filter =
        document.getElementById('searchBar')
            .value
            .trim();

    if (filter) {
        searchItems();
        return;
    }

    document.body.classList.remove('searching');

    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });

    const selected =
        document.getElementById(tab);

    if (selected) {
        selected.classList.add('active');
    }
}


/* ========================================================
   SEARCH

   Instead of opening several separate tables,
   this creates ONE clean search-results table.
   ======================================================== */

function searchItems() {

    const searchBar =
        document.getElementById('searchBar');

    const filter =
        searchBar.value
            .trim()
            .toLowerCase();

    const resultsBody =
        document.getElementById('searchResultsBody');


    /*
       SEARCH EMPTY:
       Return to normal tab layout.
    */

    if (!filter) {

        document.body.classList.remove('searching');

        resultsBody.innerHTML = '';

        restoreActiveTab();

        return;
    }


    /*
       SEARCH ACTIVE
    */

    document.body.classList.add('searching');

    resultsBody.innerHTML = '';

    let matchCount = 0;


    document
        .querySelectorAll('.tab-content tbody tr')
        .forEach(originalRow => {

            const itemCell =
                originalRow.cells[0];

            if (!itemCell) {
                return;
            }


            /*
               Search ONLY item names.
               Prices will not accidentally match.
            */

            const itemName =
                itemCell.innerText
                    .trim()
                    .toLowerCase();


            if (!itemName.includes(filter)) {
                return;
            }


            matchCount++;


            const originalInput =
                originalRow.querySelector(
                    'input[type="number"]'
                );


            const priceText =
                originalRow.cells[2]
                    ? originalRow.cells[2].innerText.trim()
                    : '$0.00';


            /*
               Create a clean search row.
            */

            const resultRow =
                document.createElement('tr');


            const itemTd =
                document.createElement('td');

            itemTd.textContent =
                itemCell.innerText.trim();


            const quantityTd =
                document.createElement('td');


            const searchInput =
                document.createElement('input');

            searchInput.type = 'number';

            searchInput.min = '0';

            searchInput.value =
                originalInput
                    ? originalInput.value
                    : 0;


            /*
               Link this search input back to the
               ORIGINAL item input.

               This means quantities entered while
               searching are still saved in the
               correct original item.
            */

            searchInput.addEventListener(
                'input',
                () => {

                    let value =
                        parseInt(
                            searchInput.value,
                            10
                        );

                    if (
                        isNaN(value) ||
                        value < 0
                    ) {
                        value = 0;
                    }


                    if (originalInput) {
                        originalInput.value = value;
                    }


                    updateTotal();

                }
            );


            quantityTd.appendChild(
                searchInput
            );


            const priceTd =
                document.createElement('td');

            priceTd.textContent =
                priceText;


            resultRow.appendChild(
                itemTd
            );

            resultRow.appendChild(
                quantityTd
            );

            resultRow.appendChild(
                priceTd
            );


            resultsBody.appendChild(
                resultRow
            );

        });


    /*
       No results message.
    */

    if (matchCount === 0) {

        const noResultsRow =
            document.createElement('tr');


        const noResultsCell =
            document.createElement('td');


        noResultsCell.colSpan = 3;

        noResultsCell.className =
            'no-results';

        noResultsCell.textContent =
            'No items found.';


        noResultsRow.appendChild(
            noResultsCell
        );


        resultsBody.appendChild(
            noResultsRow
        );

    }

}


/* ========================================================
   CALCULATE TOTAL

   Standard sections:
   Uses Buying Price.

   Heist:
   Uses Selling Price.

   Because both are the 3rd displayed column,
   cell index 2 works for both.
   ======================================================== */

function calculateTotal() {

    let total = 0;


    document
        .querySelectorAll('.tab-content tbody tr')
        .forEach(row => {

            const input =
                row.querySelector(
                    'input[type="number"]'
                );


            if (!input) {
                return;
            }


            const quantity =
                parseInt(
                    input.value,
                    10
                ) || 0;


            if (quantity <= 0) {
                return;
            }


            const priceCell =
                row.cells[2];


            if (!priceCell) {
                return;
            }


            const price =
                parseFloat(
                    priceCell
                        .innerText
                        .replace(/[$,]/g, '')
                ) || 0;


            total +=
                price * quantity;

        });


    return total;
}


/* ========================================================
   MONEY FORMAT
   ======================================================== */

function money(value) {

    return '$' +
        Number(value).toLocaleString(
            'en-US',
            {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }
        );

}


/* ========================================================
   UPDATE TOTAL
   ======================================================== */

function updateTotal() {

    const totalBox =
        document.getElementById(
            'totalPrices'
        );


    if (!totalBox) {
        return;
    }


    totalBox.textContent =
        'Total: ' +
        money(
            calculateTotal()
        );

}


/* ========================================================
   CALCULATE BUTTON
   ======================================================== */

function calculatePrices() {
    updateTotal();
}


/* ========================================================
   AUTO UPDATE TOTAL

   Only listens to the ORIGINAL item tables.
   Search-result inputs already update their
   original inputs and call updateTotal().
   ======================================================== */

document.addEventListener(
    'input',
    event => {

        if (
            event.target.matches(
                '.tab-content input[type="number"]'
            )
        ) {

            updateTotal();


            /*
               If search is open and an original input
               changes for any reason, refresh the
               search results so the values stay synced.
            */

            if (
                document.body.classList.contains(
                    'searching'
                )
            ) {

                searchItems();

            }

        }

    }
);


/* ========================================================
   STARTUP
   ======================================================== */

document.addEventListener(
    'DOMContentLoaded',
    () => {

        restoreActiveTab();

        updateTotal();

    }
);

</script>
</body>
</html>
