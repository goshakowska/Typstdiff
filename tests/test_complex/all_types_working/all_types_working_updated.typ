  GNU nano 6.2                        test1.typ                              
= Introduction
In this report, we will explore the
various factors that influence _fluid
dynamics_ in glaciers and how they
contribute to the changed and
behaviour of these natural structures.

+ The climate3
  - Temperature2
  - Precipitation2
+ The topography
+ The geology2

// Obrazek z podpisem zapisane w figurze działa
// #figure(
//   image("doggo.jpg", width: 70%),
//   caption: [
//     _Dog_ form an important part
//     of the earth's climate system.
//   ],
// )

The equation $Q = rho A v + C$
defines the glacial flow rate.

The flow rate of a glacier is
defined by the following equation:

$ Q = rho A v + C $

The flow rate of a glacier is given
by the following equation:

$ Q = rho A v + "time offset" $

Total displaced soil by glacial flow:

#underline($ 7.32 beta +
  sum_(i=0)^nabla Q_i / 2 $)

Total displaced changed by glacial flow:

$ 7.32 beta +
  sum_(i=0)^nabla
    (Q_i (a_i - epsilon)) / 2 $

    
$ v := vec(x_1, x_2, x_3) $

$ a arrow.squiggly b $

#lorem(2)


// Działa, ale po konwersji przed i po logo+słowo jest nowa linia

// #show "ArtosFlow": name => box[
//   #box(image(
//     // "logo.svg",
//     height: 0.7em,
//   ))
//   #name
// ]

// This report is embedded in the
// ArtosFlow project. ArtosFlow is a
// project of the Artos Institute.





/* SYNTAX */


/* MODES */
Number: #(1 + 2)

$-x$ is the opposite of $x$

let name = [*Typst!*]


/* MARKUP */

*strongABC*

_emphasis_

`print(1)`

https://typst.app/

<intro>

https://another.app/

= Heading

- item

+ item

/ Term: description

$x^2$

'single' or "double"

~, ---


/* MATH MODE */

$x^2$

$ x^2 $

$x_1$

$x^2$

$1 + (a+b)/5$

$x \ y$

$x &= 2 \ &= 3$

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
It explains #name.

#let add(x, y) = x + y
Sum is #add(2, 3).


// krotki, listy, słowniki
#let (x, y) = (1, 2)
The coordinates are #x, #y.

#let (a, .., b) = (1, 2, 3, 4)
The first element is #a.
The last element is #b.

#let books = (
  Shakespeare: "Hamlet",
  Homer: "The Odyssey2",
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
#if 1 < 2 [
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
        Dobrze 
] else [
        Niedobrze  
]



*Date:* 26.12.2022 \
*Topic:* Infrastructure Test \
*Severity:* High \

#lower("ABC") \
#lower("AAAAAA") \
#lower[*My Text*] \
#lower[already low]


```typc
let f(x) = x
code = "centered"
```

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

#upper("abc") \
#upper("def") \
#upper[*my text*] \
#upper[ALREADY HIGH]
