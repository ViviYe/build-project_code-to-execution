
# Code To Execution – Workshop 1 Setup Guide

Welcome to the Build Fellowship project:

**Code To Execution: Build Your Own Interpreter**

Before Workshop 1, please complete this setup guide.

**Estimated setup time:** 20–45 minutes

---

# What You Need By Workshop 1

By the beginning of Workshop 1, you should have:

- Python 3 installed
- VS Code installed
- Git installed
- A GitHub account
- Your own GitHub repository
- A local copy of your repository on your computer
- A folder named `workshop1`
- The Workshop 1 notebook inside `workshop1`
- Ability to run notebook cells successfully

---

# Part 1: Create a GitHub Account

If you do not already have one:

1. Go to GitHub.com
2. Create an account
3. Verify your email

You will use this account throughout the fellowship.

---

# Part 2: Install Python

Recommended version:

Python 3.10+

---

## Windows Python Installation

### Step 1

Visit:

https://www.python.org/downloads/

### Step 2

Download the latest Python 3 release.

### Step 3

Run the installer.

IMPORTANT:

Check:

☑ Add Python to PATH

before clicking Install.

### Step 4

Open Command Prompt.

Run:

```bash
python --version
```

Expected:

```text
Python 3.x.x
```

If that doesn't work:

```bash
py --version
```

One of these should display a version.

### Step 5

Verify pip:

```bash
python -m pip --version
```

or

```bash
py -m pip --version
```

---

## Mac Python Installation (Recommended: Homebrew)

### Step 1

Open Terminal.

Check whether Homebrew exists:

```bash
brew --version
```

If it works, continue to Step 3.

### Step 2

Install Homebrew

Run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the instructions shown.

Restart Terminal.

Verify:

```bash
brew --version
```

### Step 3

Install Python

```bash
brew install python
```

### Step 4

Verify installation

```bash
python3 --version
```

Expected:

```text
Python 3.x.x
```

### Step 5

Verify pip

```bash
python3 -m pip --version
```

---

# Part 3: Install VS Code

Download:

https://code.visualstudio.com/

Install VS Code.

Open VS Code.

Install extensions:

1. Python (Microsoft)
2. Jupyter (Microsoft)

---

# Part 4: Install Jupyter

## Windows

```bash
py -m pip install notebook ipykernel
```

or

```bash
python -m pip install notebook ipykernel
```

## Mac

```bash
python3 -m pip install notebook ipykernel
```

Verify:

```bash
jupyter --version
```

---

# Part 5: Install Git

## Windows

Download:

https://git-scm.com/download/win

Install using default settings.

Verify:

```bash
git --version
```

---

## Mac

Most Macs already include Git.

Run:

```bash
git --version
```

If prompted to install Command Line Tools, accept.

Verify again:

```bash
git --version
```

---

# Part 6: Configure Git

Run once:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Verify:

```bash
git config --global --list
```

---

# Part 7: Create Your Repository

Go to GitHub.

Create a repository.

Repository name:

```text
build-interpreter-yourname
```

Examples:

```text
build-interpreter-john
build-interpreter-sarah
```

Settings:

- README ✓
- Python .gitignore ✓
- Public preferred
- No license

Create repository.

---

# Part 8: Clone Your Repository

Copy repository URL.

Example:

```text
https://github.com/john/build-interpreter-john.git
```

Open terminal.

Move to Desktop:

Windows:

```bash
cd Desktop
```

Mac:

```bash
cd ~/Desktop
```

Clone:

```bash
git clone YOUR_REPO_URL
```

Example:

```bash
git clone https://github.com/john/build-interpreter-john.git
```

Enter folder:

```bash
cd build-interpreter-john
```

---

# Part 9: Create Workshop 1 Folder

Inside your repository create:

```text
build-interpreter-yourname/
│
├── workshop1/
│
├── README.md
│
└── .gitignore
```

You only need the workshop1 folder for now.

Future workshops will get:

```text
workshop2/
workshop3/
...
```

---

# Part 10: Add Workshop 1 Notebook

Place:

```text
week1_symbols_recursion_trees_student.ipynb
```

inside:

```text
workshop1/
```

Final structure:

```text
build-interpreter-yourname/
│
├── workshop1/
│   └── week1_symbols_recursion_trees_student.ipynb
│
├── README.md
│
└── .gitignore
```

---

# Part 11: Open In VS Code

Open VS Code.

File → Open Folder

Select:

```text
build-interpreter-yourname
```

Open:

```text
workshop1/week1_symbols_recursion_trees_student.ipynb
```

Select Python kernel.

Run first cell.

Expected:

```text
Hello MiniLang!
```

---

# Part 12: First Commit

Open terminal inside VS Code.

Run:

```bash
git status
```

Then:

```bash
git add .

git commit -m "Workshop 1 setup complete"

git push
```

Refresh GitHub.

You should now see your notebook.

---

# Part 13: Weekly Workflow

Every week:

1. Complete notebook/code
2. Save work
3. Commit changes

```bash
git add .

git commit -m "Complete workshop X"

git push
```

---

# Troubleshooting

## python command not found

Windows:

```bash
py --version
```

Mac:

```bash
python3 --version
```

## git command not found

Reinstall Git and restart terminal.

## Notebook won't run

Install:

```bash
python3 -m pip install ipykernel
```

or

```bash
py -m pip install ipykernel
```

Restart VS Code.

---

# Need Help?

Do not spend hours fighting setup issues.

Bring screenshots to Workshop 1 and we will help.
