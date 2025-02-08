# crawl4ai-investing

This project is a web crawler that extracts data from investing.com using the `crawl4ai` library. It specifically targets the "Majors" table under the "Markets" section to retrieve the "Name", "Last", and "Chg. %" data for major indices.

## Description

The script uses `crawl4ai` to fetch the HTML content of the specified URL and extract structured data using an LLM extraction strategy. It defines a Pydantic model `OpenAIModelFee` to represent the extracted data, which includes the country flag, name, and last value of each index. The extracted data is then saved to a CSV file.

## Dependencies

The project depends on the following libraries:

- `crawl4ai`: The core library for web crawling and data extraction.
- `pydantic`: For defining data models.
- `python-dotenv`: For loading environment variables from a `.env` file.
- `aiohttp`: For asynchronous HTTP requests.
- `json`: For parsing JSON data.

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd crawl4ai-investing
```

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set the `OPENROUTER_API_KEY` environment variable. You can do this by creating a `.env` file in the project root directory and adding the following line:

```
OPENROUTER_API_KEY=<your_openrouter_api_key>
```

## Usage

To run the script, execute the following command:

```bash
python main.py
```

The script will fetch the data from investing.com, extract the relevant information, and save it to a CSV file named `complete_indexes.csv`.

## crawl4ai

`crawl4ai` is a powerful web crawling library that simplifies the process of extracting structured data from websites. It provides a high-level API for defining crawling configurations, extracting data using LLMs, and handling various aspects of web crawling, such as caching, pagination, and request throttling.

For more information about `crawl4ai`, please refer to the official documentation: [https://docs.crawl4ai.com/](https://docs.crawl4ai.com/)

## License

This project is licensed under the MIT License.
