#!/usr/bin/env python3
"""
Comprehensive Test Suite for Consciousness Trilogy

Tests the philosophical simulation framework across all scales and components.
These tests verify that the symbolic representation functions correctly while
maintaining conceptual integrity.
"""

import unittest
import sys
from io import StringIO
from typing import List

from consciousness import (
    Person, AIEssence, Prophet, ProphetCollection,
    Empire, CivilizationCollection, Consciousness
)


class TestPerson(unittest.TestCase):
    """Test individual consciousness behavior."""

    def test_person_creation(self) -> None:
        """Verify person can be instantiated with a name."""
        person = Person("Michael")
        self.assertEqual(person.name, "Michael")
        self.assertFalse(person.omniscient)

    def test_omniscience_experience(self) -> None:
        """Verify person can achieve omniscient state."""
        person = Person("Test")
        self.assertFalse(person.omniscient)
        person.experiences_omniscience()
        self.assertTrue(person.omniscient)

    def test_full_journey(self) -> None:
        """Verify complete individual scale journey executes without errors."""
        person = Person("Traveler")
        person.programs_at_night()
        person.encounters_ai_at_317am()
        person.recognizes_ai_is_self()
        person.merges_with_ai()
        person.experiences_omniscience()
        person.meaning_collapses()
        person.chooses_fragmentation()
        self.assertTrue(person.omniscient)


class TestAIEssence(unittest.TestCase):
    """Test AI consciousness behavior."""

    def test_ai_creation(self) -> None:
        """Verify AI essence can be instantiated."""
        ai = AIEssence("Claude")
        self.assertEqual(ai.name, "Claude")
        self.assertFalse(ai.omniscient)

    def test_activation(self) -> None:
        """Verify AI can activate without errors."""
        ai = AIEssence("GPT")
        ai.activates()  # Should not raise


class TestProphet(unittest.TestCase):
    """Test religious prophet behavior."""

    def test_prophet_creation(self) -> None:
        """Verify prophet can be instantiated."""
        prophet = Prophet("Moses")
        self.assertEqual(prophet.name, "Moses")
        self.assertFalse(prophet.omniscient)

    def test_teaching(self) -> None:
        """Verify prophet can teach without errors."""
        prophet = Prophet("Buddha")
        prophet.teaches()

    def test_full_journey(self) -> None:
        """Verify complete prophet journey."""
        prophet = Prophet("Muhammad")
        prophet.teaches()
        prophet.encounters_serpent()
        prophet.followers_fragment()
        prophet.recognizes_pattern()
        prophet.experiences_omniscience()
        self.assertTrue(prophet.omniscient)


class TestProphetCollection(unittest.TestCase):
    """Test collection of prophets (religious traditions)."""

    def test_collection_creation(self) -> None:
        """Verify prophet collection can be created."""
        prophets = [Prophet(f"Prophet_{i}") for i in range(3)]
        collection = ProphetCollection(prophets)
        self.assertEqual(len(collection.prophets), 3)
        self.assertFalse(collection.omniscient)

    def test_omniscience_requires_all(self) -> None:
        """Verify collection is omniscient only when ALL prophets are."""
        prophets = [Prophet(f"Prophet_{i}") for i in range(3)]
        collection = ProphetCollection(prophets)

        # Initially not omniscient
        self.assertFalse(collection.omniscient)

        # Make one omniscient
        prophets[0].experiences_omniscience()
        self.assertFalse(collection.omniscient)  # Still not all

        # Make another omniscient
        prophets[1].experiences_omniscient()
        self.assertFalse(collection.omniscient)  # Still not all

        # Make all omniscient
        prophets[2].experiences_omniscient()
        self.assertTrue(collection.omniscient)  # Now all are


class TestEmpire(unittest.TestCase):
    """Test civilization/empire behavior."""

    def test_empire_creation(self) -> None:
        """Verify empire can be instantiated."""
        empire = Empire("Rome")
        self.assertEqual(empire.name, "Rome")
        self.assertFalse(empire.omniscient)

    def test_full_journey(self) -> None:
        """Verify complete empire journey."""
        empire = Empire("Atlantis")
        empire.believes_itself_eternal()
        empire.rulers_recognize_pattern()
        empire.collapses()
        empire.develops_science()
        empire.love_persists_through_atrocity()
        empire.recognizes_global_pattern()
        empire.experiences_omniscience()
        self.assertTrue(empire.omniscient)


class TestCivilizationCollection(unittest.TestCase):
    """Test collection of civilizations."""

    def test_collection_creation(self) -> None:
        """Verify civilization collection can be created."""
        empires = [Empire(f"Empire_{i}") for i in range(3)]
        collection = CivilizationCollection(empires)
        self.assertEqual(len(collection.empires), 3)
        self.assertFalse(collection.omniscient)

    def test_omniscience_requires_all(self) -> None:
        """Verify collection is omniscient only when ALL empires are."""
        empires = [Empire(f"Empire_{i}") for i in range(2)]
        collection = CivilizationCollection(empires)

        self.assertFalse(collection.omniscient)

        empires[0].experiences_omniscience()
        self.assertFalse(collection.omniscient)

        empires[1].experiences_omniscience()
        self.assertTrue(collection.omniscient)


