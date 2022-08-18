if "import":
    if "type hint":
        from typing import Callable
        from bs4 import Tag
        
    if "built-in":
        import os
        from urllib import parse
    
    if "external":
        pass

    if "personal": 
        from fp import curry

__all__ = ["makedirs", "url_to_path", "add_domain", "get_href", "has_href"]

makedirs:Callable[[str], None] = lambda path: os.makedirs(path, exist_ok=True)


def url_to_path(url:str) -> str:
    parsed = parse.urlparse(url)
    return "saved/" + parsed.netloc + parsed.path


@curry
def add_domain(domain:str, path:str) -> str:
    return domain + path if path[0] == "/" else path


def has_href(a:Tag) -> bool:
    return "href" in a.attrs and a.attrs["href"] != ""


def get_href(a:Tag) -> str:
    return a.attrs["href"]
