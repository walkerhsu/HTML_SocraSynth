## HTML Bonus Track

### Description

This is a bonus track that participates in a pilot project called SocraSynth. It is a project that aims to extract knowledge from Large Language Models (LLMs) towards
the unknown truth by holding a debate with 2 Agents.

### Installation

To see the result of our project, you can  clone the repository:

```bash
    git clone https://github.com/walkerhsu/HTML_SocraSynth.git
```

### Structure

#### Tree structure

The project is structured as follows:

```bash
    HTML_SocraSynth
    ├── README.md
    ├── .gitignore
    ├── all_statistics.py
    ├── all_subjects.csv
    ├── generate_CSV_folders.py
    ├── generate_files.py
    ├── generate_links.py
    ├── move_csv_to_folders.py
    ├── move_to_links_folders.py
    ├── score_distribution.png
    ├── settings_1106.json
    ├── subjects-private.csv
    ├── subjects-public.csv
    ├── Our_prompts
    │   ├── 2vs2_prompt.txt
    │   ├── David_prompt.txt
    │   ├── Oscar_prompt.txt
    │   ├── Walker_prompt.txt
    ├── CSV
    │   ├── subject1 (exist at least one of the following folders)
    │   │   ├── GPT3.5
    │   │   ├── Bard
    │   │   ├── GPT3.5-2
    │   ├── subject2 (exist at least one of the following folders)
    │   │   ├── GPT3.5
    │   │   ├── Bard
    │   │   ├── GPT3.5-2
    │   ├── ...
    │   ├── subjectN (exist at least one of the following folders)
    │   │   ├── GPT3.5
    │   │   ├── Bard
    │   │   ├── GPT3.5-2
    ├── links
    │   ├── subject1
    │   │   ├── links.txt
    │   ├── subject2
    │   │   ├── links.txt
    │   ├── ...
    │   ├── subjectN
    │   │   ├── links.txt
```

#### File description

- `all_statistics.py`: This file is used to generate the statistics of the results of the debate.

- `all_subjects.csv`: This file is used to store the score and id of subjects of the debate.

- `generate_CSV_folders.py`: This file is used to generate the folders of the subjects in CSV folders.

- `generate_files.py`: This file is used to generate the links' files of the subjects in links folders.

- `move_csv_to_folders.py`: This file is used to move the CSV files to the corresponding folders.

- `move_to_links_folders.py`: This file is used to move the links to the corresponding folders.

- `score_distribution.png`: This file is used to show the score distribution of all the subjects.

- `settings_1106.json`: This file is used to store the config settings of the GPT-4.0-1106.

- `subjects-private.csv`: This file is used to store the subjects' information of the private debate.

- `subjects-public.csv`: This file is used to store the subjects' information of the public debate.

- `Our_prompts`: This folder is used to store the prompts of the debate.

    - `2vs2_prompt.txt`: This file is used to store the prompt of the 2vs2 debate.

    - `David_prompt.txt`: This file is used to store the prompt of the David debate.

    - `Oscar_prompt.txt`: This file is used to store the prompt of the Oscar debate.

    - `Walker_prompt.txt`: This file is used to store the prompt of the Walker debate.

- `CSV`: This folder is used to store the CSV files of the debate.

    - GPT3.5: This folder is used to store the CSV files resulted from GPT-3.5-turbo.

    - Bard: This folder is used to store the CSV files resulted from Bard (PaLM-2.0).

    - GPT4.0: This folder is used to store the CSV files resulted from GPT-4.0-1106.
    
- `links`: This folder is used to store the links of the debate.
