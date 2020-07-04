# Currency

This project aims to convert portuguese numbers written in full or numerically.

## Usage

To use this code into your project, clone it into a folder (`external_libs` for example).

Install `requirements.txt`.

```pip install -r requirements.txt```

Import `src` directory contents.

### Exemplo

````python
from external_libs.currency.src import number_to_text
from external_libs.currency.src import text_to_number
print(number_to_text(0))
# zero
print(text_to_number("cem reais"))
# 100.0
print(text_to_number("cem mil trezentos e cinquenta reais e vinte um centavo"))
# 100350.21
```