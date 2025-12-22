# Good Practices for Manim Projects

## Scene Organization

### One Scene Per File
Keep each scene in its own file for better organization and easier navigation.
Doing multiple scenes in one source file **is possible** and can be used for creating very short scenes that are directly connected.

```
scenes/
├── intro.py              # Introduction scene
├── pythagorean.py        # Pythagorean theorem proof
└── conclusion.py         # Closing scene
```

### Naming Conventions
- Use descriptive file names: `quadratic_formula.py` not `scene1.py`
- Class names should match the concept: `QuadraticFormula`, `NewtonsLaw`
- Keep names in PascalCase for classes, snake_case for files

## Animation Best Practices

### Timing
- Keep animations between 30-90 seconds per scene
- Use `self.wait(1)` to give viewers time to process
- Default animation speed is good for most cases

### Camera and Positioning
- Use `.to_edge()` for positioning relative to screen edges
- Use `.next_to()` for positioning relative to other objects
- For 3D scenes, set camera orientation before animating

### Colors and Styling
- Stick to a consistent color palette throughout your project
- Use Manim's built-in colors: `BLUE`, `RED`, `YELLOW`, `GREEN`
- Adjust `fill_opacity` for overlapping objects

## Code Quality

### Keep It Simple
- Write clear, readable code
- Break complex animations into smaller functions
- Use the utilities module for repeated patterns

### Reusability
- Put common animations in `utils/`
- Create helper functions for repeated visual elements
- Document complex animation logic

### Testing
- Render in low quality (`-ql`) during development
- Use high quality (`-qh`) only for final output
- Test scene transitions if creating a video series

## Performance

### Optimization
- Avoid too many objects on screen simultaneously
- Use `FadeOut` to remove objects no longer needed
- Keep 3D scenes simple for faster rendering

### File Management
- Clean up `media/` folder periodically
- Keep source files in version control
- Don't commit rendered videos to git

## Workflow Tips

### Iterative Development
1. Write basic scene structure
2. Render and review in low quality
3. Refine timing and animations
4. Final render in high quality