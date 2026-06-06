
# Workshop 1 Student Setup Guide
## Code To Execution: Build Your Own Interpreter

This course assumes no prior experience with interpreters, parsers, or compilers.

Before Workshop 1, please complete the steps below.

---

# Step 1: Install Python

Recommended: Python 3.10+

## Windows

Download Python from python.org.

IMPORTANT:
Check:

☑ Add Python to PATH

Verify:

```bash
python --version
```

or

```bash
py --version
```

## Mac

Verify:

```bash
python3 --version
```

---

# Step 2: Install VS Code

Install:

- VS Code
- Python extension
- Jupyter extension

---

# Step 3: Install Jupyter

Windows:

```bash
py -m pip install notebook ipykernel
```

Mac:

```bash
python3 -m pip install notebook ipykernel
```

---

# Step 4: Create Your Own GitHub Repository

For this fellowship, everyone will maintain their own repository.

Create a repository named:

```text
build-interpreter-yourname
```

Example:

```text
build-interpreter-john
```

Repository settings:

- README ✓
- Python .gitignore ✓
- Public or Private

---

# Step 5: Install Git

Verify:

```bash
git --version
```

---

# Step 6: Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

# Step 7: Clone YOUR Repository

Example:

```bash
git clone https://github.com/YOUR_USERNAME/build-interpreter-yourname.git

cd build-interpreter-yourname
```

---

# Step 8: Create Project Structure

Create:

```text
build-interpreter-yourname/
│
├── notebooks/
├── interpreter/
├── assignments/
├── notes/
└── README.md
```

---

# Step 9: Copy Workshop 1 Notebook

Download:

week1_symbols_recursion_trees_student.ipynb

Place it inside:

```text
notebooks/
```

---

# Step 10: Open Notebook

Open the repository folder in VS Code.

Open:

```text
notebooks/week1_symbols_recursion_trees_student.ipynb
```

Select a Python kernel.

Run the first cell.

---

# Step 11: First Commit

```bash
git add .

git commit -m "Complete setup"

git push
```

---

# Weekly Workflow

Each week:

```bash
git add .

git commit -m "Complete workshop 2"

git push
```

---

# Final Deliverable

Your repository should contain:

```text
notebooks/
interpreter/
assignments/
README.md
```

Including:

- Week 1 notebook
- Week 2 notebook
- Interpreter source code
- Final extension
- Final README

At the end of the fellowship, you will submit your GitHub repository link.
