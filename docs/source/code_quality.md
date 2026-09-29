# Qualidade de código

## Objetivo

Manter o código Python formatado, com imports consistentes e livre de erros
estáticos antes de integrar alterações.

## Ferramentas

- **Black**: formatação automática com limite de 88 caracteres.
- **isort**: organização dos imports no perfil compatível com Black.
- **Flake8**: análise estática e validação das regras PEP 8.
- **Tox**: execução reproduzível dos testes e das verificações de qualidade.

## Execução local

Instale as dependências de desenvolvimento e execute:

```bash
python -m pip install -r requirements-dev.txt
black .
isort .
flake8 .
tox
```

Para verificar sem modificar arquivos:

```bash
black --check .
isort --check-only .
```

## Correção de falhas

Execute Black e isort para corrigir problemas automáticos. Falhas do Flake8
devem ser corrigidas no arquivo indicado; imports realmente intencionais
podem receber uma exceção local documentada com `# noqa`.

O workflow `.github/workflows/code-quality.yml` executa `tox -e lint` em cada
push ou pull request para `main`.

## Regras de revisão

- Manter arquivos e símbolos Python em `snake_case`.
- Usar imports absolutos do projeto.
- Executar `tox` antes de abrir um pull request.
