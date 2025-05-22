"""
Training module for the Model Selector Agent
"""
import json
import random
from typing import List, Dict, Any, Tuple
from pathlib import Path
from ..model_selector import ModelSelector

class ModelSelectorTrainer:
    def __init__(self):
        self.model_selector = ModelSelector()
        self.training_data_path = Path(__file__).parent / "data"
        self.training_scenarios = self._load_training_scenarios()
        
    def _load_training_scenarios(self) -> List[Dict[str, Any]]:
        """Load training scenarios from JSON file"""
        scenarios_file = self.training_data_path / "training_scenarios.json"
        if not scenarios_file.exists():
            self._create_training_scenarios()
        
        with open(scenarios_file, 'r') as f:
            return json.load(f)
    
    def _create_training_scenarios(self):
        """Create and save training scenarios"""
        scenarios = [
            {
                "tool_type": "text-generation",
                "task_type": "creative",
                "provider": "openai",
                "context_length": 2000,
                "expected_model": "gpt-4",
                "description": "Creative writing task with moderate context"
            },
            {
                "tool_type": "text-generation",
                "task_type": "technical",
                "provider": "openrouter",
                "context_length": 50000,
                "expected_model": "anthropic/claude-2",
                "description": "Technical documentation with very long context"
            },
            {
                "tool_type": "code-generation",
                "task_type": "python",
                "provider": "deepseek",
                "context_length": 4000,
                "expected_model": "deepseek-ai/deepseek-coder-33b-instruct",
                "description": "Python code generation task"
            },
            {
                "tool_type": "image-generation",
                "task_type": "high_quality",
                "provider": "openai",
                "context_length": None,
                "expected_model": "dall-e-3",
                "description": "High-quality image generation"
            }
        ]
        
        # Save scenarios
        self.training_data_path.mkdir(parents=True, exist_ok=True)
        with open(self.training_data_path / "training_scenarios.json", 'w') as f:
            json.dump(scenarios, f, indent=2)
    
    def evaluate_scenario(self, scenario: Dict[str, Any]) -> Tuple[bool, str]:
        """Evaluate a single training scenario"""
        selected_model, model_info = self.model_selector.select_model(
            tool_type=scenario["tool_type"],
            provider=scenario["provider"],
            task_type=scenario["task_type"],
            context_length=scenario["context_length"]
        )
        
        success = selected_model == scenario["expected_model"]
        message = (
            f"Success: Selected {selected_model} matches expected {scenario['expected_model']}"
            if success else
            f"Failure: Selected {selected_model} does not match expected {scenario['expected_model']}"
        )
        
        return success, message
    
    def run_training_evaluation(self) -> Dict[str, Any]:
        """Run evaluation on all training scenarios"""
        results = {
            "total_scenarios": len(self.training_scenarios),
            "successful": 0,
            "failed": 0,
            "scenario_results": []
        }
        
        for scenario in self.training_scenarios:
            success, message = self.evaluate_scenario(scenario)
            results["scenario_results"].append({
                "description": scenario["description"],
                "success": success,
                "message": message
            })
            
            if success:
                results["successful"] += 1
            else:
                results["failed"] += 1
        
        results["success_rate"] = results["successful"] / results["total_scenarios"]
        return results
    
    def generate_test_scenario(self) -> Dict[str, Any]:
        """Generate a random test scenario"""
        tool_types = ["text-generation", "code-generation", "image-generation"]
        providers = {
            "text-generation": ["openai", "openrouter", "huggingface"],
            "code-generation": ["openai", "deepseek", "openrouter"],
            "image-generation": ["openai", "huggingface"]
        }
        task_types = {
            "text-generation": ["creative", "technical", "default"],
            "code-generation": ["python", "javascript", "default"],
            "image-generation": ["high_quality", "default"]
        }
        
        tool_type = random.choice(tool_types)
        provider = random.choice(providers[tool_type])
        task_type = random.choice(task_types[tool_type])
        
        # Get expected model from internal knowledge
        tool_info = self.model_selector.internal_knowledge.get(tool_type, {})
        provider_models = tool_info.get("optimal_models", {}).get(provider, {})
        expected_model = provider_models.get(task_type, provider_models.get("default"))
        
        return {
            "tool_type": tool_type,
            "provider": provider,
            "task_type": task_type,
            "context_length": random.choice([None, 2000, 4000, 8000, 50000]),
            "expected_model": expected_model,
            "description": f"Random test: {tool_type} with {provider} for {task_type} task"
        }
    
    def run_random_tests(self, num_tests: int = 10) -> Dict[str, Any]:
        """Run a series of random tests"""
        results = {
            "total_tests": num_tests,
            "successful": 0,
            "failed": 0,
            "test_results": []
        }
        
        for _ in range(num_tests):
            scenario = self.generate_test_scenario()
            success, message = self.evaluate_scenario(scenario)
            
            results["test_results"].append({
                "scenario": scenario,
                "success": success,
                "message": message
            })
            
            if success:
                results["successful"] += 1
            else:
                results["failed"] += 1
        
        results["success_rate"] = results["successful"] / results["total_tests"]
        return results

if __name__ == "__main__":
    # Run training evaluation
    trainer = ModelSelectorTrainer()
    print("Running training evaluation...")
    training_results = trainer.run_training_evaluation()
    print(f"Training success rate: {training_results['success_rate']*100:.1f}%")
    
    # Run random tests
    print("\nRunning random tests...")
    test_results = trainer.run_random_tests(num_tests=20)
    print(f"Random test success rate: {test_results['success_rate']*100:.1f}%") 