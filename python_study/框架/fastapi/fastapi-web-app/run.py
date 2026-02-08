#!/usr/bin/env python3
"""
Application runner script
"""
import subprocess
import sys


def run_server():
    """Run the FastAPI server"""
    print("Starting FastAPI server...")
    subprocess.run([
        "uvicorn", "app.main:app",
        "--host", "0.0.0.0",
        "--port", "8000",
        "--reload"
    ])


def run_tests():
    """Run tests"""
    print("Running tests...")
    result = subprocess.run(["pytest", "tests/", "-v"])
    return result.returncode


def run_migrations():
    """Run database migrations"""
    print("Running database migrations...")
    subprocess.run(["alembic", "upgrade", "head"])


def create_migration(message: str):
    """Create new migration"""
    print(f"Creating migration: {message}")
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", message])


def show_help():
    """Show help message"""
    print("""
FastAPI Web Application Management Script

Usage:
    python run.py [command]

Commands:
    server      - Start the development server
    test        - Run tests
    migrate     - Run database migrations
    makemigration <message> - Create new migration
    help        - Show this help message

Examples:
    python run.py server
    python run.py test
    python run.py migrate
    python run.py makemigration "Add new field"
    """)


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    if command == "server":
        run_server()
    elif command == "test":
        sys.exit(run_tests())
    elif command == "migrate":
        run_migrations()
    elif command == "makemigration":
        if len(sys.argv) < 3:
            print("Error: Migration message required")
            show_help()
            sys.exit(1)
        message = sys.argv[2]
        create_migration(message)
    elif command == "help":
        show_help()
    else:
        print(f"Error: Unknown command '{command}'")
        show_help()
        sys.exit(1)


if __name__ == "__main__":
    main()