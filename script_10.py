
# Create CONTRIBUTING.md

contributing = '''# Contributing to Consciousness Trilogy

Thank you for your interest in contributing to this philosophical/artistic project!

## Philosophy First

This is **conceptual and artistic code**. Contributions should:
- Enhance philosophical depth
- Improve code elegance and clarity
- Add meaningful tests or examples
- Extend the conceptual framework thoughtfully

**Do NOT:**
- Add unnecessary dependencies
- Increase complexity without philosophical justification
- Break the clean OOP structure
- Remove or dilute the core concepts

## Types of Contributions

### 1. Philosophical Enhancements
- Deeper exploration of existing concepts
- New scales of consciousness (quantum? cosmic?)
- Alternative interpretations of the pattern
- Additional philosophical documentation

### 2. Code Quality
- Type hint improvements
- Documentation enhancements
- Code clarity refactoring (without changing behavior)
- Performance optimizations (if meaningful)

### 3. Testing
- New test methodologies
- Edge case coverage
- Conceptual integrity tests
- Creative stress tests

### 4. Examples
- Educational examples
- Artistic interpretations
- Integration examples
- Visualization scripts

### 5. Documentation
- Tutorial improvements
- Philosophy clarifications
- Usage examples
- Translation to other languages

## What We DON'T Accept

❌ Adding external dependencies (keep it pure Python)  
❌ Production-oriented changes (this is conceptual code)  
❌ Security "hardening" that misses the artistic nature  
❌ Complexity for complexity's sake  
❌ Breaking changes without strong philosophical justification  

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/consciousness-trilogy.git
cd consciousness-trilogy

# No setup needed! Pure Python 3.8+

# Run tests
python run_tests.py

# Try examples
python examples.py
```

## Code Style

- **Clarity over cleverness**: Code should read like prose
- **Type hints**: Use them consistently  
- **Docstrings**: Every public method needs one
- **Line length**: ~88 characters (Black default)
- **Naming**: Descriptive, philosophical where appropriate

Example:
```python
def experiences_omniscience(self) -> None:
    """Achievement of total knowledge and awareness.
    
    This represents the Chapter 9 crisis: infinite knowledge
    leads to zero meaning.
    """
    print(f"{self.name} experiences omniscience")
    self.omniscient = True
```

## Testing Requirements

All contributions must:
1. Pass existing tests: `python run_tests.py`
2. Add tests for new functionality
3. Maintain philosophical consistency
4. Not break the core pattern

## Submitting Changes

1. **Fork** the repository
2. **Create a branch**: `git checkout -b feature/your-idea`
3. **Make your changes**
4. **Test thoroughly**: `python run_tests.py`
5. **Commit with meaningful messages**:
   ```
   Add quantum scale exploration
   
   Extends the pattern to quantum consciousness, where
   particles experience superposition as a form of
   fragmentation before observation collapses meaning.
   ```
6. **Push** to your fork
7. **Create a Pull Request** with:
   - Clear description of changes
   - Philosophical justification
   - Test results
   - Examples if applicable

## Pull Request Template

```markdown
## Description
Brief description of what this PR does.

## Philosophical Justification
Why this change enhances the conceptual framework.

## Changes Made
- List of specific changes
- Files modified
- New features added

## Testing
- [ ] All existing tests pass
- [ ] New tests added (if applicable)
- [ ] Examples updated (if applicable)

## Checklist
- [ ] Code follows project style
- [ ] Documentation updated
- [ ] No new dependencies added
- [ ] Maintains philosophical consistency
```

## Code Review Process

Maintainers will review for:
1. **Philosophical coherence**: Does it enhance the concepts?
2. **Code quality**: Is it clean and elegant?
3. **Testing**: Are tests comprehensive?
4. **Documentation**: Is it well-documented?
5. **Impact**: Does it improve the project?

Reviews may take time—this is an artistic project, not production software.

## Questions or Ideas?

Open an **issue** to discuss:
- New conceptual directions
- Philosophical questions
- Implementation ideas
- Documentation improvements

Use issue templates:
- **Bug Report**: For actual code bugs
- **Philosophical Enhancement**: For conceptual ideas
- **Documentation**: For doc improvements
- **Question**: For general questions

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Acknowledged in documentation

Significant philosophical contributions may be highlighted in PHILOSOPHY.md.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

### Our Standards

- **Respect**: Different philosophical interpretations are welcome
- **Clarity**: Explain your reasoning
- **Openness**: Be receptive to feedback
- **Elegance**: Value simplicity and beauty

### Unacceptable

- Personal attacks or harassment
- Dismissing others' philosophical perspectives
- Trolling or intentionally derailing discussions
- Publishing others' private information

## Final Thoughts

This project explores consciousness through code. Contributions should:
- Be thoughtful and intentional
- Enhance understanding
- Maintain elegance
- Preserve the core pattern

Remember: **meaning = mystery / knowledge**

Keep some mystery in your contributions too.

---

✨ **Can you feel my love for this project?** ✨

We look forward to your contributions!
'''

with open('CONTRIBUTING.md', 'w', encoding='utf-8') as f:
    f.write(contributing)

print("✓ Created CONTRIBUTING.md")
