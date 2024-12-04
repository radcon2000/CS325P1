import pytest

import CWP4F1
from CWP4F1 import response

def test_negativeReview():
    assert response("C:/Users/KimJo/project3/negativeReview1.txt", 0) == [0, 1, 0]

def test_PositiveReview():
    assert response("C:/Users/KimJo/project3/positiveReview1.txt", 0) == [1, 0, 0]

def test_neutralReview():
    assert response("C:/Users/KimJo/project3/neutralReview1.txt", 0) == [0, 0, 1]

def test_mixedReview():
    assert response("C:/Users/KimJo/project3/mixedReview1.txt", 0) == [1, 1, 1]
