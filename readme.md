<h1 align="center">Telemetria Dinamica (Juno New Origin)</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Version-Alpha-green" alt="Version Badge" />
  <img src="https://wakatime.com/badge/user/8edf9756-b6e5-4a16-afcc-b737762a79ad/project/38867b66-57d9-4077-bdf0-969b5e37d355.svg" alt="WakaTime Badge" />
  <img src="https://img.shields.io/badge/Status-Developing-purple" alt="Status Badge" />
</p>

---

Sistema de **telemetria em tempo real via UDP**, projetado para receber dados continuamente, manter um **estado centralizado e thread-safe**, monitorar a conexão através de um **watchdog** e exportar **snapshots periódicos em JSON** para consumo por painéis ou outros sistemas.

O foco do projeto é a **robustez do core**, separando claramente recepção, processamento, monitoramento e exportação dos dados.

---

## Requisitos

- Python *3.10+*
- Sistema operacional com suporte a sinais  
  (Linux e Windows compatíveis)

---

## Configuração

As principais configurações do sistema estão localizadas em:

/src/config/settings.py

Nesse arquivo é possível configurar, entre outros pontos:

- Endereço e porta UDP
- Intervalo de exportação
- Timeout do watchdog
- Campos de telemetria esperados

⚠️ *Recomendado* ajustar essas configurações antes de iniciar o receptor.

---

## Inicialização

Para iniciar o core de telemetria, execute:

```bash
python ./src/main.py
```

Ao iniciar, o sistema irá:

1. Subir o receptor UDP
2. Ativar o watchdog de conexão
3. Iniciar o pipeline de exportação
4. Exibir logs estruturados no terminal

---

##  Funcionalidades

📡 Recebimento de dados via UDP

🔒 Estado centralizado e protegido por Lock

🐶 Watchdog para detecção de perda de conexão

📦 Exportação periódica de snapshots em JSON

🧵 Arquitetura baseada em threads

📊 Logs estruturados utilizando Rich

---

##  Modelo de Execução

O sistema utiliza multithreading, onde cada responsabilidade roda em sua própria thread:

Receptor UDP

Watchdog de conexão

Exportador de snapshots


⚠️ Importante:
Apesar do uso de múltiplas threads, o Python executa em um único núcleo (GIL).
Esse modelo é ideal para I/O intensivo, como rede e escrita em arquivos.

---

 Exemplo de Snapshot (JSON)
```json
{
  "timestamp": 1734567890.123,
  "connected": true,
  "telemetry": {
    "Velocity (m/s)": 123.4,
    "Altitude (m)": 4567,
    "Fuel (%)": 78.9
  }
}
```