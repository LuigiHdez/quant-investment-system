cat > README.md << 'EOF'
# Quant Investment System

Sistema para simulación y predicción de mercados financieros.

## Instalación

```bash
git clone git@github.com:LuigiHdez/quant-investment-system.git
cd quant-investment-system
python -m venv venv
source venv/bin/activate   # o venv\Scripts\activate en Windows
pip install -r requirements.txt
cp .env.example .env
# Edita .env con tus símbolos y claves
