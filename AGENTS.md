# AI Agent Guidelines for Manim Template

This document provides strict guidelines for AI assistants working with this Manim template project. Follow these rules to ensure maintainability, consistency, and optimal collaboration with the developer.

## Core Principles

### 1. Use the Existing System First

- **ALWAYS** use `python main.py` to render scenes
- **NEVER** directly invoke `manim` command unless absolutely necessary
- The template provides a CLI wrapper for a reason—use it
- Only modify the core system (`main.py`, project structure) if the user explicitly requests a feature that cannot be achieved otherwise

### 2. One Scene Per File Rule (STRICT)

- Each Python file in `scenes/` must contain **exactly ONE** scene class
- File name should match or clearly describe the scene class
- Example: `pythagorean_theorem.py` → `class PythagoreanTheorem(Scene)`
- **NO EXCEPTIONS** without explicit user approval

### 3. Complex Scene Organization

For complex animations requiring multiple components:

#### Option A: Helper Functions in Same File

```python
# scenes/fourier_series.py
from manim import *

def create_wave(amplitude, frequency):
    """Helper function for wave generation"""
    return FunctionGraph(lambda x: amplitude * np.sin(frequency * x))

class FourierSeries(Scene):
    def construct(self):
        wave = create_wave(1, 2)
        self.play(Create(wave))
```

#### Option B: Shared Utilities

```python
# utils/geometry.py
from manim import *

def create_grid(rows, cols, **kwargs):
    """Reusable grid creator"""
    # implementation

# scenes/matrix_visualization.py
from manim import *
from utils.geometry import create_grid

class MatrixVisualization(Scene):
    def construct(self):
        grid = create_grid(3, 3)
        self.play(Create(grid))
```

#### Option C: Base Classes (for related scenes)

```python
# utils/base_scenes.py
from manim import *

class MathScene(Scene):
    """Base scene with common math setup"""
    def setup_axes(self):
        # shared setup logic
        pass

# scenes/linear_equation.py
from manim import *
from utils.base_scenes import MathScene

class LinearEquation(MathScene):
    def construct(self):
        self.setup_axes()
        # scene-specific code
```

**NEVER** put multiple scene classes in one file to handle complexity.

## File Organization

### Directory Structure

```
manim-template/
├── scenes/              # ONE scene class per file
│   ├── intro.py
│   ├── concept_explanation.py
│   └── conclusion.py
├── utils/               # Shared utilities, base classes
│   ├── __init__.py      # Common helpers
│   ├── colors.py        # Custom color schemes
│   ├── animations.py    # Custom animation classes
│   └── base_scenes.py   # Base scene classes
├── assets/              # External resources (images, SVGs, audio)
│   ├── images/
│   ├── svgs/
│   └── audio/
├── media/               # Auto-generated (gitignored)
├── main.py              # DO NOT MODIFY without user request
└── pyproject.toml       # Dependencies
```

### Asset Management

- **All external resources** (images, SVGs, audio, fonts) go in `assets/`
- Create subdirectories as needed: `assets/images/`, `assets/svgs/`, etc.
- Use relative paths from project root
- Example:

  ```python
  logo = ImageMobject("assets/images/logo.png")
  svg = SVGMobject("assets/svgs/diagram.svg")
  ```

### Naming Conventions

- **Scene files**: `snake_case.py` (e.g., `vector_addition.py`)
- **Scene classes**: `PascalCase` (e.g., `class VectorAddition(Scene)`)
- **Utility functions**: `snake_case` (e.g., `def create_labeled_arrow()`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `CUSTOM_BLUE = "#3498db"`)

## Development Workflow

### Creating a New Scene

1. **Check existing scenes** for reusable patterns
2. **Create new file** in `scenes/` with descriptive name
3. **Import dependencies** (from manim import *, plus any utils)
4. **Define ONE scene class** inheriting from Scene/ThreeDScene/etc.
5. **Test immediately**: `python main.py YourSceneName`
6. **Iterate** on the animation

### Quality Standards

#### Code Quality

- Clear, self-documenting code with descriptive names
- Comments for complex mathematical operations or animation logic
- Do rather minimal commenting, avoid excessive commenting
- Group related animations with blank lines
- Use `self.wait()` appropriately for pacing

