# Currency

This project aims to convert portuguese numbers written in full or numerically.

## Usage

Para utilizar dentro do seu projeto clone o projeto dentro de uma pasta (`external_libs` pro exemplo).
Faça a instalação do `requirements.txt`.
```pip install -r requirements.txt```
Importe o conteúdo do diretório `src`

### Exemplo

--------
from external_libs.currency.src import number_to_text
from external_libs.currency.src import text_to_number
print(number_to_text(0))
# zero
print(text_to_number("cem reais"))
# 100.0
print(text_to_number("cem mil trezentos e cinquenta reais e vinte um centavo"))
# 100350.21
--------