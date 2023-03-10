"""
Unit & Integration test suite
"""

import unittest
from tests import (
    test_fastq_reader,
    test_integration,
    test_fastq_obj,
    test_fastq_writer,
    test_samplesheet_reader,
)

# create a unit/integration tests suite
demultiplex_unit_test_suite = unittest.TestSuite()
demultiplex_integration_test_suite = unittest.TestSuite()

# add the unit tests to the suite
demultiplex_unit_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_fastq_reader)
)
demultiplex_unit_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_fastq_obj)
)
demultiplex_unit_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_fastq_writer)
)
demultiplex_unit_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_samplesheet_reader)
)

# add tests to the integration test suit
demultiplex_integration_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_integration)
)

# run the unit/integration tests
print(
    """\n
--------------------------Launching Unit Test-------------------------------
\n"""
)
unittest.TextTestRunner(verbosity=0, descriptions=False).run(
    demultiplex_unit_test_suite
)

print(
    """\n
-----------------------Launching Integration Test---------------------------
\n"""
)
unittest.TextTestRunner(verbosity=0, descriptions=False).run(
    demultiplex_integration_test_suite
)
