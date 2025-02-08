import os
import asyncio
import json
from models import Index
from data_utils import save_to_csv
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from dotenv import load_dotenv

load_dotenv()

async def extract_structured_data_using_llm(
    provider: str, api_token: str = None, extra_headers: dict[str, str] = None
):
    print(f"\n--- Extracting Structured Data with {provider} ---")

    if api_token is None and provider != "ollama":
        print(f"API token is required for {provider}. Skipping this example.")
        return

    browser_config = BrowserConfig(headless=True)

    extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000}
    if extra_headers:
        extra_args["extra_headers"] = extra_headers

    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        word_count_threshold=1,
        page_timeout=80000,
        extraction_strategy=LLMExtractionStrategy(
            provider=provider,
            api_token=api_token,
            schema=Index.model_json_schema(),
            extraction_type="schema",
            instruction="""From the crawled content, extract all items on the table. Get names along with their flags (country) and last value. 
            Do not miss any models in the entire content.""",
            extra_args=extra_args,
        ),
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.investing.com/indices/major-indices", config=crawler_config
        )
        print(f"\n--- Results started ---")
        # Parse the JSON string into a list of dictionaries
        try:
            data = json.loads(result.extracted_content)
            save_to_csv(data, "complete_indexes.csv")
            print(f"\n--- Results finished ---")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Use ollama with llama3.3
    asyncio.run(
        extract_structured_data_using_llm(
            provider="openrouter/google/gemini-2.0-flash-001", api_token=os.getenv("OPENROUTER_API_KEY")
        )
    )
