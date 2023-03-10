from regex_construtor import Flags, RegexConstrutor

rc = RegexConstrutor()

# Exemplo: CPF Simples - 000.000.000-00 ou 11111111111
print(
    (
        rc.exatamente_n(3, rc.tipos.numero)
        .zero_ou_um('.')
        .exatamente_n(3, rc.tipos.numero)
        .zero_ou_um('.')
        .exatamente_n(3, rc.tipos.numero)
        .zero_ou_um('-')
        .exatamente_n(2, rc.tipos.numero)
        .construir(Flags.ASCII)
    ).findall(
        """
    Esse é um CPF com pontuação: 000.000.000-00;
    Já esse, não tem rs: 11111111111;
    E esse tem simbolos invalidos: 222-222-222.22;
"""
    )
)
# Saida: RegexBuilder::debug --> re.compile('\\d{3}.?\\d{3}.?\\d{3}-?\\d{2}', re.ASCII)
#        ['000.000.000-00', '11111111111']


# Exemplo: intervalo
print(
    (
        rc.um_ou_mais(rc.tipos.intervalo(1, 5))
        .termina_com('a')
        .construir(Flags.MULTILINE)
    ).findall(
        """
        111a

        as[a]5555a
        """
    )
)
# Saida: RegexBuilder::debug --> re.compile('[1-5]+a$', re.MULTILINE)
#        ['111a', '5555a']
