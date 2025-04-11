#Using composing create pipline to achive given formating
# ">> hi world! <<" #Original "    hello WORLD!    "

#Choose your composition well (>ᴗ•)
# https://github.com/SoliGabiAnn/Functional-programming-course/wiki/07.-Composing

def to_lower(text):
    return text.lower()

def to_upper(text):
    return text.upper()

def strip_whitespace(text):
    return text.strip()

def replace(sub, repl):
    return lambda text: text.replace(sub, repl)

def add_prefix(prefix):
    return lambda text: f"{prefix}{text}"

def add_suffix(suffix):
    return lambda text: f"{text}{suffix}"

def title_case(text):
    return text.title()

text_pipeline = #Your code here

input_text = "   Hello WORLD!   "
formatted = text_pipeline(input_text)
print(formatted)  # Output: >> hi world! <<




