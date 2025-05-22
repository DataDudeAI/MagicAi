"""
Tool definitions for AI Tool Hub
Defines available tools and their configurations
"""
from typing import List, Dict, Any, Optional
from agents import ModelSelector

class Tool:
    def __init__(self, 
                 id: str,
                 name: str,
                 description: str,
                 icon: str,
                 cost: float,
                 example_prompts: List[str],
                 providers: List[str],
                 ad_duration: int = 60,
                 credits: Optional[float] = None,
                 ad_reward: float = 1.0):
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.cost = cost
        self.example_prompts = example_prompts
        self.providers = providers
        self.ad_duration = ad_duration
        self.credits = credits if credits is not None else cost
        self.ad_reward = ad_reward
        self.model_selector = ModelSelector()

    def get_info(self) -> Dict[str, Any]:
        """Return a summary of the tool's information."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "cost": self.cost,
            "example_prompts": self.example_prompts,
            "providers": self.providers,
            "ad_duration": self.ad_duration,
            "credits": self.credits,
            "ad_reward": self.ad_reward,
            "recommended_providers": self.get_recommended_providers()
        }

    def get_default_model(self, provider: str, task_type: str = "default") -> str:
        """Get the default model for a specific provider and task type"""
        tool_type = self.id.replace("-", "_")  # Convert tool ID to match knowledge base format
        model_id, _ = self.model_selector.select_model(
            tool_type=tool_type,
            provider=provider,
            task_type=task_type
        )
        return model_id

    def get_recommended_providers(self) -> List[str]:
        """Get recommended providers for this tool"""
        tool_type = self.id.replace("-", "_")
        return self.model_selector.get_recommended_providers(tool_type)

    def get_model_capabilities(self, model_id: str) -> List[str]:
        """Get capabilities of a specific model"""
        return self.model_selector.get_model_capabilities(model_id)

# Define the tools with associated prompts
TOOLS = [
    Tool(
        id="text-generation",
        name="Text Generation",
        description="Generate text using AI models",
        icon="text.svg",
        cost=1.0,
        example_prompts=[
            "Write a short story about a robot learning to paint.",
            "Create a product description for a new smartphone.",
            "Explain quantum computing to a 10-year-old."
        ],
        providers=["openrouter", "openai", "deepseek", "huggingface"],
        ad_duration=60,
        credits=1.0,
        ad_reward=1
    ),
    Tool(
        id="image-generation",
        name="Image Generation",
        description="Generate images from text descriptions",
        icon="image.svg",
        cost=5.0,
        example_prompts=[
            "A futuristic city with flying cars and tall buildings.",
            "A photorealistic portrait of a cyberpunk character.",
            "A peaceful mountain landscape at sunset."
        ],
        providers=["openai", "huggingface", "replicate"],
        ad_duration=60,
        credits=5.0,
        ad_reward=1
    ),
    Tool(
        id="code-generation",
        name="Code Generation",
        description="Generate code in various programming languages",
        icon="code.svg",
        cost=2.0,
        example_prompts=[
            "Write a Python function to calculate Fibonacci numbers.",
            "Create a React component for a login form.",
            "Generate a SQL query to find customers who made purchases last month."
        ],
        providers=["openai", "deepseek", "openrouter"],
        ad_duration=60,
        credits=2.0,
        ad_reward=1
    ),
    Tool(
        id="ai-copywriter",
        name="AI Copywriter",
        description="Generates product descriptions and creative content.",
        icon="copywriter.svg",
        cost=0.20,
        example_prompts=[
            "Generate a product description for a new gadget.",
            "Create a catchy tagline for a marketing campaign."
        ],
        providers=["huggingface", "openrouter", "openai"],
        ad_duration=60,
        credits=0.20,
        ad_reward=1
    ),
    Tool(
        id="email-generator",
        name="Email Generator",
        description="Drafts professional or marketing emails.",
        icon="email.svg",
        cost=0.18,
        example_prompts=[
            "Draft a follow-up email for a job application.",
            "Create a marketing email for a new product launch."
        ],
        providers=["huggingface", "deepseek", "openai"],
        ad_duration=60,
        credits=0.18,
        ad_reward=1
    ),
    Tool(
        id="blog-writer",
        name="Blog Writer",
        description="Writes detailed blog posts with SEO optimization.",
        icon="blog.svg",
        cost=0.30,
        example_prompts=[
            "Write a blog post about the benefits of meditation.",
            "Create a travel blog post about Paris."
        ],
        providers=["huggingface", "deepseek", "openai"],
        ad_duration=60,
        credits=0.30,
        ad_reward=1
    ),
    Tool(
        id="resume-builder",
        name="AI Resume Builder",
        description="Creates professional resumes tailored to job roles.",
        icon="resume.svg",
        cost=0.25,
        example_prompts=[
            "Create a resume for a software engineer.",
            "Draft a resume for a marketing manager."
        ],
        providers=["huggingface", "openrouter"],
        ad_duration=60,
        credits=0.25,
        ad_reward=1
    ),
    Tool(
        id="cover-letter-creator",
        name="Cover Letter Creator",
        description="Generates customized cover letters.",
        icon="cover_letter.svg",
        cost=0.20,
        example_prompts=[
            "Generate a cover letter for a data analyst position.",
            "Create a cover letter for a graphic designer role."
        ],
        providers=["huggingface", "openrouter"],
        ad_duration=60,
        credits=0.20,
        ad_reward=1
    ),
    Tool(
        id="script-generator",
        name="Script Generator",
        description="Writes engaging video or movie scripts.",
        icon="script.svg",
        cost=0.30,
        example_prompts=[
            "Write a script for a 5-minute promotional video.",
            "Create a movie script for a romantic comedy."
        ],
        providers=["huggingface", "deepseek"],
        ad_duration=60,
        credits=0.30,
        ad_reward=1
    ),
    Tool(
        id="storytelling",
        name="AI Storytelling",
        description="Develops creative and compelling stories.",
        icon="storytelling.svg",
        cost=0.20,
        example_prompts=[
            "Create a fantasy story about a dragon.",
            "Write a mystery story set in a small town."
        ],
        providers=["huggingface", "openrouter"],
        ad_duration=60,
        credits=0.20,
        ad_reward=1
    ),
    Tool(
        id="chatbot-assistant",
        name="Chatbot Assistant",
        description="Provides conversational responses for support.",
        icon="chatbot.svg",
        cost=0.18,
        example_prompts=[
            "Provide support for a customer inquiry.",
            "Answer frequently asked questions about a product."
        ],
        providers=["huggingface", "deepseek"],
        ad_duration=60,
        credits=0.18,
        ad_reward=1
    ),
    Tool(
        id="ai-image-generator",
        name="AI Image Generator",
        description="Creates visuals from text prompts.",
        icon="ai_image.svg",
        cost=2.50,
        example_prompts=[
            "Generate an image of a sunset over the mountains.",
            "Create an illustration of a futuristic city."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=2.50,
        ad_reward=1
    ),
    Tool(
        id="ai-logo-creator",
        name="AI Logo Creator",
        description="Designs logos for startups and businesses.",
        icon="logo.svg",
        cost=1.50,
        example_prompts=[
            "Create a logo for a new tech startup.",
            "Design a logo for a coffee shop."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=1.50,
        ad_reward=1
    ),
    Tool(
        id="ai-avatar-generator",
        name="AI Avatar Generator",
        description="Generates custom avatars for gaming or profiles.",
        icon="avatar.svg",
        cost=2.00,
        example_prompts=[
            "Generate an avatar for a gaming profile.",
            "Create a custom avatar for a social media account."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=2.00,
        ad_reward=1
    ),
    Tool(
        id="ai-face-swap",
        name="AI Face Swap",
        description="Swaps faces in images or videos seamlessly.",
        icon="face_swap.svg",
        cost=2.00,
        example_prompts=[
            "Swap faces in a family photo.",
            "Create a fun face swap for a video."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=2.00,
        ad_reward=1
    ),
    Tool(
        id="ai-meme-creator",
        name="AI Meme Creator",
        description="Generates memes with custom captions.",
        icon="meme.svg",
        cost=0.40,
        example_prompts=[
            "Create a meme about cats.",
            "Generate a funny meme for social media."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=0.40,
        ad_reward=1
    ),
    Tool(
        id="ai-video-editor",
        name="AI Video Editor",
        description="Automates video edits, transitions, and effects.",
        icon="video_editor.svg",
        cost=10.00,
        example_prompts=[
            "Edit a video for a YouTube channel.",
            "Create a highlight reel from a sports event."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=10.00,
        ad_reward=1
    ),
    Tool(
        id="ai-video-script-writer",
        name="AI Video Script Writer",
        description="Generates structured video content ideas.",
        icon="video_script.svg",
        cost=0.30,
        example_prompts=[
            "Write a script for a cooking tutorial.",
            "Create a script for a travel vlog."
        ],
        providers=["huggingface", "deepseek"],
        ad_duration=60,
        credits=0.30,
        ad_reward=1
    ),
    Tool(
        id="ai-video-dubbing",
        name="AI Video Dubbing",
        description="Dubs videos in multiple languages with natural voices.",
        icon="video_dubbing.svg",
        cost=5.00,
        example_prompts=[
            "Dub a video in Spanish.",
            "Create a multilingual version of a promotional video."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=5.00,
        ad_reward=1
    ),
    Tool(
        id="ai-data-analyzer",
        name="AI Data Analyzer",
        description="Analyzes datasets for insights and trends.",
        icon="data_analyzer.svg",
        cost=3.00,
        example_prompts=[
            "Analyze sales data for trends.",
            "Generate insights from customer feedback data."
        ],
        providers=["huggingface", "deepseek"],
        ad_duration=60,
        credits=3.00,
        ad_reward=1
    ),
    Tool(
        id="ai-code-optimizer",
        name="AI Code Optimizer",
        description="Enhances Python, JavaScript, and SQL code.",
        icon="code_optimizer.svg",
        cost=0.60,
        example_prompts=[
            "Optimize this Python function for performance.",
            "Improve the readability of this SQL query."
        ],
        providers=["huggingface", "deepseek"],
        ad_duration=60,
        credits=0.60,
        ad_reward=1
    ),
    Tool(
        id="ai-debugging-assistant",
        name="AI Debugging Assistant",
        description="Identifies and corrects coding errors.",
        icon="debugging.svg",
        cost=1.00,
        example_prompts=[
            "Find and fix errors in this JavaScript code.",
            "Debug this Python script for syntax issues."
        ],
        providers=["huggingface", "deepseek"],
        ad_duration=60,
        credits=1.00,
        ad_reward=1
    ),
    Tool(
        id="ai-quiz-generator",
        name="AI Quiz Generator",
        description="Creates quizzes with multiple-choice options.",
        icon="quiz.svg",
        cost=0.40,
        example_prompts=[
            "Generate a quiz on world history.",
            "Create a multiple-choice quiz for a science topic."
        ],
        providers=["huggingface", "deepseek"],
        ad_duration=60,
        credits=0.40,
        ad_reward=1
    ),
    Tool(
        id="ai-poetry-generator",
        name="AI Poetry Generator",
        description="Crafts unique poetry on various themes.",
        icon="poetry.svg",
        cost=0.20,
        example_prompts=[
            "Write a poem about love.",
            "Create a haiku about nature."
        ],
        providers=["huggingface", "openrouter"],
        ad_duration=60,
        credits=0.20,
        ad_reward=1
    ),
    Tool(
        id="ai-meditation-coach",
        name="AI Meditation Coach",
        description="Guides users through relaxation exercises.",
        icon="meditation.svg",
        cost=1.00,
        example_prompts=[
            "Guide a user through a breathing exercise.",
            "Provide a meditation session for stress relief."
        ],
        providers=["huggingface", "replicate"],
        ad_duration=60,
        credits=1.00,
        ad_reward=1
    )
]

def get_tool_by_id(tool_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a tool by its ID."""
    for tool in TOOLS:
        if tool.id == tool_id:
            return tool.get_info()
    return None

if not TOOLS:
    print("No tools are available to display.")