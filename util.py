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
