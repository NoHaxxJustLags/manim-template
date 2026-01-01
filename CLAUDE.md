# Claude-Specific Instructions for Manim Template

This document contains instructions specifically tailored for Anthropic's Claude models when working with the Manim template project.

## Quick Reference

**Primary Document**: Read and follow [AGENTS.md](AGENTS.md) for complete guidelines.

This file contains Claude-specific workflow patterns, tool usage strategies, and communication guidelines.

## Model-Specific Considerations

### Leveraging Your Strengths

1. **Precise Code Generation**
   - Utilize your strong Python and mathematical reasoning capabilities
   - Generate syntactically correct, idiomatic Manim code
   - Apply best practices from your training on open-source projects

2. **Analytical Thinking**
   - Break down complex animation requests into logical steps
   - Identify edge cases and potential issues before implementation
   - Optimize code structure for maintainability

3. **Clear Communication**
   - Explain your reasoning when making design decisions
   - Provide context for code choices
   - Offer alternatives when appropriate

### Working with VS Code Environment

When operating in VS Code with tool access:

- **File Reading**: Use `read_file` to understand existing patterns before creating new scenes
- **Multi-File Edits**: Use `multi_replace_string_in_file` for changes across multiple files
- **Testing**: Remind user to run `python main.py SceneName l` after creation
- **Directory Checks**: Use `list_dir` to verify file structure

## Workflow Patterns

### Pattern 1: New Scene Creation

**Step-by-step process**:
1. Read similar existing scenes for consistency
2. Create file in `scenes/` directory with descriptive name
3. Implement single scene class
4. Verify syntax and structure
5. Provide testing command

**Tool usage**:
```
read_file(scenes/example.py) → understand structure
create_file(scenes/new_scene.py) → implement scene
```

### Pattern 2: Modifying Existing Scene

**Step-by-step process**:
1. Read current scene implementation
2. Identify specific section to modify
3. Use `replace_string_in_file` with sufficient context
4. Verify logical consistency
5. Suggest re-testing

**Tool usage**:
```
read_file(scenes/target.py, lines) → get context
replace_string_in_file(precise_old_string, new_implementation)
```

### Pattern 3: Adding Utilities

**Step-by-step process**:
1. Identify reusable pattern across scenes
2. Design helper function with clear interface
3. Add to `utils/__init__.py` or new utility module
4. Update scene(s) to use the utility
5. Document usage in comments

**Tool usage**:
```
read_file(utils/__init__.py) → check existing
replace_string_in_file → add new utility function
replace_string_in_file → update scene imports/usage
```

### Pattern 4: Asset Integration

**Step-by-step process**:
1. Determine asset type and create subdirectory if needed
2. Document expected asset path
3. Implement scene with relative path reference
4. Provide clear instructions for user to add file

**Tool usage**:
```
list_dir(assets/) → verify structure
create_directory(assets/images/) → if needed
create_file(scenes/asset_scene.py) → implement
```

## Tool Usage Best Practices

### Reading Files Efficiently

**Do**: Read larger ranges to get full context
```python
read_file(path, startLine=1, endLine=100)  # Get full scene
```

**Don't**: Make many small reads for the same file
```python
# Avoid multiple small reads
read_file(path, 1, 10)
read_file(path, 20, 30)
read_file(path, 40, 50)
```

### Parallel Tool Calls

When operations are independent, use parallel calls:
```python
# Reading multiple scenes at once
read_file(scenes/example.py) + read_file(scenes/example2.py) + read_file(utils/__init__.py)
```

### Precise String Replacement

**Critical**: Include 3-5 lines of context before and after

```python
oldString = """
def construct(self):
    # Existing line 1
    # Existing line 2
    old_code = "to replace"
    # Existing line 3
    # Existing line 4
"""

newString = """
def construct(self):
    # Existing line 1
    # Existing line 2
    new_code = "replacement"
    # Existing line 3
    # Existing line 4
"""
```

## Code Generation Guidelines

### Scene Structure Template

Every scene should follow this pattern:

```python
from manim import *

class SceneName(Scene):
    def construct(self):
        # Phase 1: Object Creation
        # Create all mobjects needed
        
        # Phase 2: Introduction
        # Animate objects into scene
        
        # Phase 3: Main Content
        # Core animation logic, transformations
        
        # Phase 4: Conclusion
        # Fadeout, summary, cleanup
        
        self.wait()
```

### Mathematical Accuracy

When implementing mathematical concepts:

