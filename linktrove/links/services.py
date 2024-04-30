from metadata_parser import MetadataParser
from urllib.parse import urlparse

FAKE_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"


def extract_metadata(url: str) -> tuple[str, str | None, str | None, str | None]:
    # add a fake user agent and lang to simulate a request from a web browser
    url_headers = {"User-Agent": FAKE_USER_AGENT, "Accept-Language": ACCEPT_LANGUAGE}

    try:
        page = MetadataParser(
            url=url,
            url_headers=url_headers,
            support_malformed=True,
            force_doctype=True,
            search_head_only=False,
        )
    except Exception:
        return url, None, None, None

    titles = page.get_metadatas("title")
    descriptions = page.get_metadatas("description")
    images = page.get_metadatas("image")

    title = titles[0] if titles else url
    description = descriptions[0] if descriptions else None
    thumbnail = images[0] if images else None

    favicon_links = page.soup.find_all("link", rel="icon")
    favicon_links.extend(page.soup.find_all("link", rel="shortcut icon"))
    favicon_url = None
    if favicon_links:
        favicon_url = favicon_links[0].get("href")
        if not favicon_url.startswith("http"):
            parsed_url = urlparse(url)
            without_leading_slash = (
                favicon_url[1:] if favicon_url.startswith("/") else favicon_url
            )
            favicon_url = "{scheme}://{domain}/{icon}".format(
                scheme=parsed_url.scheme,
                domain=parsed_url.netloc,
                icon=without_leading_slash,
            )

    return title, description, thumbnail, favicon_url
