"1. Si r = 10, s = 0, resolver mostrando el orden de los pasos la siguiente expresión lógica:"

"(r != 10) or not (s == -r) or not((True or r >= 10) and not (s <= 0 and True))"
" false    or       true    or not(true and false)"
"false      or      true    or true"
"true or true"
"true"

r=10;
s=0;

verificacion= (r != 10) or not (s == -r) or not((True or r >= 10) and not (s <= 0 and True));
print(verificacion);