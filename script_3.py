
# Create updated test runner

polished_runner = '''#!/usr/bin/env python3
"""
Test Runner for Consciousness Trilogy

Executes all test suites:
- Comprehensive tests (functional verification)
- Advanced tests (multi-methodology validation)
"""

import subprocess
import sys
import os


def run_script(script_path: str) -> int:
    """Run a test script and capture output.
    
    Args:
        script_path: Path to the test script
        
    Returns:
        Exit code from the script
    """
    print(f"\\n{'='*70}")
    print(f"Running {script_path}...")
    print('='*70)
    
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )
    
    if result.stdout:
        print(result.stdout)
    
    if result.stderr:
        print("STDERR:", result.stderr, file=sys.stderr)
    
    return result.returncode


def main() -> int:
    """Run all test suites."""
    # Ensure correct working directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("="*70)
    print("CONSCIOUSNESS TRILOGY - MASTER TEST RUNNER")
    print("="*70)
    
    # Run test suites
    exit_code1 = run_script("test_consciousness.py")
    exit_code2 = run_script("advanced_tests.py")
    
    # Summary
    print("\\n" + "="*70)
    print("FINAL SUMMARY")
    print("="*70)
    
    if exit_code1 == 0 and exit_code2 == 0:
        print("✓ ALL TEST SUITES PASSED")
        print("="*70)
        return 0
    else:
        print("✗ TEST SUITE FAILURE DETECTED")
        if exit_code1 != 0:
            print("  - Comprehensive tests failed")
        if exit_code2 != 0:
            print("  - Advanced tests failed")
        print("="*70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
'''

with open('run_tests.py', 'w', encoding='utf-8') as f:
    f.write(polished_runner)

print("✓ Created run_tests.py")
