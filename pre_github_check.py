from pathlib import Path
import ast
import sys

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "FaceSecurity/main.py",
    "FaceSecurity/enroll.py",
    "FaceSecurity/camera/camera_manager.py",
    "FaceSecurity/detection/face_detector.py",
    "FaceSecurity/recognition/face_encoder.py",
    "FaceSecurity/recognition/face_matcher.py",
    "FaceSecurity/database/face_database.py",
    "FaceSecurity/config/settings.py",
    "requirements.txt",
]

def main():
    errors = []

    for path in ROOT.rglob("*.py"):
        if ".git" in path.parts or "venv" in path.parts or "__pycache__" in path.parts:
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    missing = [p for p in REQUIRED_FILES if not (ROOT / p).exists()]

    print("FACE SECURITY AI - PRE GITHUB CHECK")
    print("=" * 50)

    if errors:
        print("Syntax errors:")
        for error in errors:
            print(" -", error)

    if missing:
        print("Missing required files:")
        for path in missing:
            print(" -", path)

    if errors or missing:
        print("\nSTATUS: REVIEW REQUIRED")
        sys.exit(1)

    print("\nSTATUS: READY FOR GITHUB")

if __name__ == "__main__":
    main()
