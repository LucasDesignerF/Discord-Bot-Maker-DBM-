---

# 🚀 Discord Bot Maker (DBM)

O **Discord Bot Maker (DBM)** é uma aplicação desktop avançada para Windows que permite criar, configurar e gerenciar bots do Discord de forma intuitiva e modular. Com uma interface gráfica robusta, você pode desenvolver bots personalizados com comandos, eventos e muito mais, sem precisar escrever código manualmente. 🤖✨

---

## 🎯 Funcionalidades Principais

- **🖥️ Interface Gráfica Amigável**:
  - Dashboard para gerenciar múltiplos bots.
  - Editor visual para criar comandos e eventos.
  - Painel de logs em tempo real.

- **🤖 Criação de Bots**:
  - Adicionar novos bots e configurar tokens, prefixos e intenções (intents).
  - Suporte a comandos de barra (Slash Commands).

- **🛠️ Editor de Comandos**:
  - Criar comandos personalizados com argumentos, permissões e respostas dinâmicas.

- **🎉 Gerenciador de Eventos**:
  - Configurar eventos como `on_message`, `on_member_join`, `on_reaction_add`, etc.

- **▶️ Reprodução de Bots**:
  - Iniciar, parar e reiniciar bots diretamente na interface.
  - Suporte a múltiplos bots rodando simultaneamente.

- **🧩 Extensibilidade**:
  - Sistema de plugins para adicionar funcionalidades extras.
  - API para desenvolvedores criarem plugins.

- **📥 Exportação/Importação**:
  - Salvar e carregar configurações de bots em arquivos `.dbm`.

---

## 🛠️ Tecnologias Utilizadas

- **🐍 Python 3.10+**: Linguagem principal do projeto.
- **🎨 PyQt6**: Para a interface gráfica.
- **🤖 discord.py**: Para interagir com a API do Discord.
- **🗃️ SQLAlchemy**: Para gerenciar o banco de dados local.
- **⏳ Asyncio**: Para operações assíncronas.
- **📦 PyInstaller**: Para empacotar a aplicação em um executável para Windows.

---

## 📸 Capturas de Tela

Aqui estão algumas imagens de exemplo da interface do **DBM**:

| **Dashboard** | **Editor de Comandos** | **Gerenciador de Eventos** |
|---------------|------------------------|----------------------------|
| ![Dashboard](https://dummyimage.com/600x400/000/fff&text=Dashboard) | ![Editor de Comandos](https://dummyimage.com/600x400/000/fff&text=Editor+de+Comandos) | ![Gerenciador de Eventos](https://dummyimage.com/600x400/000/fff&text=Gerenciador+de+Eventos) |

---

## 🚀 Instalação

### Pré-requisitos
- Python 3.10 ou superior.
- Git (opcional, para clonar o repositório).

### Passos para Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucasDesignerF/Discord-Bot-Maker-DBM-.git
   cd Discord-Bot-Maker-DBM-
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   python main.py
   ```

---

## 🎮 Como Usar

1. **🖥️ Dashboard**:
   - Insira o token do seu bot no campo "Token do Bot".
   - Clique em "Iniciar Bot" para rodar o bot.

2. **🛠️ Editor de Comandos**:
   - Crie comandos personalizados com argumentos e respostas dinâmicas.

3. **🎉 Gerenciador de Eventos**:
   - Configure eventos como `on_message`, `on_member_join`, etc.

4. **📜 Logs**:
   - Acompanhe os logs em tempo real para depuração e monitoramento.

5. **🧩 Plugins**:
   - Instale plugins para adicionar funcionalidades extras ao DBM.

---

## 📂 Estrutura do Projeto

```
discord-bot-maker/
│
├── main.py                # Ponto de entrada da aplicação
├── gui/                   # Módulo de interface gráfica
│   ├── __init__.py
│   ├── main_window.py     # Janela principal
│   ├── command_editor.py  # Editor de comandos
│   ├── event_manager.py   # Gerenciador de eventos
│   └── logs.py            # Painel de logs
├── core/                  # Módulo de núcleo
│   ├── __init__.py
│   ├── bot_manager.py     # Gerenciamento de bots
│   ├── command_handler.py # Processamento de comandos
│   └── event_handler.py   # Processamento de eventos
├── database/              # Módulo de banco de dados
│   ├── __init__.py
│   └── models.py          # Modelos de dados
├── plugins/               # Módulo de plugins
│   ├── __init__.py
│   └── plugin_api.py      # API para plugins
└── requirements.txt       # Dependências do projeto
```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m "Adicionando nova funcionalidade"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Contato

Se tiver dúvidas ou sugestões, entre em contato:

- **📧 E-mail**: ofc.rede@gmail.com
- **🐙 GitHub**: [LucasDesignerF](https://github.com/LucasDesignerF)
- **🎮 Discord**: [Code Projects](https://discord.gg/MjKrGpF44g)
```

---
