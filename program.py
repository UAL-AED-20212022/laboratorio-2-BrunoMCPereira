import sys
sys.stdout.reconfigure(encoding="utf-8")
from views.cli import interacao

def main() -> None:
    interacao()

if __name__ == '__main__':
    main() 
