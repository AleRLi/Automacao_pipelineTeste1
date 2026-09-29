# Automação de testes

Projeto de automação de testes com Selenium e Pytest.

## Qualidade de Código

As ferramentas de qualidade usam Python 3.11 e ficam configuradas em
`pyproject.toml`, `.flake8` e `tox.ini`.

```bash
# Instalar dependências de desenvolvimento
python -m pip install -r requirements-dev.txt

# Formatar código
black .

# Ordenar imports
isort .

# Verificar qualidade
flake8 .

# Executar testes e verificações de lint
tox
```

O workflow de qualidade é executado automaticamente em pushes e pull requests
para `main`.
