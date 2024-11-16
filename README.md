# Controle de Dispositivos via API Flask

Este projeto permite o controle de dispositivos conectados aos pinos GPIO de um Raspberry Pi, usando uma API Flask. A API expõe rotas para ligar e desligar dispositivos específicos, como impressora 3D, ventilador, luz e tomada, através de requisições HTTP.

## Endpoints da API

Abaixo estão as rotas disponíveis para controle dos dispositivos conectados. Cada dispositivo pode ser ligado (`/on`) ou desligado (`/off`) através de uma requisição GET.

### Base URL
```
http://192.168.8.225:5000
```

### Controle de Dispositivos

1. **Impressora 3D**
   - **Desligar**: `GET /api/pin/21/off`
     - Descrição: Desliga a impressora 3D conectada ao pino GPIO 21.
   - **Ligar**: `GET /api/pin/21/on`
     - Descrição: Liga a impressora 3D conectada ao pino GPIO 21.

2. **Ventilador**
   - **Desligar**: `GET /api/pin/22/off`
     - Descrição: Desliga o ventilador conectado ao pino GPIO 22.
   - **Ligar**: `GET /api/pin/22/on`
     - Descrição: Liga o ventilador conectado ao pino GPIO 22.

3. **Luz da Impressora 3D**
   - **Ligar**: `GET /api/pin/23/on`
     - Descrição: Liga a luz da impressora 3D conectada ao pino GPIO 23.
   - **Desligar**: `GET /api/pin/23/off`
     - Descrição: Desliga a luz da impressora 3D conectada ao pino GPIO 23.

4. **Tomada**
   - **Ligar**: `GET /api/pin/24/on`
     - Descrição: Liga a tomada conectada ao pino GPIO 24.
   - **Desligar**: `GET /api/pin/24/off`
     - Descrição: Desliga a tomada conectada ao pino GPIO 24.

### Exemplo de Requisição

Para fazer uma requisição HTTP e ligar um dispositivo, use `curl` ou seu navegador.

#### Exemplo usando `curl` para Ligar a Impressora 3D:
```bash
curl http://192.168.8.225:5000/api/pin/21/on
```

#### Exemplo usando `curl` para Desligar o Ventilador:
```bash
curl http://192.168.8.225:5000/api/pin/22/off
```

## Status dos Dispositivos

Para verificar o status atual de todos os dispositivos, acesse a rota abaixo:

- **Status de todos os dispositivos**: `GET /api/status/`
  - Retorna o status (on/off) de cada dispositivo e informações sobre a data e hora da consulta, além do nome do host.

#### Exemplo de Resposta JSON para `/api/status/`
```json
{
  "relay_21": "off",  // Impressora 3D
  "relay_22": "on",   // Ventilador
  "relay_23": "off",  // Luz da 3D
  "relay_24": "on",   // Tomada
  "datetime": "2024-11-16T10:25:30",
  "who": "pi-automation-3d"
}
```

## Observações

- Certifique-se de que o Raspberry Pi e o servidor Flask estejam ligados e conectados à rede para acessar as rotas.
- As rotas devem ser acessadas através do IP do Raspberry Pi (`192.168.8.225` no exemplo).
- **Atenção**: O uso inadequado desses comandos pode interferir no funcionamento dos dispositivos conectados.

## Dependências

- Python 3.x
- Flask
- RPi.GPIO (para controle dos pinos GPIO)

Para mais informações sobre instalação e configuração, consulte a documentação de cada biblioteca.

---

Este projeto fornece uma interface simples para o controle de dispositivos via rede. Aproveite o sistema para automação e monitoramento de dispositivos conectados ao Raspberry Pi!
```