
import ast
import os
import sys
import logging
import time
import platform
import re
import webbrowser

try:
    from pygments import highlight
    from pygments.lexers import PythonLexer, JavascriptLexer, HtmlLexer, CppLexer, TypeScriptLexer
    from pygments.formatters import TerminalFormatter
except ImportError:
    print("Pygments not installed. Run 'pip install pygments' for syntax highlighting.")
    highlight = None

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("Colorama not installed. Run 'pip install colorama' for colored output.")
    class Fore:
        RED = GREEN = YELLOW = CYAN = MAGENTA = BLUE = LIGHTCYAN_EX = RESET = ''
    class Style:
        BRIGHT = RESET_ALL = ''

logging.basicConfig(filename='translation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def print_banner():
    banner = f"""
{Fore.BLUE}{Style.BRIGHT}
╔════════════════════════════════════════════╗
║        Sinthiya's Multi-Lang Translator     ║
╚════════════════════════════════════════════╝
{Fore.LIGHTCYAN_EX}         Empowering Code Across Borders
{Style.RESET_ALL}
"""
    print(banner)

def print_credit():
    credit_box = f"""
{Fore.CYAN}{Style.BRIGHT}
+-------------------------------------------------------------+
|                                                             |
|           Developed & Maintained by {Fore.YELLOW}Sinthiya{Fore.CYAN}                 |
|                                                             |
|    GitHub   : {Fore.GREEN}https://github.com/SinthuChan{Fore.CYAN}                        |
|    Email    : {Fore.GREEN}trytohack15@gmail.com{Fore.CYAN}                             |
|    Facebook : {Fore.GREEN}Sinthiya Chowdhury{Fore.CYAN}                              |
|                                                             |
|  © 2025 Sinthiya - All rights reserved                      |
+-------------------------------------------------------------+
{Style.RESET_ALL}
"""
    print(credit_box)

# Dummy translate functions for brevity
def translate_py_to_js(code): return "// JS Code for: " + code
def translate_js_to_py(code): return "# Python Code for: " + code
def translate_js_to_ts(code): return "// TS Code for: " + code
def translate_ts_to_js(code): return "// JS Code (from TS): " + code
def translate_html_to_jsx(code): return code.replace('class=', 'className=')
def translate_jsx_to_html(code): return code.replace('className=', 'class=')
def translate_cpp_to_py(code): return "# Python (from C++): " + code
def translate_py_to_cpp(code): return "// C++ Code for: " + code + "\n}"

def highlight_code(code, lexer):
    return highlight(code, lexer, TerminalFormatter()) if highlight else code

def get_code_from_user():
    while True:
        print("\nChoose input method:")
        print("1. Write/Paste code")
        print("2. Provide path to a code file")
        print("3. Exit")
        choice = input(Fore.YELLOW + "Enter choice (1, 2 or 3): " + Fore.RESET).strip()

        if choice == '1':
            print(Fore.GREEN + "\nEnter your code (type 'END' alone on a line to finish):" + Fore.RESET)
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            return "\n".join(lines)
        elif choice == '2':
            path = input(Fore.YELLOW + "Enter full path to code file: " + Fore.RESET).strip()
            if not os.path.isfile(path):
                print(Fore.RED + f"File not found: {path}" + Fore.RESET)
                continue
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                print(Fore.RED + f"Error reading file: {e}" + Fore.RESET)
        elif choice == '3':
            print(Fore.CYAN + "Exiting input section." + Fore.RESET)
            return ""
        else:
            print(Fore.RED + "Invalid choice. Try again." + Fore.RESET)

def main():
    clear_screen()
    print_banner()
    print_credit()

    translators = {
        '1': (translate_py_to_js, PythonLexer(), JavascriptLexer()),
        '2': (translate_js_to_py, JavascriptLexer(), PythonLexer()),
        '3': (translate_js_to_ts, JavascriptLexer(), TypeScriptLexer()),
        '4': (translate_ts_to_js, TypeScriptLexer(), JavascriptLexer()),
        '5': (translate_html_to_jsx, HtmlLexer(), JavascriptLexer()),
        '6': (translate_jsx_to_html, JavascriptLexer(), HtmlLexer()),
        '7': (translate_cpp_to_py, CppLexer(), PythonLexer()),
        '8': (translate_py_to_cpp, PythonLexer(), CppLexer()),
    }

    while True:
        print("\nChoose translation direction:")
        print("1. Python → JavaScript")
        print("2. JavaScript → Python")
        print("3. JavaScript → TypeScript")
        print("4. TypeScript → JavaScript")
        print("5. HTML → JSX")
        print("6. JSX → HTML")
        print("7. C++ → Python")
        print("8. Python → C++")
        print("9. Exit")
        print("10. Contact Developer")

        direction = input(Fore.YELLOW + "Enter choice (1-10): " + Fore.RESET).strip()

        if direction == '9':
            print(Fore.CYAN + "Thanks for using the translator. Goodbye!" + Fore.RESET)
            break
        elif direction == '10':
            print(Fore.CYAN + "Opening Sinthiya's Facebook profile..." + Fore.RESET)
            webbrowser.open("https://www.facebook.com/Myloveayan")
            continue

        if direction not in translators:
            print(Fore.RED + "Invalid choice. Try again." + Fore.RESET)
            continue

        func, in_lexer, out_lexer = translators[direction]
        code = get_code_from_user()
        if not code.strip():
            continue

        clear_screen()
        print_banner()
        print_credit()

        print(Fore.LIGHTCYAN_EX + "\nOriginal Code:\n" + Fore.RESET)
        print(highlight_code(code, in_lexer))

        print(Fore.YELLOW + "\nTranslating..." + Fore.RESET)
        time.sleep(1)

        translated = func(code)

        print(Fore.LIGHTGREEN_EX + "\nTranslated Code:\n" + Fore.RESET)
        print(highlight_code(translated, out_lexer))

if __name__ == "__main__":
    main()
