from regex_construtor import Flags, RegexConstrutor, Tipos

rc = RegexConstrutor()

# CPF Simples - 000.000.000-00
print(
    (
        rc.exatamente_n(3, Tipos.numero)
        .zero_ou_um('.')
        .exatamente_n(3, Tipos.numero)
        .zero_ou_um('.')
        .exatamente_n(3, Tipos.numero)
        .zero_ou_um('-')
        .exatamente_n(2, Tipos.numero)
    )
    .construir(Flags.ASCII)
    .findall('000.000.000-00')
)
