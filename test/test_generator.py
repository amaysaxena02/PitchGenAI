import unittest
from generators.pitch_generator import generate_pitch

class TestPitchGenerator(unittest.TestCase):

    def test_generate_pitch_basic(self):
        """Test pitch generation returns a non-empty string."""
        test_startup = {
            "name": "AI Coffee",
            "problem": "People waste time making coffee manually",
            "solution": "Automated AI coffee machines",
            "market": "Coffee shops and offices",
            "business_model": "Subscription + hardware sales",
            "tone": "formal"
        }
        result = generate_pitch(test_startup)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()