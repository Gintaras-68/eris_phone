````markdown name=README.md
# 🔧 Eris Phone - AI Technical Support Agent

**Inteligentus techninio support'o agentas**, kuris teikia pagalbą klientams naudojant savos pagalbos sprendimus ir dirbtinį intelektą.

## ✨ Pagrindinės Funkcijos

🤖 **AI-Powered Support** - Automatinė kliento problemos klasifikacija  
📚 **Self-Help Solutions** - Detalūs žingsniai konkretiems prietaisams  
💬 **Multi-Channel** - Chat, email, telefonas (planuojama)  
📊 **Analytics** - Tiketo statistika ir suvestinės  
🧠 **Machine Learning** - Sistema mokosi iš feedback'o  

### Palaikomi Prietaisai

- ❄️ **Šaldytuvai** - Atitirpimas, efektyvumas
- 🧺 **Skalbykles** - Nuotekų valymas, kvapai
- 🔥 **Orkaitės** - Šildymas, stiklas
- 🍽️ **Indaplovės** - Valymas, nuotekos
- 📺 **Televizoriai** - Įsijungimas, garsas, vaizdo problemos
- 📶 **Mikrobangos pečius** - Šildymas, veikimas
- ⚡ **Kiti prietaisai** - Bendros problemos

## 🚀 Greita Pradžia

### Reikalavimas
- Docker & Docker Compose
- Python 3.9+
- Node.js 16+

### Paleisti Lokaliai

```bash
# 1. Klonuoti repo
git clone https://github.com/Gintaras-68/eris_phone.git
cd eris_phone

# 2. Naudoti Makefile komandas
make up          # Paleisti visą sistemą
make logs        # Matyti logs
make down        # Sustabdyti sistemą

# 3. Atidaryti aplikacijas
- Frontend: http://localhost:3000
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
```

## 📋 Architektūra

```
eris_phone/
├── backend/
│   ├── main.py              # FastAPI aplikacija
│   ├── models.py            # Duomenų modeliai
│   ├── ml_engine/           # Machine Learning modulis
│   ├── database/            # PostgreSQL schemos
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
├── docker-compose.yml       # Konteinerizacija
├── Makefile                 # Dev komandos
└── docs/                    # Dokumentacija
```

## 🔌 API Endpoints

### Kategorijos
```bash
GET /api/v1/categories
```

### Sprendimai
```bash
GET /api/v1/solutions/{category_id}
```

### Tiketo Kūrimas
```bash
POST /api/v1/support/ticket
{
  "category": "Skalbykles",
  "description": "Vandens neveizda"
}
```

### Tiketo Statusas
```bash
GET /api/v1/tickets/{ticket_id}
```

## 🛠️ Disponibilūs Sprendimai

### Šaldytuvai
- Atitirpinti šaldytuvą
- Šaldytuvas netaupli elektros

### Skalbykles
- Išvalyti nuotekų vamzdį
- Valykite nuo peleno

### Orkaitės
- Orkaitė nekaista
- Orkaitės stiklas žemiau

### Televizoriai
- Televizorius neįsijungia
- Nėra garso
- Nežalūs taškai ekrane

## 📊 Kitas Žingsnis

- [ ] WebSocket Chat integracijas
- [ ] ML modelio treniravimas
- [ ] Email/SMS integracijas
- [ ] Admin Dashboard
- [ ] Analitikos sistema
- [ ] Multilingual support

## 📝 Licencija

MIT License

## 👨‍💻 Autorius

**Gintaras-68** - AI Technical Support Project
````