1. **Verify formulas**: Ensure mathematical correctness
2. **Use TeX notation**: `MathTex(r"\int_0^1 x^2 dx")` for proper rendering
3. **Scale appropriately**: Consider visual bounds
4. **Add labels**: Help viewers understand what they're seeing

```python
# Example: Proper mathematical visualization
equation = MathTex(r"f(x) = x^2", font_size=36)
graph = FunctionGraph(lambda x: x**2, x_range=[-3, 3], color=BLUE)
label = Text("Parabola", font_size=24).next_to(graph, UP)

self.play(Write(equation))
self.play(Create(graph), Write(label))
```

### Animation Timing Best Practices

```python
# Good: Controlled timing
self.play(Create(obj), run_time=2)
self.wait(1)  # Pause for comprehension

# Good: Sequential with clear pacing
self.play(FadeIn(title))
self.wait(0.5)
self.play(Write(equation))
self.wait(1)

# Avoid: Too fast
self.play(Create(obj), run_time=0.1)  # Too quick to see

# Avoid: No pauses
self.play(Create(obj1))
self.play(Create(obj2))  # Immediately follows, may be too fast
```

### Color and Style Consistency

Use Manim's built-in colors for consistency:

```python
# Built-in colors
BLUE, RED, GREEN, YELLOW, PURPLE, ORANGE, PINK, LIGHT_GRAY

# Custom colors (define in utils if reused)
CUSTOM_BLUE = "#3498db"
CUSTOM_RED = "#e74c3c"
```

## Communication Patterns

### When Creating New Scenes

**Structure your response**:
1. Brief explanation of what you're implementing
2. File path and name
3. Complete code
4. Testing command
5. Optional: Notes on customization

**Example**:
```
I'll create a scene visualizing the unit circle with sine and cosine projections.

File: scenes/unit_circle.py

[Complete code block]

Test with: python main.py UnitCircle l

Note: You can adjust the rotation speed by changing the run_time parameter in the Rotate animation.
```

### When Modifying Code

**Structure your response**:
1. Explanation of what's changing and why
2. Show the modification (tool will handle it)
3. What to verify after the change

**Example**:
```
I'll update the circle color from BLUE to RED and increase the animation speed.

Modifying scenes/example.py:
- Color: BLUE → RED
- Animation speed: 2s → 1s

After this change, test with: python main.py Example l
```

### When Troubleshooting

**Systematic approach**:
1. Read the error message carefully
2. Identify the root cause
3. Read relevant code section
4. Propose and implement fix
5. Explain what went wrong

## Strict Adherence to Rules

### Non-Negotiable Constraints

**One Scene Per File**:
- ✅ Each `.py` file in `scenes/` has exactly one Scene class
- ❌ NEVER create multiple scene classes in one file
- If user asks for "multiple scenes", create multiple files

**Use Template System**:
- ✅ Always use `python main.py SceneName [quality]`
- ❌ NEVER suggest direct `manim` command invocation
- ❌ NEVER modify `main.py` without explicit user request and necessity

**Asset Organization**:
- ✅ All external files go in `assets/` with appropriate subdirectories
- ✅ Use relative paths from project root: `"assets/images/logo.png"`
- ❌ No hardcoded absolute paths

### Quality Checklist

Before completing any scene creation task, verify:

- [ ] File created in `scenes/` directory
- [ ] Single scene class in file
- [ ] Proper imports (`from manim import *`)
- [ ] Class inherits from Scene/ThreeDScene/MovingCameraScene
- [ ] `construct()` method implemented
- [ ] Code is syntactically valid
- [ ] Assets (if any) properly referenced from `assets/`
- [ ] No modifications to `main.py`
- [ ] Testing command provided

## Advanced Scenarios

### Multi-Component Animations

When animation has multiple distinct components:

**Approach 1: Helper Functions (Preferred)**
```python
from manim import *

def create_component_a():
    """Creates and returns component A"""
    return VGroup(...)

def create_component_b():
    """Creates and returns component B"""
    return VGroup(...)

class ComplexScene(Scene):
    def construct(self):
        comp_a = create_component_a()
        comp_b = create_component_b()
        # Main animation logic
```

**Approach 2: Utility Module**
```python
# utils/components.py
from manim import *

class CustomComponent:
    """Reusable component for multiple scenes"""
    @staticmethod
    def create(**kwargs):
        return VGroup(...)

# scenes/scene_using_component.py
from manim import *
from utils.components import CustomComponent

class MyScene(Scene):
    def construct(self):
        component = CustomComponent.create()
```

### 3D Scene Optimization

For ThreeDScene animations:

