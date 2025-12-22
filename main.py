import re
import subprocess
import sys
from pathlib import Path


def get_scene_files():
    scenes_dir = Path(__file__).parent / "scenes"
    return [f for f in scenes_dir.glob("*.py") if f.name != "__init__.py"]


def get_scene_classes(scene_file: Path) -> list[str]:
    content = scene_file.read_text()
    return re.findall(r"class (\w+)\([^)]*Scene[^)]*\):", content)


def render_scene(scene_file: Path, scene_name: str, quality: str = "l"):
    cmd = ["manim", "-q" + quality, str(scene_file), scene_name]
    subprocess.run(cmd, check=True)


def render_all(quality: str = "l"):
    for scene_file in get_scene_files():
        for scene_class in get_scene_classes(scene_file):
            print(f"Rendering {scene_class} from {scene_file.name}")
            render_scene(scene_file, scene_class, quality)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <SceneName|all> [quality]")
        print("\nAvailable scenes:")
        for f in get_scene_files():
            for scene_class in get_scene_classes(f):
                print(f"  - {scene_class} ({f.name})")
        sys.exit(1)

    scene_name = sys.argv[1]
    quality = sys.argv[2] if len(sys.argv) > 2 else "l"

    if scene_name == "all":
        render_all(quality)
        return

    for scene_file in get_scene_files():
        if scene_name in get_scene_classes(scene_file):
            render_scene(scene_file, scene_name, quality)
            return

    print(f"Scene '{scene_name}' not found")
    sys.exit(1)


if __name__ == "__main__":
    main()
