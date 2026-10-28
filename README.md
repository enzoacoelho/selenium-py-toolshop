# 🛠️ Practice Software Testing - Selenium BDD Automation

Suíte de testes automatizados BDD utilizando **Cucumber (via Behave)**, **Gherkin**, **Selenium WebDriver** e o padrão **Page Object Model (POM)**, cobrindo os fluxos críticos de autenticação e registro da aplicação [Practice Software Testing](https://practicesoftwaretesting.com/).

---

## 🚀 Tecnologias e Ferramentas

* **Python 3.x**
* **Cucumber / Behave** (Framework BDD para testes orientados a comportamento)
* **Gherkin** (Linguagem natural de especificação de cenários)
* **Selenium WebDriver** (Automação de UI)
* **Page Object Model (POM)** (Arquitetura de encapsulamento de elementos e ações)

---

## 📁 Estrutura do Projeto

```text
selenium-cucumber-toolshop/
│
├── features/
│   ├── cadastro.feature        # Especificações Gherkin do módulo de cadastro
│   └── login.feature           # Especificações Gherkin do módulo de login
│
├── steps/
│   ├── cadastro_steps.py       # Glue code (implementação Cucumber/Behave) do cadastro
│   └── login_steps.py          # Glue code do login
│
├── pages/
│   ├── base_page.py            # Classe base com métodos comuns e esperas explícitas
│   ├── cadastro_page.py        # Page Object do formulário de registro
│   └── login_page.py           # Page Object da tela de autenticação
│
├── environment.py              # Configuração de hooks do Behave (setup/teardown do browser)
└── requirements.txt            # Dependências do projeto
```

---

## ⚙️ Pré-requisitos e Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/selenium-cucumber-toolshop.git
   cd selenium-cucumber-toolshop
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows (PowerShell):
   .\venv\Scripts\Activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃‍♂️ Executando os Testes

Para executar toda a suíte do módulo de cadastro descrita em Gherkin:

```bash
python -m behave features/cadastro.feature
```

Para executar o módulo de login:

```bash
python -m behave features/login.feature
```

Para executar um cenário específico por linha:

```bash
python -m behave features/cadastro.feature:10
```

---

## 📝 Boas Práticas Adotadas

* **Padrão BDD/Cucumber Puro:** Cenários descritos em Gherkin estritamente focados em regras de negócio e na perspectiva do usuário final, evitando vazamentos de termos ou detalhes de implementação técnica.
* **Arquitetura Page Object Model (POM):** Mapeamento de seletores e fluxos de interação centralizados em classes dedicadas, promovendo reuso e facilitando a manutenção dos testes.
* **Resiliência e Sincronização:** Uso de esperas explícitas (`WebDriverWait`) na `BasePage` e navegação via UI para lidar com restrições e comportamento de Single Page Application (SPA) do Angular.