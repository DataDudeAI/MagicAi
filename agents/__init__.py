"""
AI Tool Hub - Agents Package
Contains intelligent agents for model selection and task optimization
"""

from .model_selector import ModelSelector
from pathlib import Path

# Ensure knowledge directories exist
def init_knowledge_dirs():
    base_path = Path(__file__).parent
    knowledge_dirs = [
        "knowledge/internal",
        "knowledge/external",
        "training/data"
    ]
    
    for dir_path in knowledge_dirs:
        (base_path / dir_path).mkdir(parents=True, exist_ok=True)

# Initialize package
init_knowledge_dirs()

__all__ = ['ModelSelector'] 