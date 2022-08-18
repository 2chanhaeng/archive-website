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


def get_path(browser:str|int=default_browser, update:bool=False, path:str=default_path) -> str:
    if type(browser) is int:
        browser = int_to_browser(browser)
    drivers_path:str = path + "/drivers.json"
    if not os.path.exists(drivers_path):
        with open(drivers_path, 'w') as store:
            store.write("{}")
    with open(drivers_path, 'r') as store:
        drivers:Dict[str,str] = json.loads(store.read())
    if update or browser not in drivers:
        drivers[browser] = install()
        with open(drivers_path, 'w') as store:
            json.dump(drivers, store, indent=2)
    return drivers[browser]
