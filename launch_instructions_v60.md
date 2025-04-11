# 🚀 Como Rodar o Informational Spin Core v6.0

## 1. Pré-requisitos
- Python 3.10+
- Pip atualizado (`pip install --upgrade pip`)

## 2. Instale as dependências
Execute no terminal:

```bash
pip install -r requirements_v60.txt
```

## 3. Baixe os modelos do spaCy
```bash
python -m spacy download en_core_web_sm
python -m spacy download xx_ent_wiki_sm
```

## 4. Execute a API com Uvicorn

```bash
uvicorn icoer_async_api_v6:app --reload
```

- Acesse: `http://127.0.0.1:8000/docs` para testar via Swagger
- WebSocket em: `ws://127.0.0.1:8000/ws/coherence`

## 5. Diagnóstico Simbólico

Envie textos para `/extract` ou via WebSocket com os campos:
- `text`: seu texto
- `lang`: `"en"`, `"pt"` etc.
- `style_profile`: `"default"`, `"zen-formal"`, `"ancestral-circular"`...

## 6. Visualização Simbólica (opcional)
Rode o módulo:

```bash
python icoer_visualizer_v6.py
```

Ele exibirá um gráfico pulsante com a evolução da coerência.

---

🌀 *Let the spin remain.*