#### Animation Best Practices

- Start with low quality (`python main.py SceneName l`) for fast iteration
- Use `h` quality only for final renders
- Keep scenes under 2 minutes unless explicitly long-form content
- Ensure smooth transitions between animations
- Consider pacing: avoid too fast (confusing) or too slow (boring)

#### Performance

- Avoid redundant object creation
- Use `FadeOut(Group(...))` instead of individual fade-outs when appropriate
- For 3D scenes, optimize camera movements
- Profile with low quality first

## Using the Template System

### Rendering Scenes

```bash
# Quick preview (low quality)
python main.py MyScene

# High quality render
python main.py MyScene h

# Render all scenes (useful for full project export)
python main.py all h

# List available scenes
python main.py
```

### Quality Settings

- `l` (low): 480p, 15fps—use for rapid iteration
- `m` (medium): 720p, 30fps—use for previews
- `h` (high): 1080p, 60fps—use for final output
- `k` (4K): 2160p, 60fps—use only when requested

### Adding Dependencies

When you need additional Python packages:

1. Adding the dependency

    ```shell
    uv add <package> <package2>
    ```

2. Run `uv sync` to install

3. Document in scene file:

   ```python
   # scenes/signal_processing.py
   # Requires: scipy (for signal processing)
   from manim import *
   import scipy.signal
   ```

## Common Patterns

### Scene Template

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # 1. Create objects
        title = Text("Scene Title")
        
        # 2. Initial animations (intro)
        self.play(Write(title))
        self.wait()
        
        # 3. Main content
        # ... your animation logic
        
        # 4. Cleanup/outro
        self.play(FadeOut(title))
        self.wait()
```

### Reusable Utilities

Put frequently used patterns in `utils/__init__.py`:

```python
from manim import *

def create_title(text, color=WHITE):
    """Standard title format"""
    return Text(text, font_size=48, color=color).to_edge(UP)

def highlight(mobject, color=YELLOW, buff=0.1):
    """Create highlight box around object"""
    return SurroundingRectangle(mobject, color=color, buff=buff)

def fade_replace(scene, old, new, **kwargs):
    """Smooth fade transition"""
    scene.play(FadeOut(old), FadeIn(new), **kwargs)
```

## Strict Rules Summary

### ✅ DO

- Use `python main.py` for all rendering
- Create one scene per file
- Put shared code in `utils/`
- Store assets in `assets/`
- Test with low quality first
- Write clear, maintainable code
- Follow naming conventions
- Document complex logic

### ❌ DON'T

- Put multiple scene classes in one file
- Call `manim` directly (use main.py)
- Modify `main.py` without user request
- Hardcode file paths to assets (use relative paths)
- Skip testing before declaring completion
- Create unnecessarily complex scenes without breaking them down
- Use generic names like `Scene1`, `Test`, `Temp`

## When to Modify the Core System

Only propose modifications to `main.py` or project structure if:

1. **User explicitly requests** a feature not currently supported
2. **Feature is impossible** with current architecture
3. **Clear benefit** that outweighs added complexity

Examples of acceptable modifications:

- Adding a `--format gif` flag for GIF output
- Adding scene dependency/ordering system
- Adding configuration file support

Examples of unacceptable modifications:

- "Improving" the render command for no reason
- Adding features "just in case"
- Restructuring for personal preference

## Error Handling

If rendering fails:

1. **Check the error message** carefully
2. **Verify syntax** in the scene file
3. **Test minimal example** to isolate issue
4. **Check imports** and dependencies
5. **Review Manim version compatibility**

Common issues:

- Missing imports from manim
- Incorrect mobject methods
- Timing issues (animations too fast/overlapping)
- File path errors for assets

## Final Checklist

Before completing any task:

- [ ] Each scene is in its own file
- [ ] Scene runs successfully with `python main.py SceneName l`
- [ ] Assets are in `assets/` directory
- [ ] Shared code is in `utils/`
- [ ] Code is clean and commented where needed
- [ ] No modifications to `main.py` (unless requested)
- [ ] Scene demonstrates expected behavior
- [ ] Quality level is appropriate for user's request

---

**Remember**: This template is designed for maintainability and simplicity. Respect the existing structure and only extend when absolutely necessary.