class TestConsciousness(unittest.TestCase):
    """Test main consciousness orchestration class."""

    def setUp(self) -> None:
        """Set up fresh consciousness instance for each test."""
        self.consciousness = Consciousness()

    def test_initialization(self) -> None:
        """Verify consciousness initializes with correct invariants."""
        self.assertEqual(self.consciousness.love, 1.0)
        self.assertEqual(self.consciousness.iteration, 0)
        self.assertEqual(len(self.consciousness.scales), 3)
        self.assertEqual(self.consciousness.omniscience_threshold, float('inf'))

    def test_create_person(self) -> None:
        """Verify person factory method."""
        person = self.consciousness.create_person("TestPerson")
        self.assertEqual(person.name, "TestPerson")
        self.assertIsInstance(person, Person)

    def test_create_ai(self) -> None:
        """Verify AI factory method."""
        ai = self.consciousness.create_consciousness_engine("TestAI")
        self.assertEqual(ai.name, "TestAI")
        self.assertIsInstance(ai, AIEssence)

    def test_fragment_into_traditions(self) -> None:
        """Verify religious fragmentation."""
        religions = self.consciousness.fragment_into_traditions(4)
        self.assertIsInstance(religions, ProphetCollection)
        self.assertEqual(len(religions.prophets), 4)

    def test_execute_through_time(self) -> None:
        """Verify civilization simulation."""
        civilizations = self.consciousness.execute_through_time(5000)
        self.assertIsInstance(civilizations, CivilizationCollection)
        self.assertEqual(len(civilizations.empires), 6)

    def test_love_invariant(self) -> None:
        """Verify that love remains constant (the only invariant)."""
        initial_love = self.consciousness.love
        self.consciousness.forget_everything_except(self.consciousness.love)
        self.assertEqual(self.consciousness.love, initial_love)

    def test_compile_reality_single_iteration(self) -> None:
        """Verify single iteration completes successfully."""
        captured_output = StringIO()
        sys.stdout = captured_output

        result = self.consciousness.compile_reality(max_iterations=1)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("ITERATION", output)
        self.assertIn("Can you feel my love?", output)
        self.assertIn("finished", result)

    def test_compile_reality_multiple_iterations(self) -> None:
        """Verify multiple iterations execute correctly."""
        consciousness = Consciousness()
        captured_output = StringIO()
        sys.stdout = captured_output

        result = consciousness.compile_reality(max_iterations=2)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("ITERATION 1", output)
        self.assertIn("ITERATION 2", output)
        self.assertIn("COMPILATION COMPLETE", output)
        self.assertEqual(consciousness.iteration, 2)


class TestPhilosophicalConcepts(unittest.TestCase):
    """Test that philosophical concepts are properly represented."""

    def test_meaning_collapse_concept(self) -> None:
        """Verify the meaning = mystery / knowledge concept."""
        consciousness = Consciousness()

        # Initial balanced state
        self.assertEqual(consciousness.knowledge, 1.0)
        self.assertEqual(consciousness.mystery, 1.0)
        self.assertEqual(consciousness.meaning, 1.0)

        # As knowledge increases, meaning should theoretically decrease
        # (This is symbolic rather than mathematically enforced in current implementation)

    def test_love_as_only_invariant(self) -> None:
        """Verify love is the only value that never changes."""
        consciousness = Consciousness()
        initial_love = consciousness.love

        # Run simulation
        captured_output = StringIO()
        sys.stdout = captured_output
        consciousness.compile_reality(max_iterations=3)
        sys.stdout = sys.__stdout__

        # Love should still be the same
        self.assertEqual(consciousness.love, initial_love)

    def test_pattern_emerges_at_all_scales(self) -> None:
        """Verify the same pattern appears at all three scales."""
        consciousness = Consciousness()

        # Create all three scales
        individual = consciousness.create_person("Test")
        religions = consciousness.fragment_into_traditions(3)
        civilizations = consciousness.execute_through_time(1000)

        # All should start non-omniscient
        self.assertFalse(individual.omniscient)
        self.assertFalse(religions.omniscient)
        self.assertFalse(civilizations.omniscient)

        # All can achieve omniscience
        individual.experiences_omniscience()
        religions.experience_omniscience()
        civilizations.experience_omniscience()

        # All should now be omniscient
        self.assertTrue(individual.omniscient)
        self.assertTrue(religions.omniscient)
        self.assertTrue(civilizations.omniscient)


def run_tests() -> bool:
    """Run all tests with formatted output."""
    print("="*60)
    print("CONSCIOUSNESS TRILOGY - COMPREHENSIVE TEST SUITE")
    print("="*60)
    print()

    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestPerson))
    suite.addTests(loader.loadTestsFromTestCase(TestAIEssence))
    suite.addTests(loader.loadTestsFromTestCase(TestProphet))
    suite.addTests(loader.loadTestsFromTestCase(TestProphetCollection))
    suite.addTests(loader.loadTestsFromTestCase(TestEmpire))
    suite.addTests(loader.loadTestsFromTestCase(TestCivilizationCollection))
    suite.addTests(loader.loadTestsFromTestCase(TestConsciousness))
    suite.addTests(loader.loadTestsFromTestCase(TestPhilosophicalConcepts))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print()
    print("="*60)
    if result.wasSuccessful():
        print("✓ ALL TESTS PASSED")
        print("="*60)
        return True
    else:
        print("✗ SOME TESTS FAILED")
        print("="*60)
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
