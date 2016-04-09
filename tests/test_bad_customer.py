from nose.tools import assert_raises


def test_failed_import():
    with assert_raises(ImportError):
        import circular_references.bad_customer

