from regex_builder import Flags, RegexBuilder, Types

rb = RegexBuilder()

print(
    (rb.begins_with('a').contain(Types.any).ends_with('b'))
    .build(Flags.IGNORECASE)
    .findall('a0b')
)
