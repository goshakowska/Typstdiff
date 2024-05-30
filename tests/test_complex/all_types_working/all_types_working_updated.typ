GNU nano 6.2                        test1.typ                              
= CHANGED
In this CHANGED, we will explore the
various factors that influence _fluid
dynamics_ in glaciers and how they
contribute to the formation and
behaviour SOMETHING NEW.

The equation $Q = rho A v + C$
defines the glacial flow rate.

The flow CHANGED of a glacier is
defined by the following equation:

$ Q = rho A v + C $

The flow rate of a CHANGED is given
by the following equation:

$ Q = rho A v + "time CHANGED" $

Total displaced soil by glacial flow:
$ 7.32 beta +
  sum_(i=0)^nabla
    (Q_i (a_i - epsilon)) / 3 $

    
$ v := vec(x_1, x_2, x_2) $

$ a arrow.squiggly b $

#lorem(20)

/* MODES */
Number: #(1 + 5)

$-x$ is the opposite of $x$

let name = [*Typst NEW!*]

/* MARKUP */

*strong*

`print(1)`

https://typst.app/

<intro>

= Heading


$x^2$

'single' or "double"

~, ---

/* MATH MODE */

$x^3$

$ x^2 $

$x_5$

$x^2$

$1 + (a+b)/5$

$x \ y$

$x &= 5 \ &= 3$

$pi$

$arrow.r.long$\

$x y$

$->, !=$

$a "is natural"$

$floor(x)$




#lorem(30)

/* SCRIPTING */
#emph[Hello] \
#"hello".len()

// proste zmienne w bloku
#{
  let a = [from]
  let b = [*world*]
  [hello ]
  a + [ the ] + b
}

// zmienne i funkcje
#let name = "Typst"
This is #name's documentation.
It CHANGED #name.

#let add(x, y) = x + y
Sum is #add(2, 3).


// krotki, listy, słowniki
#let (x, y) = (1, 2)
The CHANGED are #x, #y.

#let (a, .., b) = (5, 2, 3, 4)
The CHANGED element is #a.
The last element is #b.

#let books = (
  Shakespeare: "Hamlet",
  Homer: "The Odyssey",
  Austen: "Persuasion",
)

#let (Austen,) = books
Austen wrote #Austen.

#let (Homer: h) = books
Homer wrote #h.

// zmienne _
#let (_, y, _) = (1, 2, 3)
The y coordinate is #y.

// zip zmiennych i wywołanie funkcji na wartościach
// dobrze formatuje, ale typst automatycznie dodaje kolor, więc trochę działa i trochę nie
#let left = (2, 4, 5)
#let right = (3, 2, 6)
#left.zip(right).map(
  ((a,b)) => a + b
)

// instrukcje warunkowe
#if 1 < 3 [
  This is shown
] else [
  This is not.
]

// pętla for z break (dobrze formatuje jedynie litery jak w przykładzie)
// dłuższy tekst - dodaje nową linię
// liczby - nie zachowuje kolorowania typsta
#for letter in "abc nope" {
  if letter == " " {
    break
  }

  letter
}

// słowniki i body zmiennej działa
#let dict = (greet: "Hello")
#dict.greet \

#let it = [= Heading]
#it.body \

// metody na tekście
3 is the same as
#"abc".len()

// metody na konkretnych zmiennych
#let array = (1, 2, 3, 4)
#array.pop() \
#array.len() \

#("a, b, c"
    .split(", ")
    .join[ --- ])


// Wszystkie operatory działają
#if 3 in (1, 2, 3) [
        CHANGED 
] else [
        Niedobrze  
]

*Date:* 26.12.2022 \
*Topic:* Infrastructure Test \
*Severity:* High \

#lower("ABC") \
#lower[*CHANGED*] \
#lower[already low]

#upper("CHANGED") \
#upper[*my text*] \
#upper[ALREADY HIGH]


"This is in quotes."

#set text(lang: "de")
"Das ist in Anführungszeichen."

#set text(lang: "fr")
"C'est entre guillemets."

1#super[st] try!

#text(font: "Linux Libertine", style: "italic")[Italic]
#text(font: "DejaVu Sans", style: "oblique")[Oblique]


This is #underline[important].

Take #underline(
  stroke: 1.5pt + red,
  offset: 2pt,
  [care],
)