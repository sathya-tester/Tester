import pytest
@pytest.mark.smoke
def testsmoke1():
    print('smoke 1 data')


@pytest.mark.regression
def testregression1():
    print('regression 1 test')

@pytest.mark.smoke
def testsmoke2():
    print('smoke 2 data')

@pytest.mark.sanity
def testregression2():
    print('regression 2 test')