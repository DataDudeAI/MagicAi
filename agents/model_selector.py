"""
Model Selector Agent
Intelligently selects the optimal model for each task based on internal and external knowledge
"""
import json
import os
from typing import Dict, Any, Optional, List, Tuple
from pathlib import Path

class ModelSelector:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.internal_knowledge = self._load_json("knowledge/internal/tool_capabilities.json")
        self.external_knowledge = self._load_json("knowledge/external/model_capabilities.json")
        
    def _load_json(self, relative_path: str) -> Dict[str, Any]:
        """Load JSON knowledge file"""
        file_path = self.base_path / relative_path
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {relative_path}: {e}")
            return {}

    def select_model(self, 
                    tool_type: str, 
                    provider: str, 
                    task_type: Optional[str] = None,
                    context_length: Optional[int] = None) -> Tuple[str, Dict[str, Any]]:
        """
        Select the optimal model based on tool type, provider, and requirements
        
        Args:
            tool_type: Type of tool (e.g., "text-generation", "code-generation")
            provider: Provider name (e.g., "openai", "openrouter")
            task_type: Specific type of task (e.g., "creative", "technical")
            context_length: Required context length if any
            
        Returns:
            Tuple of (selected_model_id, model_info)
        """
        # Get tool-specific knowledge
        tool_info = self.internal_knowledge.get(tool_type, {})
        if not tool_info:
            return self._get_fallback_model(provider), {}
            
        # Get optimal models for this tool and provider
        provider_models = tool_info.get("optimal_models", {}).get(provider, {})
        if not provider_models:
            return self._get_fallback_model(provider), {}
            
        # Select model based on task type
        model_id = provider_models.get(task_type or "default", provider_models.get("default"))
        if not model_id:
            return self._get_fallback_model(provider), {}
            
        # Get external knowledge about the model
        model_info = self._get_model_info(model_id)
        
        # Validate context length requirement if specified
        if context_length and model_info.get("context_length", 0) < context_length:
            # Try to find a model with sufficient context length
            alt_model = self._find_model_with_context(provider_models, context_length)
            if alt_model:
                model_id = alt_model
                model_info = self._get_model_info(model_id)
        
        return model_id, model_info
    
    def _get_fallback_model(self, provider: str) -> str:
        """Get a fallback model for a provider"""
        fallbacks = {
            "openai": "gpt-3.5-turbo",
            "openrouter": "meta-llama/llama-2-70b-chat",
            "huggingface": "mistralai/Mistral-7B-Instruct-v0.2",
            "deepseek": "deepseek-ai/deepseek-chat-7b"
        }
        return fallbacks.get(provider, "gpt-3.5-turbo")
    
    def _get_model_info(self, model_id: str) -> Dict[str, Any]:
        """Get external knowledge about a model"""
        # Extract base model name from full path if needed
        base_name = model_id.split('/')[-1]
        
        # Check language models
        model_info = self.external_knowledge.get("language_models", {}).get(base_name, {})
        if model_info:
            return model_info
            
        # Check image models
        model_info = self.external_knowledge.get("image_models", {}).get(base_name, {})
        if model_info:
            return model_info
            
        return {}
    
    def _find_model_with_context(self, provider_models: Dict[str, str], required_length: int) -> Optional[str]:
        """Find a model that satisfies the context length requirement"""
        for model_id in provider_models.values():
            model_info = self._get_model_info(model_id)
            if model_info.get("context_length", 0) >= required_length:
                return model_id
        return None
    
    def get_model_capabilities(self, model_id: str) -> List[str]:
        """Get the capabilities of a specific model"""
        model_info = self._get_model_info(model_id)
        return model_info.get("capabilities", [])
    
    def get_recommended_providers(self, tool_type: str) -> List[str]:
        """Get recommended providers for a tool type"""
        tool_info = self.internal_knowledge.get(tool_type, {})
        return tool_info.get("best_providers", []) 