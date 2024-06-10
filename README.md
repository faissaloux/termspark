![Logo](https://raw.githubusercontent.com/faissaloux/termspark/main/.github/art/logo.png)

[![Test Python package](https://github.com/faissaloux/termspark/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/faissaloux/termspark/actions/workflows/tests.yml) [![codecov](https://codecov.io/gh/faissaloux/termspark/branch/main/graph/badge.svg)](https://codecov.io/gh/faissaloux/termspark) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/faissaloux/termspark/main.svg)](https://results.pre-commit.ci/latest/github/faissaloux/termspark/main) ![PyPI](https://img.shields.io/pypi/v/termspark) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/termspark) ![PyPI - Status](https://img.shields.io/pypi/status/termspark)

# Installation
```bash
    pip install termspark
```

# Usage

- [`print()`](#print-but-more)
- [`input()`](#input)
- [`line()`](#line)
- [paint](#you-can-use-different-styles-on-same-position)
- [`raw()`](#raw)
- [force Width](#force-width)
- [max width](#set-content-max-width)
- [`full_width()`](#full-width)
- [separator](#separator)
- [`Termspark().line()`](#line-1)
- [style](#style)
- [hyperlinks](#hyperlinks)
- [supported colors](#supported-colors)

### `print()`, but more!
Import Termspark's print and take advantage of all its features, [colors](#you-can-also-paint-your-content), [highlights](#you-can-also-paint-your-content), [styles](#style), [hyperlinks](#hyperlinks) and more ...

```python
from termspark import print

print(" Termspark ", "white", "blue", "italic")
print(" [@termspark](https://github.com/faissaloux/termspark) ", "black", "white", "italic, bold")
```
![](https://github.com/faissaloux/termspark/assets/60013703/2fcdf8c7-dca6-4bb7-9557-e307173c5ab2)

You can choose from `["left", "center", "right"]` to specify where to print by passing it as position parameter:
`print(" Termspark ", position="center")`.

You can enable the Full Width using full_width parameter:
`print(" Termspark ", highlight="blue", full_width=True)`.

You can fill the empty space by a character using `print(separator=)`.

```python
from termspark import print

print(" TERMSPARK ", "white", "green", position="center", separator="_")
```
![](https://github.com/faissaloux/termspark/assets/60013703/b6c38ae1-ec25-4abb-a078-1309c3234a62)

### `input()`

input with colors, highlights, styles, and hyperlinks.

With `input(position=)` you can specify position where to put your input text `["left", "center", "right"]`.
With `input(full_width=)` you can enable full width `True | False`.

```python
from termspark import input

name = input(" What's your name? ", "white", "blue", "italic", "center", True)
```
![](https://github.com/faissaloux/termspark/assets/60013703/8077eb19-07b5-4f32-b1bb-b00be7860eba)


#### Input Type
You can specify the input type by passing it to the `type=` parameter.

For a calculation example, to pass the input value into a calculation you don't need to convert it to `int`  anymore, you just need to set it from `type` argument 🥳 .
```python
from termspark import input

birthyear = input(" Your year birth? ", "white", "blue", type=int)
print(f"Your age is: {2023 - birthyear}")
```

#### Input Callback
the `input()` supports callback too.

If you need to pass the input value into some function before returning the result, you need to pass it into the `callback=` argument.

```python
from termspark import input

def age_calc(birthyear, currentyear=2023):
    return currentyear - birthyear

age = input(" Your year birth? ", "white", "blue", type=int, callback=age_calc)
print(f"Your age is: {age}")
```

You can use separator in `input(separator=)` too.

```python
from termspark import input

name = input(" What's your name?", "white", "blue", position="left", separator=".")
```
![](https://github.com/faissaloux/termspark/assets/60013703/b4a4f5b0-ff55-4079-8a82-a6c5a0ba0973)

### `line()`
To print empty line use `line()`, you can leave it empty or fill it with a repeated character, you can specify its color too.

```python
from termspark import line

line(".", "blue")
line(highlight="green")
line()
line("-")
```
![](https://github.com/faissaloux/termspark/assets/60013703/210a5778-e7c8-4031-a49f-6f09f41dc23e)

## More control
```python
    from termspark import TermSpark

    TermSpark().print_right('RIGHT').spark()
    TermSpark().spark_right('RIGHT').spark()
    TermSpark().print_left('LEFT').spark()
    TermSpark().spark_left('LEFT').spark()
    TermSpark().print_center('CENTER').spark()
    TermSpark().spark_center('CENTER').spark()
    TermSpark().line('.').spark()

    TermSpark().print_left('LEFT').print_right('RIGHT').set_separator('.').spark()
    TermSpark().print_left('LEFT').print_center('CENTER').print_right('RIGHT').set_separator('.').spark()
    TermSpark().spark_left('LEFT').spark_center('CENTER').spark_right('RIGHT').set_separator('.').spark()
```

> [!NOTE]
> Separator can contain only one character.

### You can also paint your content
#### text color

```python
    from termspark import TermSpark

    TermSpark().print_right('RIGHT', 'blue').spark()
    TermSpark().print_left('LEFT', 'light red').spark()
    TermSpark().print_center('CENTER', 'light_green').spark()
```

#### background color

```python
    from termspark import TermSpark

    TermSpark().print_right('RIGHT', None, 'light_magenta').spark()
    TermSpark().print_left('LEFT', 'red', 'white').spark()
    TermSpark().print_center('CENTER', 'white', 'light blue').spark()
```

### You can use different styles on same position
```python
    from termspark import TermSpark

    TermSpark().spark_left([' * ', 'gray', 'white'], [' Info ', 'white', 'blue']).spark()
    TermSpark().spark_center([' * ', 'gray', 'white'], [' Warning ', 'white', 'yellow']).spark()
    TermSpark().spark_right([' * ', 'gray', 'white'], [' Error ', 'white', 'red']).spark()
```
`You know you can use them all together 😉`

### Lines are too long to write a termspark line! 😑
```python
    from termspark import TermSpark

    TermSpark().spark_left([' * ', 'gray', 'white'], [' Info ', 'white', 'blue']).spark_center([' * ', 'gray', 'white'], [' Warning ', 'white', 'yellow']).spark_right([' * ', 'gray', 'white'], [' Error ', 'white', 'red']).spark()
```
#### You can separate them by calling each function in a line 🤤
```python
    from termspark import TermSpark

    termspark = TermSpark()
    termspark.spark_left([' * ', 'gray', 'white'], [' Info ', 'white', 'blue'])
    termspark.spark_center([' * ', 'gray', 'white'], [' Warning ', 'white', 'yellow'])
    termspark.spark_right([' * ', 'gray', 'white'], [' Error ', 'white', 'red'])
    termspark.spark()
```
#### Still too long 🙄 Got you 🤩
```python
    from termspark import TermSpark

    termspark = TermSpark()
    termspark.spark_left([' * ', 'gray', 'white'])
    termspark.spark_left(' Info ', 'white', 'blue')
    termspark.spark_center([' * ', 'gray', 'white'])
    termspark.spark_center([' Warning ', 'white', 'yellow'])
    termspark.spark_right(' * ', 'gray', 'white')
    termspark.spark_right([' Error ', 'white', 'red'])
    termspark.spark()
```

### Raw
You can print raw version which is colors-code-free so you can print clean text into files for example.

```python
    from termspark import TermSpark

    raw = TermSpark().print_left('LEFT').print_right('RIGHT').set_separator('.').raw()
```

### Force Width
You can customize width instead of the default full terminal width.

```python
    from termspark import TermSpark

    TermSpark().set_width(40).print_left("LEFT", "red").print_right("RIGHT", "blue").spark()
```

### Set content max width
You can specify max width of content depending on position using `max_[position](max_characters)`.
```python
    from termspark import TermSpark

    termspark = TermSpark()
    termspark.spark_left(["LEFT", "red"])
    termspark.spark_right(["RIGHT", "blue"])
    termspark.max_left(2)
    termspark.max_right(3)
    termspark.spark()
```
This should show only "LE" on the left, and "RIG" on the right.
> [!WARNING]
> `max_[position]()` is only supported by sparkers.

### Full width
You can enable full width by using `full_width()`.

```python
    from termspark import TermSpark

    termspark = TermSpark()
    termspark.spark_center(['Thanks for using Termspark!', 'white', 'green'])
    termspark.full_width()
    termspark.spark()
```
> [!WARNING]
> `full_width()` can only be used with one position.

### Separator
You can add color and highlight to separator too using `set_separator(content, color, highlight)`.
```python
termspark = TermSpark()
termspark.spark_left([' Author ', 'green'])
termspark.spark_right([' Faissal Wahabali ', 'green'])
termspark.set_separator('.', 'green')
termspark.spark()
```
![](https://github.com/faissaloux/termspark/assets/60013703/5cf5039c-66c5-4fbc-9e4a-cb39332a2fb6)

### Line
You can add highlight a line by using `line(highlight=highlight)`.
```python
termspark = TermSpark()
termspark.line(highlight='green')
termspark.spark()
```
![](https://github.com/faissaloux/termspark/assets/60013703/41be7d15-4cab-4f73-a460-89c6d254db78)

### Style
You can style your text by passing it to `print() style parameter` or to `spark([]) fourth list element`.

**Supported styles:**
- bold
- dim
- italic
- overline
- underline
- double underline
- strike through
- blink
- reverse
- hidden

> [!NOTE]
> You can mix styles by separating them by commas.

```python
termspark = TermSpark()
termspark.print_center(' Termspark ', 'green', style='underline, overline, italic')
termspark.full_width()
termspark.spark()
```
![](https://github.com/faissaloux/termspark/assets/60013703/46f4b13d-9d06-4327-85f6-877732b49fba)

### Hyperlinks
You can insert hyperlink using Markdown `[TEXT](LINK)`.
```python
termspark = TermSpark()
termspark.spark_left([" Author ", "green"])
termspark.spark_right([" [@faissaloux](https://github.com/faissaloux) ", "green"])
termspark.set_separator(".", "green")
termspark.spark()
```
![](https://github.com/faissaloux/termspark/assets/60013703/ce829c1a-f14e-419c-80d0-aa202e5608dc)

### Supported colors

| Color	                                                      | Name                | HEX     |
| ----------------------------------------------------------- | ------------------- | ------- |
| ![#000000](https://placehold.it/40x40/000000/FFFFFF?text= ) | black               | #000000 |
| ![#800000](https://placehold.it/40x40/800000/FFFFFF?text= ) | maroon              | #800000 |
| ![#008000](https://placehold.it/40x40/008000/FFFFFF?text= ) | green               | #008000 |
| ![#808000](https://placehold.it/40x40/808000/FFFFFF?text= ) | olive               | #808000 |
| ![#000080](https://placehold.it/40x40/000080/FFFFFF?text= ) | navy                | #000080 |
| ![#800080](https://placehold.it/40x40/800080/FFFFFF?text= ) | purple              | #800080 |
| ![#008080](https://placehold.it/40x40/008080/FFFFFF?text= ) | teal                | #008080 |
| ![#c0c0c0](https://placehold.it/40x40/c0c0c0/FFFFFF?text= ) | silver              | #c0c0c0 |
| ![#808080](https://placehold.it/40x40/808080/FFFFFF?text= ) | gray                | #808080 |
| ![#808080](https://placehold.it/40x40/808080/FFFFFF?text= ) | grey                | #808080 |
| ![#ff0000](https://placehold.it/40x40/ff0000/FFFFFF?text= ) | red                 | #ff0000 |
| ![#00ff00](https://placehold.it/40x40/00ff00/FFFFFF?text= ) | lime                | #00ff00 |
| ![#ffff00](https://placehold.it/40x40/ffff00/FFFFFF?text= ) | yellow              | #ffff00 |
| ![#0000ff](https://placehold.it/40x40/0000ff/FFFFFF?text= ) | blue                | #0000ff |
| ![#ff00ff](https://placehold.it/40x40/ff00ff/FFFFFF?text= ) | fuchsia             | #ff00ff |
| ![#00ffff](https://placehold.it/40x40/00ffff/FFFFFF?text= ) | aqua                | #00ffff |
| ![#ffffff](https://placehold.it/40x40/ffffff/FFFFFF?text= ) | white               | #ffffff |
| ![#00005f](https://placehold.it/40x40/00005f/FFFFFF?text= ) | navy blue           | #00005f |
| ![#000087](https://placehold.it/40x40/000087/FFFFFF?text= ) | dark blue           | #000087 |
| ![#0000af](https://placehold.it/40x40/0000af/FFFFFF?text= ) | dark blue 2         | #0000af |
| ![#0000d7](https://placehold.it/40x40/0000d7/FFFFFF?text= ) | dark blue 1         | #0000d7 |
| ![#005f00](https://placehold.it/40x40/005f00/FFFFFF?text= ) | dark green          | #005f00 |
| ![#005f5f](https://placehold.it/40x40/005f5f/FFFFFF?text= ) | blue stone          | #005f5f |
| ![#005f87](https://placehold.it/40x40/005f87/FFFFFF?text= ) | orient              | #005f87 |
| ![#005faf](https://placehold.it/40x40/005faf/FFFFFF?text= ) | endeavour           | #005faf |
| ![#005fd7](https://placehold.it/40x40/005fd7/FFFFFF?text= ) | science blue        | #005fd7 |
| ![#005fff](https://placehold.it/40x40/005fff/FFFFFF?text= ) | blue ribbon         | #005fff |
| ![#008700](https://placehold.it/40x40/008700/FFFFFF?text= ) | JAPANESE_LAUREL     | #008700 |
| ![#00875f](https://placehold.it/40x40/00875f/FFFFFF?text= ) | DEEP_SEA            | #00875f |
| ![#008787](https://placehold.it/40x40/008787/FFFFFF?text= ) | TURQUOISE           | #008787 |
| ![#0087af](https://placehold.it/40x40/0087af/FFFFFF?text= ) | DEEP_CERULEAN       | #0087af |
| ![#0087d7](https://placehold.it/40x40/0087d7/FFFFFF?text= ) | LOCHMARA            | #0087d7 |
| ![#0087ff](https://placehold.it/40x40/0087ff/FFFFFF?text= ) | AZURE_RADIANCE      | #0087ff |
| ![#00af00](https://placehold.it/40x40/00af00/FFFFFF?text= ) | ISLAMIC_GREEN       | #00af00 |
| ![#00af5f](https://placehold.it/40x40/00af5f/FFFFFF?text= ) | SPRING_GREEN        | #00af5f |
| ![#00af87](https://placehold.it/40x40/00af87/FFFFFF?text= ) | DARK_CYAN           | #00af87 |
| ![#00afaf](https://placehold.it/40x40/00afaf/FFFFFF?text= ) | LIGHT_SEA_GREEN     | #00afaf |
| ![#00afd7](https://placehold.it/40x40/00afd7/FFFFFF?text= ) | CERULEAN            | #00afd7 |
| ![#00afff](https://placehold.it/40x40/00afff/FFFFFF?text= ) | BLUE_BOLT           | #00afff |
| ![#00d700](https://placehold.it/40x40/00d700/FFFFFF?text= ) | ELECTRIC_GREEN      | #00d700 |
| ![#00d75f](https://placehold.it/40x40/00d75f/FFFFFF?text= ) | MALACHITE           | #00d75f |
| ![#00d787](https://placehold.it/40x40/00d787/FFFFFF?text= ) | CARIBBEAN_GREEN     | #00d787 |
| ![#00d7af](https://placehold.it/40x40/00d7af/FFFFFF?text= ) | CYAN_1              | #00d7af |
| ![#00d7d7](https://placehold.it/40x40/00d7d7/FFFFFF?text= ) | DARK_TURQUOISE      | #00d7d7 |
| ![#00d7ff](https://placehold.it/40x40/00d7ff/FFFFFF?text= ) | VIVID_SKY_BLUE      | #00d7ff |
| ![#00ff00](https://placehold.it/40x40/00ff00/FFFFFF?text= ) | ELECTRIC_GREEN_1    | #00ff00 |
| ![#00ff5f](https://placehold.it/40x40/00ff5f/FFFFFF?text= ) | GUPPIE_GREEN        | #00ff5f |
| ![#00ff87](https://placehold.it/40x40/00ff87/FFFFFF?text= ) | SPRING_GREEN_1      | #00ff87 |
| ![#00ffaf](https://placehold.it/40x40/00ffaf/FFFFFF?text= ) | MEDIUM_SPRING_GREEN | #00ffaf |
| ![#00ffd7](https://placehold.it/40x40/00ffd7/FFFFFF?text= ) | SEA_GREEN           | #00ffd7 |
| ![#00ffff](https://placehold.it/40x40/00ffff/FFFFFF?text= ) | CYAN                | #00ffff |
| ![#5f0000](https://placehold.it/40x40/5f0000/FFFFFF?text= ) | ROSEWOOD            | #5f0000 |
| ![#5f005f](https://placehold.it/40x40/5f005f/FFFFFF?text= ) | POMPADOUR           | #5f005f |
| ![#5f0087](https://placehold.it/40x40/5f0087/FFFFFF?text= ) | PIGMENT_INDIGO      | #5f0087 |
| ![#5f00af](https://placehold.it/40x40/5f00af/FFFFFF?text= ) | PURPLE_3            | #5f00af |
| ![#5f00d7](https://placehold.it/40x40/5f00d7/FFFFFF?text= ) | ELECTIC_VIOLET      | #5f00d7 |
| ![#5f00ff](https://placehold.it/40x40/5f00ff/FFFFFF?text= ) | BLUE_VIOLET         | #5f00ff |
| ![#5f5f00](https://placehold.it/40x40/5f5f00/FFFFFF?text= ) | VERDUN_GREEN        | #5f5f00 |
| ![#5f5f5f](https://placehold.it/40x40/5f5f5f/FFFFFF?text= ) | SCORPION            | #5f5f5f |
| ![#5f5f87](https://placehold.it/40x40/5f5f87/FFFFFF?text= ) | COMET               | #5f5f87 |
| ![#5f5faf](https://placehold.it/40x40/5f5faf/FFFFFF?text= ) | SCAMPI              | #5f5faf |
| ![#5f5fd7](https://placehold.it/40x40/5f5fd7/FFFFFF?text= ) | INDIGO              | #5f5fd7 |
| ![#5f5fff](https://placehold.it/40x40/5f5fff/FFFFFF?text= ) | CORNFLOWER_BLUE_1   | #5f5fff |
| ![#5f8700](https://placehold.it/40x40/5f8700/FFFFFF?text= ) | LIMEADE             | #5f8700 |
| ![#5f875f](https://placehold.it/40x40/5f875f/FFFFFF?text= ) | GLADE_GREEN         | #5f875f |
| ![#5f8787](https://placehold.it/40x40/5f8787/FFFFFF?text= ) | JUNIPER             | #5f8787 |
| ![#5f87af](https://placehold.it/40x40/5f87af/FFFFFF?text= ) | HIPPIE_BLUE         | #5f87af |
| ![#5f87d7](https://placehold.it/40x40/5f87d7/FFFFFF?text= ) | HAVELOCK_BLUE       | #5f87d7 |
| ![#5f87ff](https://placehold.it/40x40/5f87ff/FFFFFF?text= ) | CORNFLOWER_BLUE     | #5f87ff |
| ![#5faf00](https://placehold.it/40x40/5faf00/FFFFFF?text= ) | LIMEA               | #5faf00 |
| ![#5faf5f](https://placehold.it/40x40/5faf5f/FFFFFF?text= ) | FERN                | #5faf5f |
| ![#5faf87](https://placehold.it/40x40/5faf87/FFFFFF?text= ) | SILVER_TREE         | #5faf87 |
| ![#5fafaf](https://placehold.it/40x40/5fafaf/FFFFFF?text= ) | TRADEWIND           | #5fafaf |
| ![#5fafd7](https://placehold.it/40x40/5fafd7/FFFFFF?text= ) | SHAKESPEARE         | #5fafd7 |
| ![#5fafff](https://placehold.it/40x40/5fafff/FFFFFF?text= ) | MALIBU              | #5fafff |
| ![#5fd700](https://placehold.it/40x40/5fd700/FFFFFF?text= ) | BRIGHT_GREEN        | #5fd700 |
| ![#5fd75f](https://placehold.it/40x40/5fd75f/FFFFFF?text= ) | PALE_GREEN          | #5fd75f |
| ![#5fd787](https://placehold.it/40x40/5fd787/FFFFFF?text= ) | PASTEL_GREEN        | #5fd787 |
| ![#5fd7af](https://placehold.it/40x40/5fd7af/FFFFFF?text= ) | DOWNY               | #5fd7af |
| ![#5fd7d7](https://placehold.it/40x40/5fd7d7/FFFFFF?text= ) | VIKING              | #5fd7d7 |
| ![#5fd7ff](https://placehold.it/40x40/5fd7ff/FFFFFF?text= ) | STEEL_BLUE          | #5fd7ff |
| ![#5fff00](https://placehold.it/40x40/5fff00/FFFFFF?text= ) | CHARTREUSE          | #5fff00 |
| ![#5fff5f](https://placehold.it/40x40/5fff5f/FFFFFF?text= ) | SCREAMING_GREEN     | #5fff5f |
| ![#5fff87](https://placehold.it/40x40/5fff87/FFFFFF?text= ) | SEA_GREEN_1         | #5fff87 |
| ![#5fffaf](https://placehold.it/40x40/5fffaf/FFFFFF?text= ) | AQUAMARINE_1        | #5fffaf |
| ![#5fffd7](https://placehold.it/40x40/5fffd7/FFFFFF?text= ) | AQUAMARINE_2        | #5fffd7 |
| ![#5fffff](https://placehold.it/40x40/5fffff/FFFFFF?text= ) | AQUAMARINE          | #5fffff |
| ![#870000](https://placehold.it/40x40/870000/FFFFFF?text= ) | DARK_RED            | #870000 |
| ![#87005f](https://placehold.it/40x40/87005f/FFFFFF?text= ) | FRESH_EGGPLANT      | #87005f |
| ![#870087](https://placehold.it/40x40/870087/FFFFFF?text= ) | DARK_MAGENTA        | #870087 |
| ![#8700af](https://placehold.it/40x40/8700af/FFFFFF?text= ) | PURPLE_2            | #8700af |
| ![#8700d7](https://placehold.it/40x40/8700d7/FFFFFF?text= ) | ELECTRIC_VIOLET     | #8700d7 |
| ![#8700ff](https://placehold.it/40x40/8700ff/FFFFFF?text= ) | PURPLE_1            | #8700ff |
| ![#875f00](https://placehold.it/40x40/875f00/FFFFFF?text= ) | BROWN               | #875f00 |
| ![#875f5f](https://placehold.it/40x40/875f5f/FFFFFF?text= ) | COPPER_ROSE         | #875f5f |
| ![#875f87](https://placehold.it/40x40/875f87/FFFFFF?text= ) | STRIKE_MASTER       | #875f87 |
| ![#875faf](https://placehold.it/40x40/875faf/FFFFFF?text= ) | DELUGE              | #875faf |
| ![#875fd7](https://placehold.it/40x40/875fd7/FFFFFF?text= ) | MEDIUM_PURPLE       | #875fd7 |
| ![#875fff](https://placehold.it/40x40/875fff/FFFFFF?text= ) | HELIOTROPE          | #875fff |
| ![#878700](https://placehold.it/40x40/878700/FFFFFF?text= ) | OLIVE_1             | #878700 |
| ![#87875f](https://placehold.it/40x40/87875f/FFFFFF?text= ) | CLAY_CREEK          | #87875f |
| ![#878787](https://placehold.it/40x40/878787/FFFFFF?text= ) | GRAY_1              | #878787 |
| ![#878787](https://placehold.it/40x40/878787/FFFFFF?text= ) | GREY_1              | #878787 |
| ![#8787af](https://placehold.it/40x40/8787af/FFFFFF?text= ) | WILD_BLUE_YONDER    | #8787af |
| ![#8787d7](https://placehold.it/40x40/8787d7/FFFFFF?text= ) | CHETWODE_BLUE       | #8787d7 |
| ![#8787ff](https://placehold.it/40x40/8787ff/FFFFFF?text= ) | LIGHT_SLATE_BLUE    | #8787ff |
| ![#87af00](https://placehold.it/40x40/87af00/FFFFFF?text= ) | LIMEADE_1           | #87af00 |
| ![#87af5f](https://placehold.it/40x40/87af5f/FFFFFF?text= ) | CHELSEA_CUCUMBER    | #87af5f |
| ![#87af87](https://placehold.it/40x40/87af87/FFFFFF?text= ) | BAY_LEAF            | #87af87 |
| ![#87afaf](https://placehold.it/40x40/87afaf/FFFFFF?text= ) | GULF_STREAM         | #87afaf |
| ![#87afd7](https://placehold.it/40x40/87afd7/FFFFFF?text= ) | POLO_BLUE           | #87afd7 |
| ![#87afff](https://placehold.it/40x40/87afff/FFFFFF?text= ) | MALIBU_1            | #87afff |
| ![#87d700](https://placehold.it/40x40/87d700/FFFFFF?text= ) | PISTACHIO           | #87d700 |
| ![#87d75f](https://placehold.it/40x40/87d75f/FFFFFF?text= ) | DARK_OLIVE_GREEN    | #87d75f |
| ![#87d787](https://placehold.it/40x40/87d787/FFFFFF?text= ) | FEIJOA              | #87d787 |
| ![#87d7af](https://placehold.it/40x40/87d7af/FFFFFF?text= ) | VISTA_BLUE          | #87d7af |
| ![#87d7d7](https://placehold.it/40x40/87d7d7/FFFFFF?text= ) | BERMUDA             | #87d7d7 |
| ![#87d7ff](https://placehold.it/40x40/87d7ff/FFFFFF?text= ) | ANAKIWA             | #87d7ff |
| ![#87ff00](https://placehold.it/40x40/87ff00/FFFFFF?text= ) | CHARTREUSE_1        | #87ff00 |
| ![#87ff5f](https://placehold.it/40x40/87ff5f/FFFFFF?text= ) | LIGHT_GREEN         | #87ff5f |
| ![#87ff87](https://placehold.it/40x40/87ff87/FFFFFF?text= ) | MINT_GREEN          | #87ff87 |
| ![#87ffaf](https://placehold.it/40x40/87ffaf/FFFFFF?text= ) | PALE_GREEN_1        | #87ffaf |
| ![#87ffd7](https://placehold.it/40x40/87ffd7/FFFFFF?text= ) | AQUA_MARINE         | #87ffd7 |
| ![#87ffff](https://placehold.it/40x40/87ffff/FFFFFF?text= ) | ANAKIWA_1           | #87ffff |
| ![#af0000](https://placehold.it/40x40/af0000/FFFFFF?text= ) | BRIGHT_RED          | #af0000 |
| ![#af005f](https://placehold.it/40x40/af005f/FFFFFF?text= ) | FLIRT               | #af005f |
| ![#af0087](https://placehold.it/40x40/af0087/FFFFFF?text= ) | MEDIUM_VIOLET_RED   | #af0087 |
| ![#af00af](https://placehold.it/40x40/af00af/FFFFFF?text= ) | MAGENTA_1           | #af00af |
| ![#af00d7](https://placehold.it/40x40/af00d7/FFFFFF?text= ) | DARK_VIOLET         | #af00d7 |
| ![#af00ff](https://placehold.it/40x40/af00ff/FFFFFF?text= ) | PURPLE_4            | #af00ff |
| ![#af5f00](https://placehold.it/40x40/af5f00/FFFFFF?text= ) | ROSE_OF_SHARON      | #af5f00 |
| ![#af5f5f](https://placehold.it/40x40/af5f5f/FFFFFF?text= ) | INDIAN_RED          | #af5f5f |
| ![#af5f87](https://placehold.it/40x40/af5f87/FFFFFF?text= ) | TAPESTRY            | #af5f87 |
| ![#af5faf](https://placehold.it/40x40/af5faf/FFFFFF?text= ) | FUCHSIA_PINK        | #af5faf |
| ![#af5fd7](https://placehold.it/40x40/af5fd7/FFFFFF?text= ) | MEDIUM_PURPLE_1     | #af5fd7 |
| ![#af5fff](https://placehold.it/40x40/af5fff/FFFFFF?text= ) | HELIOTROPE_1        | #af5fff |
| ![#af8700](https://placehold.it/40x40/af8700/FFFFFF?text= ) | PIRATE_GOLD         | #af8700 |
| ![#af875f](https://placehold.it/40x40/af875f/FFFFFF?text= ) | MUESLI              | #af875f |
| ![#af8787](https://placehold.it/40x40/af8787/FFFFFF?text= ) | PHARLAP             | #af8787 |
| ![#af87af](https://placehold.it/40x40/af87af/FFFFFF?text= ) | BOUQUET             | #af87af |
| ![#af87d7](https://placehold.it/40x40/af87d7/FFFFFF?text= ) | LAVENDER            | #af87d7 |
| ![#af87ff](https://placehold.it/40x40/af87ff/FFFFFF?text= ) | HELIOTROPE_2        | #af87ff |
| ![#afaf00](https://placehold.it/40x40/afaf00/FFFFFF?text= ) | GOLD_1              | #afaf00 |
| ![#afaf5f](https://placehold.it/40x40/afaf5f/FFFFFF?text= ) | OLIVE_GREEN         | #afaf5f |
| ![#afaf87](https://placehold.it/40x40/afaf87/FFFFFF?text= ) | HILLARY             | #afaf87 |
| ![#afafaf](https://placehold.it/40x40/afafaf/FFFFFF?text= ) | SILVER_CHALICE      | #afafaf |
| ![#afafd7](https://placehold.it/40x40/afafd7/FFFFFF?text= ) | WISTFUL             | #afafd7 |
| ![#afafff](https://placehold.it/40x40/afafff/FFFFFF?text= ) | MELROSE             | #afafff |
| ![#afd700](https://placehold.it/40x40/afd700/FFFFFF?text= ) | RIO_GRANDE          | #afd700 |
| ![#afd75f](https://placehold.it/40x40/afd75f/FFFFFF?text= ) | CONIFER             | #afd75f |
| ![#afd787](https://placehold.it/40x40/afd787/FFFFFF?text= ) | FEIJOA_1            | #afd787 |
| ![#afd7af](https://placehold.it/40x40/afd7af/FFFFFF?text= ) | PIXIE_GREEN         | #afd7af |
| ![#afd7d7](https://placehold.it/40x40/afd7d7/FFFFFF?text= ) | JUNGLE_MIST         | #afd7d7 |
| ![#afd7ff](https://placehold.it/40x40/afd7ff/FFFFFF?text= ) | ANAKIWA_2           | #afd7ff |
| ![#afff00](https://placehold.it/40x40/afff00/FFFFFF?text= ) | LIME_1              | #afff00 |
| ![#afff5f](https://placehold.it/40x40/afff5f/FFFFFF?text= ) | GREEN_YELLOW        | #afff5f |
| ![#afff87](https://placehold.it/40x40/afff87/FFFFFF?text= ) | MINT_GREEN_1        | #afff87 |
| ![#afffaf](https://placehold.it/40x40/afffaf/FFFFFF?text= ) | DARK_SEA_GREEN      | #afffaf |
| ![#afffd7](https://placehold.it/40x40/afffd7/FFFFFF?text= ) | AERO_BLUE           | #afffd7 |
| ![#afffff](https://placehold.it/40x40/afffff/FFFFFF?text= ) | FRENCH_PASS         | #afffff |
| ![#d70000](https://placehold.it/40x40/d70000/FFFFFF?text= ) | GUARDSMAN_RED       | #d70000 |
| ![#d7005f](https://placehold.it/40x40/d7005f/FFFFFF?text= ) | RAZZMATAZZ          | #d7005f |
| ![#d70087](https://placehold.it/40x40/d70087/FFFFFF?text= ) | HOLLYWOOD_CERISE    | #d70087 |
| ![#d700af](https://placehold.it/40x40/d700af/FFFFFF?text= ) | HOLLYWOOD_CERISE_1  | #d700af |
| ![#d700d7](https://placehold.it/40x40/d700d7/FFFFFF?text= ) | PURPLE_PIZZAZZ      | #d700d7 |
| ![#d700ff](https://placehold.it/40x40/d700ff/FFFFFF?text= ) | ELECTRIC_VIOLET_1   | #d700ff |
| ![#d75f00](https://placehold.it/40x40/d75f00/FFFFFF?text= ) | TENN                | #d75f00 |
| ![#d75f5f](https://placehold.it/40x40/d75f5f/FFFFFF?text= ) | ROMAN               | #d75f5f |
| ![#d75f87](https://placehold.it/40x40/d75f87/FFFFFF?text= ) | CRANBERRY           | #d75f87 |
| ![#d75faf](https://placehold.it/40x40/d75faf/FFFFFF?text= ) | HOPBUSH             | #d75faf |
| ![#d75fd7](https://placehold.it/40x40/d75fd7/FFFFFF?text= ) | ORCHID              | #d75fd7 |
| ![#d75fff](https://placehold.it/40x40/d75fff/FFFFFF?text= ) | MEDIUM_ORCHID       | #d75fff |
| ![#d78700](https://placehold.it/40x40/d78700/FFFFFF?text= ) | MANGO_TANGO         | #d78700 |
| ![#d7875f](https://placehold.it/40x40/d7875f/FFFFFF?text= ) | COPPERFIELD         | #d7875f |
| ![#d78787](https://placehold.it/40x40/d78787/FFFFFF?text= ) | PINK                | #d78787 |
| ![#d787af](https://placehold.it/40x40/d787af/FFFFFF?text= ) | CANCAN              | #d787af |
| ![#d787d7](https://placehold.it/40x40/d787d7/FFFFFF?text= ) | LIGHT_ORCHID        | #d787d7 |
| ![#d787ff](https://placehold.it/40x40/d787ff/FFFFFF?text= ) | HELIOTROPE_3        | #d787ff |
| ![#d7af00](https://placehold.it/40x40/d7af00/FFFFFF?text= ) | CORN                | #d7af00 |
| ![#d7af5f](https://placehold.it/40x40/d7af5f/FFFFFF?text= ) | TACHA               | #d7af5f |
| ![#d7af87](https://placehold.it/40x40/d7af87/FFFFFF?text= ) | TAN                 | #d7af87 |
| ![#d7afaf](https://placehold.it/40x40/d7afaf/FFFFFF?text= ) | CLAM_SHELL          | #d7afaf |
| ![#d7afd7](https://placehold.it/40x40/d7afd7/FFFFFF?text= ) | THISTLE             | #d7afd7 |
| ![#d7afff](https://placehold.it/40x40/d7afff/FFFFFF?text= ) | MAUVE               | #d7afff |
| ![#d7d700](https://placehold.it/40x40/d7d700/FFFFFF?text= ) | CORN_1              | #d7d700 |
| ![#d7d75f](https://placehold.it/40x40/d7d75f/FFFFFF?text= ) | KHAKI               | #d7d75f |
| ![#d7d787](https://placehold.it/40x40/d7d787/FFFFFF?text= ) | DECO                | #d7d787 |
| ![#d7d7af](https://placehold.it/40x40/d7d7af/FFFFFF?text= ) | GREEN_MIST          | #d7d7af |
| ![#d7d7d7](https://placehold.it/40x40/d7d7d7/FFFFFF?text= ) | ALTO                | #d7d7d7 |
| ![#d7d7ff](https://placehold.it/40x40/d7d7ff/FFFFFF?text= ) | FOG                 | #d7d7ff |
| ![#d7ff00](https://placehold.it/40x40/d7ff00/FFFFFF?text= ) | CHARTREUSE_YELLOW   | #d7ff00 |
| ![#d7ff5f](https://placehold.it/40x40/d7ff5f/FFFFFF?text= ) | CANARY              | #d7ff5f |
| ![#d7ff87](https://placehold.it/40x40/d7ff87/FFFFFF?text= ) | HONEYSUCKLE         | #d7ff87 |
| ![#d7ffaf](https://placehold.it/40x40/d7ffaf/FFFFFF?text= ) | REEF                | #d7ffaf |
| ![#d7ffd7](https://placehold.it/40x40/d7ffd7/FFFFFF?text= ) | SNOWY_MINT          | #d7ffd7 |
| ![#d7ffff](https://placehold.it/40x40/d7ffff/FFFFFF?text= ) | OYSTER_BAY          | #d7ffff |
| ![#ff005f](https://placehold.it/40x40/ff005f/FFFFFF?text= ) | ROSE                | #ff005f |
| ![#ff0087](https://placehold.it/40x40/ff0087/FFFFFF?text= ) | DEEP_PINK           | #ff0087 |
| ![#ff00af](https://placehold.it/40x40/ff00af/FFFFFF?text= ) | HOLLYWOOD_CERISE_2  | #ff00af |
| ![#ff00d7](https://placehold.it/40x40/ff00d7/FFFFFF?text= ) | PURPLE_PIZZAZZ_1    | #ff00d7 |
| ![#ff00ff](https://placehold.it/40x40/ff00ff/FFFFFF?text= ) | MAGENTA             | #ff00ff |
| ![#ff5f00](https://placehold.it/40x40/ff5f00/FFFFFF?text= ) | BLAZE_ORANGE        | #ff5f00 |
| ![#ff5f5f](https://placehold.it/40x40/ff5f5f/FFFFFF?text= ) | BITTER_SWEET        | #ff5f5f |
| ![#ff5f87](https://placehold.it/40x40/ff5f87/FFFFFF?text= ) | WILD_WATERMELON     | #ff5f87 |
| ![#ff5faf](https://placehold.it/40x40/ff5faf/FFFFFF?text= ) | HOTPINK             | #ff5faf |
| ![#ff5fd7](https://placehold.it/40x40/ff5fd7/FFFFFF?text= ) | HOTPINK_1           | #ff5fd7 |
| ![#ff5fff](https://placehold.it/40x40/ff5fff/FFFFFF?text= ) | PINK_FLAMINGO       | #ff5fff |
| ![#ff8700](https://placehold.it/40x40/ff8700/FFFFFF?text= ) | FLUSH_ORANGE        | #ff8700 |
| ![#ff875f](https://placehold.it/40x40/ff875f/FFFFFF?text= ) | SALMON              | #ff875f |
| ![#ff8787](https://placehold.it/40x40/ff8787/FFFFFF?text= ) | VIVID_TANGERINE     | #ff8787 |
| ![#ff87af](https://placehold.it/40x40/ff87af/FFFFFF?text= ) | PINK_SALMON         | #ff87af |
| ![#ff87d7](https://placehold.it/40x40/ff87d7/FFFFFF?text= ) | LAVENDER_ROSE       | #ff87d7 |
| ![#ff87ff](https://placehold.it/40x40/ff87ff/FFFFFF?text= ) | BLUSH_PINK          | #ff87ff |
| ![#ffaf00](https://placehold.it/40x40/ffaf00/FFFFFF?text= ) | YELLOW_SEA          | #ffaf00 |
| ![#ffaf5f](https://placehold.it/40x40/ffaf5f/FFFFFF?text= ) | TEXAS_ROSE          | #ffaf5f |
| ![#ffaf87](https://placehold.it/40x40/ffaf87/FFFFFF?text= ) | HIT_PINK            | #ffaf87 |
| ![#ffafaf](https://placehold.it/40x40/ffafaf/FFFFFF?text= ) | SUNDOWN             | #ffafaf |
| ![#ffafd7](https://placehold.it/40x40/ffafd7/FFFFFF?text= ) | COTTON_CANDY        | #ffafd7 |
| ![#ffafff](https://placehold.it/40x40/ffafff/FFFFFF?text= ) | LAVENDER_ROSE_1     | #ffafff |
| ![#ffd700](https://placehold.it/40x40/ffd700/FFFFFF?text= ) | GOLD                | #ffd700 |
| ![#ffd75f](https://placehold.it/40x40/ffd75f/FFFFFF?text= ) | DANDELION           | #ffd75f |
| ![#ffd787](https://placehold.it/40x40/ffd787/FFFFFF?text= ) | GRANDIS             | #ffd787 |
| ![#ffd7af](https://placehold.it/40x40/ffd7af/FFFFFF?text= ) | CARAMEL             | #ffd7af |
| ![#ffd7d7](https://placehold.it/40x40/ffd7d7/FFFFFF?text= ) | COSMOS              | #ffd7d7 |
| ![#ffd7ff](https://placehold.it/40x40/ffd7ff/FFFFFF?text= ) | PINK_LACE           | #ffd7ff |
| ![#ffff5f](https://placehold.it/40x40/ffff5f/FFFFFF?text= ) | LASER_LEMON         | #ffff5f |
| ![#ffff87](https://placehold.it/40x40/ffff87/FFFFFF?text= ) | DOLLY               | #ffff87 |
| ![#ffffaf](https://placehold.it/40x40/ffffaf/FFFFFF?text= ) | PORTAFINO           | #ffffaf |
| ![#ffffd7](https://placehold.it/40x40/ffffd7/FFFFFF?text= ) | CUMULUS             | #ffffd7 |
| ![#080808](https://placehold.it/40x40/080808/FFFFFF?text= ) | COD_GRAY            | #080808 |
| ![#121212](https://placehold.it/40x40/121212/FFFFFF?text= ) | COD_GRAY_1          | #121212 |
| ![#1c1c1c](https://placehold.it/40x40/1c1c1c/FFFFFF?text= ) | COD_GRAY_2          | #1c1c1c |
| ![#262626](https://placehold.it/40x40/262626/FFFFFF?text= ) | MINE_SHAFT          | #262626 |
| ![#303030](https://placehold.it/40x40/303030/FFFFFF?text= ) | MINE_SHAFT_1        | #303030 |
| ![#3a3a3a](https://placehold.it/40x40/3a3a3a/FFFFFF?text= ) | MINE_SHAFT_2        | #3a3a3a |
| ![#444444](https://placehold.it/40x40/444444/FFFFFF?text= ) | TUNDORA             | #444444 |
| ![#4e4e4e](https://placehold.it/40x40/4e4e4e/FFFFFF?text= ) | TUNDORA_1           | #4e4e4e |
| ![#585858](https://placehold.it/40x40/585858/FFFFFF?text= ) | SCORPION_1          | #585858 |
| ![#626262](https://placehold.it/40x40/626262/FFFFFF?text= ) | DOVE_GRAY           | #626262 |
| ![#6c6c6c](https://placehold.it/40x40/6c6c6c/FFFFFF?text= ) | DOVE_GRAY_1         | #6c6c6c |
| ![#767676](https://placehold.it/40x40/767676/FFFFFF?text= ) | BOULDER             | #767676 |
| ![#8a8a8a](https://placehold.it/40x40/8a8a8a/FFFFFF?text= ) | GRAY_2              | #8a8a8a |
| ![#8a8a8a](https://placehold.it/40x40/8a8a8a/FFFFFF?text= ) | GREY_2              | #8a8a8a |
| ![#949494](https://placehold.it/40x40/949494/FFFFFF?text= ) | DUSTY_GRAY          | #949494 |
| ![#9e9e9e](https://placehold.it/40x40/9e9e9e/FFFFFF?text= ) | SILVER_CHALICE_1    | #9e9e9e |
| ![#a8a8a8](https://placehold.it/40x40/a8a8a8/FFFFFF?text= ) | SILVER_CHALICE_2    | #a8a8a8 |
| ![#b2b2b2](https://placehold.it/40x40/b2b2b2/FFFFFF?text= ) | SILVER_CHALICE_3    | #b2b2b2 |
| ![#bcbcbc](https://placehold.it/40x40/bcbcbc/FFFFFF?text= ) | SILVER_1            | #bcbcbc |
| ![#c6c6c6](https://placehold.it/40x40/c6c6c6/FFFFFF?text= ) | SILVER_2            | #c6c6c6 |
| ![#d0d0d0](https://placehold.it/40x40/d0d0d0/FFFFFF?text= ) | ALTO_1              | #d0d0d0 |
| ![#dadada](https://placehold.it/40x40/dadada/FFFFFF?text= ) | ALTO_2              | #dadada |
| ![#e4e4e4](https://placehold.it/40x40/e4e4e4/FFFFFF?text= ) | MERCURY             | #e4e4e4 |
| ![#eeeeee](https://placehold.it/40x40/eeeeee/FFFFFF?text= ) | GALLERY             | #eeeeee |
