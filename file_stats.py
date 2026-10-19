"""Count files by extension in the current directory."""
from collections import Counter
from pathlib import Path


def count_extensions(root: Path) -> Counter:
    counts = Counter()
    for path in root.rglob("*"):
        if path.is_file():
            ext = path.suffix.lower() or "(no extension)"
            counts[ext] += 1
    return counts


def main() -> None:
    counts = count_extensions(Path("."))
    for ext, n in counts.most_common():
        print(f"{ext:<15} {n}")
    print(f"total: {sum(counts.values())} files")


if __name__ == "__main__":
    main()
