DEFAULT_CONFIG = {
    "agent_llm_model": "gemma-4-26b-a4b",
    "graph_llm_model": "gemma-4-26b-a4b",
    "agent_llm_provider": "lm_studio",  # "openai", "anthropic", "qwen", "minimax", "minimax_cn", or "lm_studio"
    "graph_llm_provider": "lm_studio",  # "openai", "anthropic", "qwen", "minimax", "minimax_cn", or "lm_studio"
    "agent_llm_temperature": 0.1,
    "graph_llm_temperature": 0.1,
    "api_key": "sk-",  # OpenAI API key
    "anthropic_api_key": "sk-",  # Anthropic API key (optional, can also use ANTHROPIC_API_KEY env var)
    "qwen_api_key": "sk-",  # Qwen API key (optional, can also use DASHSCOPE_API_KEY env var)
    "minimax_api_key": "",  # MiniMax API key (optional, can also use MINIMAX_API_KEY env var)
    "minimax_cn_api_key": "",  # MiniMax CN API key (optional, can also use MINIMAX_CN_API_KEY or MINIMAX_API_KEY env var)
    "lm_studio_api_key": "sk-lm-rAyi0uvK:JjMJVprtC43iUDk3mUZ5",  # LM Studio API key (optional, can also use LM_STUDIO_API_KEY env var)
    "lm_studio_base_url": "" # LM Studio server url. Use OpenAI compatiable url (i.e. http://127.0.0.1:1234/v1)
}
