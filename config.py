from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Security: set this in both the ML service and the Next.js app.
    ml_service_secret: str

    # Comma-separated allowed origins. Example:
    # https://your-next-app.onrender.com,https://your-domain.com
    cors_origins: str = "*"

    # Redis: optional cache. If unavailable, recommendations still work.
    redis_url: str = "redis://redis:6379"
    cache_ttl_seconds: int = 3600

    # Data paths
    data_path: str = "data/books_with_emotions.csv"
    chroma_persist_dir: str = "./chroma_db"

    # Embedding model
    embedding_model: str = "all-MiniLM-L6-v2"

    # Recommendation defaults
    default_initial_top_k: int = 50
    default_final_top_k: int = 16
    oversample_multiplier: int = 4

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
