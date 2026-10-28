\# AI Daily Newsletter Agent



An AI-powered daily newsletter generator built using \*\*CrewAI\*\* and \*\*Streamlit\*\*. The project uses AI agents to research topics, gather information, and generate a structured newsletter through a simple web interface.



\## Features



\- \*\*AI-powered research:\*\* Research topics and gather relevant information.

\- \*\*Multi-agent workflow:\*\* Uses CrewAI to coordinate agents and tasks.

\- \*\*Automated newsletter generation:\*\* Produces organized research summaries.

\- \*\*Streamlit interface:\*\* Provides a simple web UI to interact with the application.

\- \*\*Modular architecture:\*\* Separates agents, tasks, tools, and crew configuration.



\## Tech Stack



\- Python

\- CrewAI

\- Streamlit

\- AI/LLM integrations

\- Research tools



\## Project Structure



```text

CrewAI-Research-Agent/

├── agents.py       # Defines AI agents

├── tasks.py        # Defines agent tasks

├── tools.py        # Research tools

├── crew.py         # Crew configuration

├── main.py         # Application entry point

├── app.py          # Streamlit web interface

├── .gitignore      # Files excluded from Git

└── README.md       # Project documentation

```



\## Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/vardhannehru/CrewAI-Research-Agent.git

cd CrewAI-Research-Agent

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



Activate it on Windows:



```powershell

.venv\\Scripts\\Activate.ps1

```



\### 3. Install dependencies



Install the dependencies required by the project. If a `requirements.txt` file is available, run:



```bash

pip install -r requirements.txt

```



Otherwise, install the packages specified by your project configuration.



\### 4. Configure environment variables



Create a `.env` file and add the API keys required by your configured LLM and research tools.



\*\*Security:\*\* Never commit API keys, passwords, or other secrets to GitHub.



\### 5. Run the application



For the Streamlit interface:



```bash

streamlit run app.py

```



Alternatively, run the main script if required by your workflow:



```bash

python main.py

```



\## Learning Objectives



\- Understand multi-agent AI workflows using CrewAI.

\- Learn how to define agents, tasks, and tools.

\- Explore AI-powered research and content generation.

\- Build a web interface for an AI application using Streamlit.



\## Future Improvements



\- Add configurable research topics.

\- Improve source citations and information verification.

\- Add newsletter export options.

\- Schedule automated daily newsletter generation.



\## Author



\*\*Vardhan Nehru\*\*



GitHub: \[@vardhannehru](https://github.com/vardhannehru)



