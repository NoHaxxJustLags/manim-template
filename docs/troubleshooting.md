# Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### "manim command not found"
**Solution**: Make sure the virtual environment is activated
```bash
source .venv/bin/activate  # On Linux/Mac
.venv\Scripts\activate     # On Windows
```

#### "Module not found" errors
**Solution**: Reinstall dependencies
```bash
uv sync
```

### Rendering Problems

#### Scene not rendering
**Checklist**:
- Is your scene class inheriting from `Scene` or `ThreeDScene`?
- Is the class name spelled correctly in the command?
- Does your file have syntax errors?

**Test**: Run Python directly to check for errors
```bash
python -c "from scenes.yourfile import YourScene"
```

#### Video file not created
**Check**: The `media/` folder for output
- Videos: `media/videos/`
- Images: `media/images/`

**Tip**: Use `-p` flag to automatically preview
```bash
manim -ql -p scenes/yourfile.py YourScene
```

#### Rendering is too slow
**Solutions**:
- Use lower quality during development: `-ql` or `-qm`
- Reduce the number of objects in your scene
- Simplify complex mathematical expressions
- Use `--disable_caching` if caching causes issues

### Animation Issues

#### Objects not appearing
**Common causes**:
- Forgot to add `self.play()` or `self.add()`
- Objects positioned outside camera frame
- Z-index issues (objects behind others)

**Debug**: Add `self.add(obj)` to instantly show objects

#### Timing feels wrong
**Adjust**:
- Use `run_time` parameter: `self.play(Create(obj), run_time=2)`
- Add waits: `self.wait(1)`
- Use `rate_func` for custom timing curves

#### Text rendering issues
**Try**:
- Use simpler fonts
- Reduce font size
- Use `Text` instead of `TexText` for plain text
- Check LaTeX installation for math text

### 3D Scene Problems

#### Camera angle is wrong
**Fix**: Set camera orientation explicitly
```python
self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
```

#### 3D objects look flat
**Ensure**:
- Using `ThreeDScene` not `Scene`
- Camera orientation is set
- Lighting is appropriate

### Codespaces-Specific

#### Setup script failed
**Try**:
- Rebuild the container
- Check `.devcontainer/setup.sh` has correct permissions
- Look at logs in terminal for specific errors

#### Extensions not working
**Solution**: Reload the window
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P`)
- Type "Reload Window"
- Press Enter

#### Preview not showing
**Check**:
- Manim Sideview extension is installed
- File is saved before running
- Output path is correct in settings

## Getting Help

### Before Asking for Help
1. Check error messages carefully
2. Verify your code has no syntax errors
3. Try the simplest possible example
4. Search the Manim documentation

### Where to Get Help
- [Manim Documentation](https://docs.manim.community/)
- [GitHub Issues](https://github.com/ManimCommunity/manim/issues)
- [Community Discord](https://www.manim.community/discord/)
- [Reddit r/manim](https://www.reddit.com/r/manim/)

### Information to Include
When reporting issues:
- Manim version: `manim --version`
- Python version: `python --version`
- Operating system
- Full error message
- Minimal code example that reproduces the issue

## Performance Tips

### Faster Rendering
- Use `-ql` (low quality) during development
- Cache previous renders (default behavior)
- Close unnecessary applications
- Use simpler geometries when possible

### Memory Issues
- Limit objects in complex scenes
- Clear unused objects with `FadeOut` or `remove()`
- Render long videos in multiple scenes
- Restart kernel if memory accumulates

## Advanced Debugging

### Enable verbose output
```bash
manim -ql scenes/file.py Scene -v DEBUG
```

### Preview single frame
```bash
manim -ql -s scenes/file.py Scene
```

### Test without rendering
Import and instantiate your scene in Python to check for errors:
```python
from scenes.yourfile import YourScene
scene = YourScene()
```
