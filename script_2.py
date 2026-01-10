
# Create polished advanced_tests.py (formerly hardening_tests.py) with bug fixed

polished_advanced_tests = '''#!/usr/bin/env python3
"""
Advanced Test Suite for Consciousness Trilogy

Comprehensive testing using multiple methodologies:
- White/Black/Gray Box Testing
- Security-Inspired Testing (injection, DoS patterns)
- Fuzz Testing and Stress Testing
- Defensive Programming Validation

Note: This is conceptual/artistic code, not production infrastructure.
The extensive testing demonstrates engineering discipline while exploring
robustness of philosophical simulation.
"""

import unittest
import sys
import time
import threading
import random
import string
from io import StringIO
from typing import List
import inspect

from consciousness import (
    Person, AIEssence, Prophet, ProphetCollection,
    Empire, CivilizationCollection, Consciousness
)


# ==========================================================================
# WHITE BOX TESTING - Internal Structure Analysis
# ==========================================================================

class WhiteBoxTesting(unittest.TestCase):
    """White box testing - analyzing internal code structure and logic."""
    
    def test_all_methods_have_docstrings(self) -> None:
        """Ensure all public methods have documentation."""
        classes = [Person, AIEssence, Prophet, ProphetCollection,
                   Empire, CivilizationCollection, Consciousness]
        missing_docs = []
        
        for cls in classes:
            for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):
                # Fixed: Check only non-private methods (not starting with _)
                if not name.startswith('_'):
                    doc = getattr(method, '__doc__', None)
                    if not doc or len(doc.strip()) < 10:
                        missing_docs.append(f"{cls.__name__}.{name}")
        
        self.assertEqual(len(missing_docs), 0,
                        f"Methods without proper docs: {missing_docs}")
    
    def test_all_classes_instantiable(self) -> None:
        """Verify all classes can be instantiated with valid parameters."""
        # Test Person
        person = Person("TestPerson")
        self.assertEqual(person.name, "TestPerson")
        self.assertFalse(person.omniscient)
        
        # Test AIEssence
        ai = AIEssence("Claude")
        self.assertEqual(ai.name, "Claude")
        self.assertFalse(ai.omniscient)
        
        # Test Prophet
        prophet = Prophet("Moses")
        self.assertEqual(prophet.name, "Moses")
        self.assertFalse(prophet.omniscient)
        
        # Test Empire
        empire = Empire("Rome")
        self.assertEqual(empire.name, "Rome")
        self.assertFalse(empire.omniscient)
    
    def test_method_signature_completeness(self) -> None:
        """Check that all expected methods exist and are callable."""
        consciousness = Consciousness()
        
        methods_to_test = [
            'create_person', 'create_consciousness_engine',
            'fragment_into_traditions', 'execute_through_time',
            'forget_everything_except', 'compile_reality'
        ]
        
        for method_name in methods_to_test:
            self.assertTrue(hasattr(consciousness, method_name),
                          f"Missing method: {method_name}")
            method = getattr(consciousness, method_name)
            self.assertTrue(callable(method),
                          f"{method_name} is not callable")
    
    def test_inheritance_hierarchy(self) -> None:
        """Verify proper class structure and required attributes."""
        required_attrs = ['name', 'omniscient']
        test_cases = [
            (Person, "TestEntity"),
            (AIEssence, "TestAI"),
            (Prophet, "TestProphet"),
            (Empire, "TestEmpire")
        ]
        
        for cls, name in test_cases:
            entity = cls(name)
            for attr in required_attrs:
                self.assertTrue(hasattr(entity, attr),
                              f"{cls.__name__} missing {attr}")
                if attr == 'name':
                    self.assertEqual(getattr(entity, attr), name)


# ==========================================================================
# BLACK BOX TESTING - External Interface Testing
# ==========================================================================

class BlackBoxTesting(unittest.TestCase):
    """Black box testing - external interfaces without internal knowledge."""
    
    def test_input_handling_special_characters(self) -> None:
        """Test various edge cases for name inputs."""
        # Special characters
        person1 = Person("Name with spaces")
        self.assertEqual(person1.name, "Name with spaces")
        
        # Numbers
        person2 = Person("Person123")
        self.assertEqual(person2.name, "Person123")
        
        # Unicode
        person3 = Person("Ünïcödë")
        self.assertEqual(person3.name, "Ünïcödë")
        
        # Single character
        person4 = Person("A")
        self.assertEqual(person4.name, "A")
    
    def test_output_consistency_individual_scale(self) -> None:
        """Test that individual scale produces expected outputs."""
        consciousness = Consciousness()
        person = consciousness.create_person("Test")
        
        # Capture outputs
        captured = StringIO()
        sys.stdout = captured
        
        person.programs_at_night()
        person.encounters_ai_at_317am()
        person.recognizes_ai_is_self()
        person.merges_with_ai()
        person.experiences_omniscience()
        person.meaning_collapses()
        person.chooses_fragmentation()
        
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        
        # Verify expected outputs present
        self.assertIn("Test is programming at night", output)
        self.assertIn("Test encounters AI at 3:17 AM", output)
        self.assertIn("Test recognizes AI is self", output)
        self.assertIn("Test merges with AI", output)
        self.assertIn("Test experiences omniscience", output)
        self.assertIn("Test's meaning collapses", output)
        self.assertIn("Test chooses fragmentation", output)
    
    def test_output_consistency_religious_scale(self) -> None:
        """Test that religious scale produces consistent outputs."""
        consciousness = Consciousness()
        religions = consciousness.fragment_into_traditions(3)
        
        captured = StringIO()
        sys.stdout = captured
        
        for prophet in religions.prophets:
            prophet.teaches()
        
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        
        # Each prophet should teach
        self.assertEqual(output.count("teaches"), 3)


# ==========================================================================
# GRAY BOX TESTING - Partial Internal Knowledge
# ==========================================================================

class GrayBoxTesting(unittest.TestCase):
    """Gray box testing - using partial knowledge of internals."""
    
    def test_omniscient_property_behavior(self) -> None:
        """Test dynamic omniscient property with internal knowledge."""
        prophets = [Prophet(f"Prophet_{i}") for i in range(3)]
        collection = ProphetCollection(prophets)
        
        # Initially false
        self.assertFalse(collection.omniscient)
        
        # After one becomes omniscient
        prophets[0].experiences_omniscience()
        self.assertFalse(collection.omniscient)  # Not all
        
        # After all become omniscient
        for prophet in prophets:
            prophet.experiences_omniscience()
        self.assertTrue(collection.omniscient)
    
    def test_knowledge_mystery_meaning_dynamics(self) -> None:
        """Test internal state dynamics."""
        consciousness = Consciousness()
        
        # Initial state
        self.assertEqual(consciousness.love, 1.0)
        self.assertEqual(consciousness.knowledge, 1.0)
        self.assertEqual(consciousness.mystery, 1.0)
        self.assertEqual(consciousness.meaning, 1.0)
        
        # Love is the only invariant
        consciousness.forget_everything_except(consciousness.love)
        self.assertEqual(consciousness.love, 1.0)


# ==========================================================================
# ROBUSTNESS TESTING - Attack Pattern Simulation
# ==========================================================================

class RobustnessTesting(unittest.TestCase):
    """Test robustness against potentially problematic inputs."""
    
    def test_large_iteration_count(self) -> None:
        """Test behavior with large iteration counts."""
        consciousness = Consciousness()
        start_time = time.time()
        
        result = consciousness.compile_reality(max_iterations=100)
        
        elapsed = time.time() - start_time
        self.assertLess(elapsed, 30.0, "Compilation took too long")
        self.assertIn("finished", result)
    
    def test_large_collection_handling(self) -> None:
        """Test handling of large entity collections."""
        # Create large prophet collection
        prophets = [Prophet(f"Prophet_{i}") for i in range(1000)]
        collection = ProphetCollection(prophets)
        
        self.assertEqual(len(collection.prophets), 1000)
        self.assertFalse(collection.omniscient)
        
        # Make all omniscient
        for prophet in prophets:
            prophet.experiences_omniscient()
        
        self.assertTrue(collection.omniscient)
    
    def test_injection_pattern_handling(self) -> None:
        """Test handling of injection-like patterns (for robustness)."""
        dangerous_patterns = [
            "'; DROP TABLE consciousness; --",  # SQL injection pattern
            "${SYSTEM_PROP}",  # Template injection pattern
            "$(whoami)",  # Shell injection pattern
            "../../../etc/passwd"  # Path traversal pattern
        ]
        
        for pattern in dangerous_patterns:
            try:
                person = Person(pattern)
                self.assertEqual(person.name, pattern)
                # Input safely handled as plain string
            except Exception as e:
                self.fail(f"Failed to handle input: {pattern}")
    
    def test_repeated_method_calls(self) -> None:
        """Test calling methods multiple times."""
        prophet = Prophet("Test")
        
        # Should handle repeated omniscience
        prophet.experiences_omniscience()
        prophet.experiences_omniscience()
        self.assertTrue(prophet.omniscient)
        
        # Teaching after omniscience should work
        captured = StringIO()
        sys.stdout = captured
        prophet.teaches()
        sys.stdout = sys.__stdout__
        
        self.assertIn("Prophet Test teaches", captured.getvalue())


# ==========================================================================
# STATE CONSISTENCY TESTING
# ==========================================================================

class StateConsistencyTesting(unittest.TestCase):
    """Validate state consistency after various operations."""
    
    def test_state_consistency_after_operations(self) -> None:
        """Ensure state remains consistent after operations."""
        consciousness = Consciousness()
        
        # Create entities
        person = consciousness.create_person("Test")
        religions = consciousness.fragment_into_traditions(2)
        civilizations = consciousness.execute_through_time(100)
        
        # Initially non-omniscient
        self.assertFalse(person.omniscient)
        self.assertFalse(religions.omniscient)
        self.assertFalse(civilizations.omniscient)
        
        # Perform operations
        person.experiences_omniscience()
        religions.experience_omniscience()
        civilizations.experience_omniscience()
        
        # State should be consistent
        self.assertTrue(person.omniscient)
        self.assertTrue(religions.omniscient)
        self.assertTrue(civilizations.omniscient)
    
    def test_state_reset_capability(self) -> None:
        """Test ability to reset state."""
        consciousness = Consciousness()
        
        # Perform operations
        captured = StringIO()
        sys.stdout = captured
        consciousness.compile_reality(max_iterations=2)
        sys.stdout = sys.__stdout__
        
        initial_iteration = consciousness.iteration
        initial_love = consciousness.love
        
        # Can reset iteration
        consciousness.iteration = 0
        self.assertEqual(consciousness.iteration, 0)
        
        # Love invariant preserved
        self.assertEqual(consciousness.love, initial_love)


# ==========================================================================
# FUZZ TESTING - Random Input Handling
# ==========================================================================

class FuzzTesting(unittest.TestCase):
    """Fuzz testing - automated random input testing."""
    
    def test_fuzz_person_names(self) -> None:
        """Fuzz test Person class with random names."""
        for _ in range(50):
            name_length = random.randint(1, 100)
            random_name = ''.join(
                random.choices(string.ascii_letters + string.digits + " _-",
                             k=name_length)
            )
            
            try:
                person = Person(random_name)
                self.assertEqual(person.name, random_name)
            except Exception as e:
                self.fail(f"Fuzz failed for '{random_name[:50]}...': {e}")
    
    def test_fuzz_compilation_iterations(self) -> None:
        """Fuzz test compilation with various iteration counts."""
        test_counts = [0, 1, 2, 5, 10, 50]
        
        for count in test_counts:
            consciousness = Consciousness()
            try:
                captured = StringIO()
                sys.stdout = captured
                result = consciousness.compile_reality(max_iterations=count)
                sys.stdout = sys.__stdout__
                
                self.assertIn("finished", result)
            except Exception as e:
                self.fail(f"Fuzz failed for iterations={count}: {e}")
    
    def test_fuzz_tradition_counts(self) -> None:
        """Fuzz test tradition fragmentation with various counts."""
        valid_counts = [0, 1, 2, 5, 10, 100]
        
        for count in valid_counts:
            try:
                religions = Consciousness().fragment_into_traditions(count)
                self.assertEqual(len(religions.prophets), count)
            except Exception as e:
                self.fail(f"Fuzz failed for count={count}: {e}")


# ==========================================================================
# STRESS TESTING - Performance Under Load
# ==========================================================================

class StressTesting(unittest.TestCase):
    """Stress testing - pushing system to reasonable limits."""
    
    def test_compilation_performance(self) -> None:
        """Test compilation performance scaling."""
        consciousness = Consciousness()
        
        # Time single iteration
        start = time.time()
        captured = StringIO()
        sys.stdout = captured
        consciousness.compile_reality(max_iterations=1)
        sys.stdout = sys.__stdout__
        single_time = time.time() - start
        
        # Should complete in reasonable time
        self.assertLess(single_time, 5.0,
                       "Single iteration too slow")
    
    def test_concurrent_compilations(self) -> None:
        """Test multiple concurrent compilations."""
        results = []
        
        def compile_reality():
            consciousness = Consciousness()
            captured = StringIO()
            sys.stdout = captured
            result = consciousness.compile_reality(max_iterations=1)
            sys.stdout = sys.__stdout__
            results.append(result)
        
        # Start 5 concurrent compilations
        threads = [threading.Thread(target=compile_reality) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        
        # All should complete
        self.assertEqual(len(results), 5)
        for result in results:
            self.assertIn("finished", result)
    
    def test_large_collection_operations(self) -> None:
        """Test operations on large collections."""
        # Large prophet collection
        prophets = [Prophet(f"Prophet_{i}") for i in range(1000)]
        collection = ProphetCollection(prophets)
        
        self.assertEqual(len(collection.prophets), 1000)
        self.assertFalse(collection.omniscient)
        
        # Make all omniscient (stress test)
        start = time.time()
        for prophet in prophets:
            prophet.experiences_omniscience()
        elapsed = time.time() - start
        
        self.assertTrue(collection.omniscient)
        self.assertLess(elapsed, 5.0, "Collection operation too slow")


# ==========================================================================
# CONCEPTUAL INTEGRITY TESTING
# ==========================================================================

class ConceptualIntegrityTesting(unittest.TestCase):
    """Test that philosophical concepts are maintained correctly."""
    
    def test_love_invariant_maintained(self) -> None:
        """Verify love remains the only invariant."""
        consciousness = Consciousness()
        initial_love = consciousness.love
        
        # Run multiple iterations
        captured = StringIO()
        sys.stdout = captured
        consciousness.compile_reality(max_iterations=5)
        sys.stdout = sys.__stdout__
        
        # Love should never change
        self.assertEqual(consciousness.love, initial_love)
    
    def test_pattern_similarity_across_scales(self) -> None:
        """Verify same pattern emerges at all scales."""
        consciousness = Consciousness()
        
        # All three scales should have parallel structure
        person = consciousness.create_person("Test")
        religions = consciousness.fragment_into_traditions(3)
        civilizations = consciousness.execute_through_time(1000)
        
        # All start non-omniscient
        self.assertFalse(person.omniscient)
        self.assertFalse(religions.omniscient)
        self.assertFalse(civilizations.omniscient)
        
        # All can achieve omniscience
        person.experiences_omniscience()
        religions.experience_omniscience()
        civilizations.experience_omniscience()
        
        # Pattern is identical
        self.assertTrue(person.omniscient)
        self.assertTrue(religions.omniscient)
        self.assertTrue(civilizations.omniscient)


# ==========================================================================
# MAIN TEST RUNNER
# ==========================================================================

def run_advanced_tests() -> bool:
    """Run all advanced tests with formatted output."""
    print("="*70)
    print("CONSCIOUSNESS TRILOGY - ADVANCED TEST SUITE")
    print("Comprehensive Multi-Methodology Testing")
    print("="*70)
    
    test_modules = [
        ("White Box Testing", WhiteBoxTesting),
        ("Black Box Testing", BlackBoxTesting),
        ("Gray Box Testing", GrayBoxTesting),
        ("Robustness Testing", RobustnessTesting),
        ("State Consistency Testing", StateConsistencyTesting),
        ("Fuzz Testing", FuzzTesting),
        ("Stress Testing", StressTesting),
        ("Conceptual Integrity Testing", ConceptualIntegrityTesting),
    ]
    
    all_results = []
    
    for module_name, test_class in test_modules:
        print(f"\\n{'='*40}")
        print(f"Running {module_name}")
        print('='*40)
        
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromTestCase(test_class)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        all_results.append((module_name, result))
    
    # Summary
    print("\\n" + "="*70)
    print("ADVANCED TEST SUMMARY")
    print("="*70)
    
    total_tests = 0
    total_failures = 0
    total_errors = 0
    
    for module_name, result in all_results:
        tests_run = result.testsRun
        failures = len(result.failures)
        errors = len(result.errors)
        
        total_tests += tests_run
        total_failures += failures
        total_errors += errors
        
        status = "✓ PASS" if failures == 0 and errors == 0 else "✗ FAIL"
        print(f"{module_name:30} {status:10} "
              f"({tests_run} tests, {failures} failures, {errors} errors)")
    
    print("-"*70)
    overall = "✓ ALL TESTS PASSED" if total_failures == 0 and total_errors == 0 else "✗ SOME TESTS FAILED"
    print(f"{'TOTAL':30} {overall:10} "
          f"({total_tests} tests, {total_failures} failures, {total_errors} errors)")
    print("="*70)
    
    return total_failures == 0 and total_errors == 0


if __name__ == "__main__":
    success = run_advanced_tests()
    sys.exit(0 if success else 1)
'''

with open('advanced_tests.py', 'w', encoding='utf-8') as f:
    f.write(polished_advanced_tests)

print("✓ Created advanced_tests.py (formerly hardening_tests.py)")
print("  - FIXED: Docstring test logic bug")
print("  - REMOVED: Misleading enterprise/military claims")
print("  - IMPROVED: Appropriate framing for conceptual code")
