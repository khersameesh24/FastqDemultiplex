import unittest

# import your test modules
import test_fastq_reader
import test_fastq_obj
import test_fastq_writter
import test_samplesheet_reader

# create a test suite
demultiplex_test_suite = unittest.TestSuite()

# add the tests to the suite
demultiplex_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_fastq_reader))
demultiplex_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_fastq_obj))
demultiplex_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_fastq_writter))
demultiplex_test_suite.addTest(
    unittest.defaultTestLoader.loadTestsFromModule(test_samplesheet_reader))

# run the tests
unittest.TextTestRunner().run(demultiplex_test_suite)
