from abc import ABC, abstractmethod
from pydantic import BaseModel
from decisify.explainer import Explainer

class DummyModel(BaseModel):
    data: str

class TestExplainer(Explainer):
    def explain(self, query: str, ref_input: BaseModel):
        return f"Explaining {query} with {ref_input}"

    def interrogate(self, query: str, ref_input: BaseModel):
        return f"Interrogating {query} with {ref_input}"

def setup_module(module):
    global explainer, query, ref_input
    explainer = TestExplainer()
    query = "test query"
    ref_input = DummyModel(data="test data")

def test_explain():
    result = explainer.explain(query, ref_input)
    assert result == f"Explaining {query} with {ref_input}"

def test_interrogate():
    result = explainer.interrogate(query, ref_input)
    assert result == f"Interrogating {query} with {ref_input}"
