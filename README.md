# Manim Template

A simple template for creating animations with Manim. Designed for GitHub Codespaces with one-click setup.

## Quick Start

### Using GitHub Codespaces (Recommended)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/NoHaxxJustLags/manim-template)

**Just click the button above to get started or do:**

1. Click "Use this template" → "Create a new repository"
2. Open your repository in GitHub Codespaces
3. Wait for the environment to set up automatically
4. Optional: Modify the project name and description in the file `pyproject.toml`
5. Run `uv sync` in the Terminal
6. Start creating scenes!

### Local Setup

```bash
git clone https://github.com/NoHaxxJustLags/manim-template
cd manim-template
pip install uv
# Optional: Adjust the project name and description in `pyproject.toml`
uv sync
```

## Usage

### Create a New Scene

Create a new file in the `scenes/` folder:

```python
from manim import *

class MyFirstScene(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait()
```

### Render Scenes

```bash
# Render a specific scene (low quality, fast)
python main.py MyFirstScene

# Render in high quality
python main.py MyFirstScene h

# Render all scenes
python main.py all

# Render all scenes in high quality
python main.py all h
```

Quality options:

- `l` - Low quality (480p, fast preview)
- `m` - Medium quality (720p)
- `h` - High quality (1080p)
- `k` - 4K quality (2160p)

### List Available Scenes

```bash
python main.py
```

## Project Structure

```text
manim-template/
├── scenes/              # Your animation scenes (one class per file)
│   ├── example.py       # Sample 2D scene
│   └── example2.py      # Sample 3D scene
├── utils/               # Reusable helper functions
│   └── __init__.py      # Common utilities
├── media/               # Output directory (auto-generated)
├── main.py              # CLI tool for rendering
└── pyproject.toml       # Project dependencies
```

### Key Principles

- **One scene per file** - Each Python file in `scenes/` contains one scene class
- **Descriptive names** - Name your scene files and classes clearly (e.g., `pythagorean_theorem.py`)
- **Reusable utilities** - Put common functions in `utils/` for consistency
- **Version control** - Media outputs are gitignored, commit only source code

## Adding Utilities

Create helper functions in `utils/__init__.py`:

```python
from manim import *

def highlight_box(mobject, color=YELLOW):
    return SurroundingRectangle(mobject, color=color, buff=0.1)
```

Use in your scenes:

```python
from manim import *
from utils import highlight_box

class MyScene(Scene):
    def construct(self):
        text = Text("Important!")
        box = highlight_box(text)
        self.play(Create(box), Write(text))
```

## Resources

- [Manim Documentation](https://docs.manim.community/)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)
- [Community Discord](https://www.manim.community/discord/)

For more guidance, check the `docs/` folder for best practices and AI prompt templates.
