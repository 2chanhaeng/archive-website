if "import":
    if "type hint":
        from typing import Callable, Dict
        
    if "built-in":
        import os
        import json
    
    if "external":
        from webdriver_manager.firefox import GeckoDriverManager
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.opera import OperaDriverManager

    if "personal": 
        from util import makedirs

default_path:str = "venv/driver/"
default_browser:str = "firefox"
int_to_browser:Callable[[int],str] = ["firefox", "chrome", "opera"].__getitem__


def install(browser, path:str=default_path) -> str:
    makedirs(path)
    match browser:
        case "firefox":
            return GeckoDriverManager(path=path).install()
        case "chrome":
            return ChromeDriverManager(path=path).install()
        case "opera":
            return OperaDriverManager(path=path).install()
        case wrong:
            sub = input(
                f"{wrong} is not brower.\n" +
                f"Install {default_browser} except {wrong}?\n" +
                f"y: {default_browser} f: Firefox, c: Chrome, o: Opera, n: Cancel install\n"
            )
            if sub == "n":
                raise "User cancels install driver."
            return {
                "f":install("firefox", path),
                "c":install("chrome", path),
                "o":install("opera", path),
                "y":install(default_browser, path),
            }[sub]
