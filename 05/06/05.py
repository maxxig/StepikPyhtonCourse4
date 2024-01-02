class Strip:
    def __init__(self, chars):
        self.chars = chars
    def __call__(self, string):
        return string.strip(self.chars)

# TEST_4:
from string import punctuation

strip = Strip(punctuation)
words = ['&}:,"@team-..|][', '[${!."language+>}*{@', ')..?(?throughout/?`%%^', '%](+{!dog\\_];]:', "+]@@'?wide[={[&_",
         "<%:#<_director!']>?$", '&__$>.onto#;|~$-', '@,}]).of?/)?=!', '<%@^:}company\'!#("^', '?@.[^|run#<\\~\\[',
         "<|%;#=father<:;@'=", ')\\`-&)street+)(#\\~', '((%/?$enough~\\<{${', '*@;{.@young!(_.:)', '?<;<}&health#!=[~^',
         ".&]+'/learn)-@@)+", "@$,,]/entire;)$'@>", '*"%=+?use#!?#``', '&:|%_+first:@+{}+', '`<&=@.heavy{(}^\\-',
         ":,]'.=argue&(([|/", '*\\|^!|mother_\\$,]_', '\'>\'@|@owner";\\)}.', '~+=+=%new?]]_!.', '<&{+$@check|\\;[*[',
         '([*;;^explain%(~"]^', ')|,){+late.,"%,(', '|~\\-{:movie.,~/}\\', ')%*=}?card<{^`>|', '$!,<+)raise+,<{<%',
         '#?:=!}direction>`\'"#*', '!/|)()article_/]),,', ']\'"=.-trouble#%\\*%$', "}^={=\\happen!)]':^",
         '`://..move)),%-&', '*`=;>.anyone&-`</,', "}^`{%'near@.+,{&", '%/<*;>short-&{*<-', '^&&(^!really=;?{`"',
         '^,=}!=check\\{*-!`', '_=?[*`management/(:)?,', '![]_]/boy$-@`&:', '.):\\,}or?]$?;*', '\\^.{:@very=@!!]=',
         '*\\@~+=attack~=>+.)', '%"`/.:available}*<~)@', "*,-\\'~sell-?;>!\\", ',)^["[executive::;_[:',
         '&#:":*up~.{`|$', '+}@_=>floor-`}`~@']

for word in words:
    print(strip(word))