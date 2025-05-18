# Simulação Educativa de Ataques a Exchanges Cripto

**Propósito:** Este projeto é uma simulação ética e educativa de como cibercriminosos exploram vulnerabilidades em exchanges de criptomoedas. Ele serve para conscientização e estudo técnico.

## Estrutura do Projeto

- `vulnerable_exchange/`: Um protótipo de exchange com falhas intencionais.
- `attacker_scripts/`: Scripts simulando ataques como phishing e exploração de APIs.
- `defenses/`: Medidas de segurança para evitar ou mitigar os ataques simulados.

## Tecnologias Utilizadas

- **Flask (Python)** para simulação da exchange web.
- Scripts auxiliares em **Python puro** para simular ataques e defesas.
- HTML básico para a interface de login vulnerável.

## Exemplos de Ataques Simulados

- **Phishing**: Script que simula o envio de e-mails maliciosos.
- **Exploração de API insegura**: Acesso a endpoints sem autenticação.

## Estratégias de Defesa Incluídas

- Reforço de autenticação (uso de MFA).
- Limitação de acesso à API.
- Detecção de padrões de acesso anômalos.

## Aviso Legal

**Este projeto é apenas para fins educativos e de conscientização. Não deve ser usado em sistemas reais.**

## Como Executar

1. Instale os requisitos:
   ```bash
   pip install -r vulnerable_exchange/requirements.txt
   python vulnerable_exchange/app.py
   http://localhost:5000
   