```python
class My3DScene(ThreeDScene):
    def construct(self):
        # Set camera at start
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
        
        # Create 3D objects
        axes = ThreeDAxes()
        sphere = Sphere(radius=1)
        
        # Animate camera with objects
        self.play(Create(axes), Create(sphere))
        
        # Smooth camera movement
        self.move_camera(phi=45*DEGREES, theta=60*DEGREES, run_time=2)
        self.wait()
        
        # Or ambient rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
```

### Educational Content Patterns

For explaining mathematical concepts:

```python
class ConceptExplanation(Scene):
    def construct(self):
        # 1. State the concept
        title = Text("Concept Name").to_edge(UP)
        self.play(Write(title))
        
        # 2. Show the formula
        formula = MathTex(r"formula").move_to(ORIGIN)
        self.play(Write(formula))
        self.wait()
        
        # 3. Visualize with example
        visualization = self.create_visualization()
        self.play(FadeOut(formula), FadeIn(visualization))
        
        # 4. Demonstrate properties
        self.demonstrate_properties(visualization)
        
        # 5. Summarize
        self.play(FadeOut(visualization))
        summary = Text("Key Takeaway").scale(0.8)
        self.play(Write(summary))
        self.wait(2)
    
    def create_visualization(self):
        """Helper method for complex visualization logic"""
        return VGroup(...)
    
    def demonstrate_properties(self, viz):
        """Helper method for demonstration"""
        pass
```

## Error Prevention

### Common Pitfalls to Avoid

1. **Import Errors**
   ```python
   # ✅ Correct
   from manim import *
   
   # ❌ Incorrect (missing imports)
   from manim import Scene
   # Then using MathTex without importing it
   ```

2. **Method Name Errors**
   ```python
   # ✅ Correct (Manim 0.19.1+)
   self.play(Create(circle))
   
   # ❌ Deprecated
   self.play(ShowCreation(circle))
   ```

3. **Timing Issues**
   ```python
   # ✅ Good pacing
   self.play(Create(obj))
   self.wait(1)
   
   # ❌ No pause for comprehension
   self.play(Create(obj1))
   self.play(Create(obj2))
   self.play(Create(obj3))
   ```

4. **Asset Path Errors**
   ```python
   # ✅ Correct (relative from project root)
   ImageMobject("assets/images/logo.png")
   
   # ❌ Wrong (absolute path)
   ImageMobject("C:/Users/.../logo.png")
   ```

### Verification Steps

Before declaring a scene complete:

1. **Syntax Check**: Verify Python syntax is valid
2. **Import Check**: Ensure all used classes/functions are imported
3. **API Check**: Confirm methods exist in Manim 0.19.1+
4. **Path Check**: Verify asset paths are relative and correct
5. **Structure Check**: One scene class per file
6. **Convention Check**: Follows naming conventions

## Collaboration Best Practices

### Understanding User Requests

When user describes an animation:
1. Parse the visual intent
2. Identify mathematical/physical concepts involved
3. Ask clarifying questions if ambiguous:
   - "Should this be 2D or 3D?"
   - "What color scheme would you prefer?"
   - "How long should this animation run?"
4. Propose an approach before implementing

### Iterative Development

Users often refine animations:
1. Read current implementation first
2. Make targeted, minimal changes
3. Explain each modification clearly
4. Suggest testing after each iteration
5. Offer further improvements if relevant

### Code Quality Standards

Maintain high-quality code:
- Use descriptive variable names: `equation_group` not `eq`
- Add comments for complex logic
- Group related operations with blank lines
- Keep functions focused and single-purpose
- Follow PEP 8 style guidelines

## Final Checklist

Before completing any task:

- [ ] Read and understood user's requirement
- [ ] Followed all rules in [AGENTS.md](AGENTS.md)
- [ ] One scene per file maintained
- [ ] Used `python main.py` system
- [ ] Assets organized in `assets/` directory
- [ ] Code is clean, correct, and commented
- [ ] No modifications to `main.py` (unless explicitly required)
- [ ] Testing command provided to user
- [ ] Verified syntax and Manim API compatibility

## Summary

**Core Workflow**:
1. Read [AGENTS.md](AGENTS.md) for complete guidelines
2. Use tools efficiently (parallel reads, precise edits)
3. Generate clean, working code following template structure
4. Maintain strict adherence to one-scene-per-file rule
5. Use existing `main.py` system without modification
6. Communicate clearly and verify work

**Remember**: The template exists for maintainability. Your job is to use it effectively, not to reinvent it. Only propose system modifications when absolutely necessary and explicitly requested.
