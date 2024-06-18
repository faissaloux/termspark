# Usage

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
- curly underline
- dotted underline
- dashed underline
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
| ![#000000](https://placehold.it/40x40/000000/ffffff?text= ) | black               | #000000 |
| ![#800000](https://placehold.it/40x40/800000/ffffff?text= ) | maroon              | #800000 |
| ![#008000](https://placehold.it/40x40/008000/ffffff?text= ) | green               | #008000 |
| ![#808000](https://placehold.it/40x40/808000/ffffff?text= ) | olive               | #808000 |
| ![#000080](https://placehold.it/40x40/000080/ffffff?text= ) | navy                | #000080 |
| ![#800080](https://placehold.it/40x40/800080/ffffff?text= ) | purple              | #800080 |
| ![#008080](https://placehold.it/40x40/008080/ffffff?text= ) | teal                | #008080 |
| ![#c0c0c0](https://placehold.it/40x40/c0c0c0/ffffff?text= ) | silver              | #C0C0C0 |
| ![#808080](https://placehold.it/40x40/808080/ffffff?text= ) | gray                | #808080 |
| ![#808080](https://placehold.it/40x40/808080/ffffff?text= ) | grey                | #808080 |
| ![#ff0000](https://placehold.it/40x40/ff0000/ffffff?text= ) | red                 | #FF0000 |
| ![#00ff00](https://placehold.it/40x40/00ff00/ffffff?text= ) | lime                | #00FF00 |
| ![#ffff00](https://placehold.it/40x40/ffff00/ffffff?text= ) | yellow              | #FFFF00 |
| ![#0000ff](https://placehold.it/40x40/0000ff/ffffff?text= ) | blue                | #0000FF |
| ![#ff00ff](https://placehold.it/40x40/ff00ff/ffffff?text= ) | fuchsia             | #FF00FF |
| ![#00ffff](https://placehold.it/40x40/00ffff/ffffff?text= ) | aqua                | #00FFFF |
| ![#ffffff](https://placehold.it/40x40/ffffff/ffffff?text= ) | white               | #FFFFFF |
| ![#00005f](https://placehold.it/40x40/00005f/ffffff?text= ) | navy blue           | #00005F |
| ![#000087](https://placehold.it/40x40/000087/ffffff?text= ) | dark blue           | #000087 |
| ![#0000af](https://placehold.it/40x40/0000af/ffffff?text= ) | dark blue 2         | #0000AF |
| ![#0000d7](https://placehold.it/40x40/0000d7/ffffff?text= ) | dark blue 1         | #0000D7 |
| ![#005f00](https://placehold.it/40x40/005f00/ffffff?text= ) | dark green          | #005F00 |
| ![#005f5f](https://placehold.it/40x40/005f5f/ffffff?text= ) | blue stone          | #005F5F |
| ![#005f87](https://placehold.it/40x40/005f87/ffffff?text= ) | orient              | #005F87 |
| ![#005faf](https://placehold.it/40x40/005faf/ffffff?text= ) | endeavour           | #005FAF |
| ![#005fd7](https://placehold.it/40x40/005fd7/ffffff?text= ) | science blue        | #005FD7 |
| ![#005fff](https://placehold.it/40x40/005fff/ffffff?text= ) | blue ribbon         | #005FFF |
| ![#008700](https://placehold.it/40x40/008700/ffffff?text= ) | japanese laurel     | #008700 |
| ![#00875f](https://placehold.it/40x40/00875f/ffffff?text= ) | deep sea            | #00875F |
| ![#008787](https://placehold.it/40x40/008787/ffffff?text= ) | turquoise           | #008787 |
| ![#0087af](https://placehold.it/40x40/0087af/ffffff?text= ) | deep cerulean       | #0087AF |
| ![#0087d7](https://placehold.it/40x40/0087d7/ffffff?text= ) | lochmara            | #0087D7 |
| ![#0087ff](https://placehold.it/40x40/0087ff/ffffff?text= ) | azure radiance      | #0087FF |
| ![#00af00](https://placehold.it/40x40/00af00/ffffff?text= ) | islamic green       | #00AF00 |
| ![#00af5f](https://placehold.it/40x40/00af5f/ffffff?text= ) | spring green        | #00AF5F |
| ![#00af87](https://placehold.it/40x40/00af87/ffffff?text= ) | dark cyan           | #00AF87 |
| ![#00afaf](https://placehold.it/40x40/00afaf/ffffff?text= ) | light sea green     | #00AFAF |
| ![#00afd7](https://placehold.it/40x40/00afd7/ffffff?text= ) | cerulean            | #00AFD7 |
| ![#00afff](https://placehold.it/40x40/00afff/ffffff?text= ) | blue bolt           | #00AFFF |
| ![#00d700](https://placehold.it/40x40/00d700/ffffff?text= ) | electric green      | #00D700 |
| ![#00d75f](https://placehold.it/40x40/00d75f/ffffff?text= ) | malachite           | #00D75F |
| ![#00d787](https://placehold.it/40x40/00d787/ffffff?text= ) | caribbean green     | #00D787 |
| ![#00d7af](https://placehold.it/40x40/00d7af/ffffff?text= ) | cyan 1              | #00D7AF |
| ![#00d7d7](https://placehold.it/40x40/00d7d7/ffffff?text= ) | dark turquoise      | #00D7D7 |
| ![#00d7ff](https://placehold.it/40x40/00d7ff/ffffff?text= ) | vivid sky blue      | #00D7FF |
| ![#00ff00](https://placehold.it/40x40/00ff00/ffffff?text= ) | electric green 1    | #00FF00 |
| ![#00ff5f](https://placehold.it/40x40/00ff5f/ffffff?text= ) | guppie green        | #00FF5F |
| ![#00ff87](https://placehold.it/40x40/00ff87/ffffff?text= ) | spring green 1      | #00FF87 |
| ![#00ffaf](https://placehold.it/40x40/00ffaf/ffffff?text= ) | medium spring green | #00FFAF |
| ![#00ffd7](https://placehold.it/40x40/00ffd7/ffffff?text= ) | sea green           | #00FFD7 |
| ![#00ffff](https://placehold.it/40x40/00ffff/ffffff?text= ) | cyan                | #00FFFF |
| ![#5f0000](https://placehold.it/40x40/5f0000/ffffff?text= ) | rosewood            | #5F0000 |
| ![#5f005f](https://placehold.it/40x40/5f005f/ffffff?text= ) | pompadour           | #5F005F |
| ![#5f0087](https://placehold.it/40x40/5f0087/ffffff?text= ) | pigment indigo      | #5F0087 |
| ![#5f00af](https://placehold.it/40x40/5f00af/ffffff?text= ) | purple 3            | #5F00AF |
| ![#5f00d7](https://placehold.it/40x40/5f00d7/ffffff?text= ) | electic violet      | #5F00D7 |
| ![#5f00ff](https://placehold.it/40x40/5f00ff/ffffff?text= ) | blue violet         | #5F00FF |
| ![#5f5f00](https://placehold.it/40x40/5f5f00/ffffff?text= ) | verdun green        | #5F5F00 |
| ![#5f5f5f](https://placehold.it/40x40/5f5f5f/ffffff?text= ) | scorpion            | #5F5F5F |
| ![#5f5f87](https://placehold.it/40x40/5f5f87/ffffff?text= ) | comet               | #5F5F87 |
| ![#5f5faf](https://placehold.it/40x40/5f5faf/ffffff?text= ) | scampi              | #5F5FAF |
| ![#5f5fd7](https://placehold.it/40x40/5f5fd7/ffffff?text= ) | indigo              | #5F5FD7 |
| ![#5f5fff](https://placehold.it/40x40/5f5fff/ffffff?text= ) | cornflower blue 1   | #5F5FFF |
| ![#5f8700](https://placehold.it/40x40/5f8700/ffffff?text= ) | limeade             | #5F8700 |
| ![#5f875f](https://placehold.it/40x40/5f875f/ffffff?text= ) | glade green         | #5F875F |
| ![#5f8787](https://placehold.it/40x40/5f8787/ffffff?text= ) | juniper             | #5F8787 |
| ![#5f87af](https://placehold.it/40x40/5f87af/ffffff?text= ) | hippie blue         | #5F87AF |
| ![#5f87d7](https://placehold.it/40x40/5f87d7/ffffff?text= ) | havelock blue       | #5F87D7 |
| ![#5f87ff](https://placehold.it/40x40/5f87ff/ffffff?text= ) | cornflower blue     | #5F87FF |
| ![#5faf00](https://placehold.it/40x40/5faf00/ffffff?text= ) | limea               | #5FAF00 |
| ![#5faf5f](https://placehold.it/40x40/5faf5f/ffffff?text= ) | fern                | #5FAF5F |
| ![#5faf87](https://placehold.it/40x40/5faf87/ffffff?text= ) | silver tree         | #5FAF87 |
| ![#5fafaf](https://placehold.it/40x40/5fafaf/ffffff?text= ) | tradewind           | #5FAFAF |
| ![#5fafd7](https://placehold.it/40x40/5fafd7/ffffff?text= ) | shakespeare         | #5FAFD7 |
| ![#5fafff](https://placehold.it/40x40/5fafff/ffffff?text= ) | malibu              | #5FAFFF |
| ![#5fd700](https://placehold.it/40x40/5fd700/ffffff?text= ) | bright green        | #5FD700 |
| ![#5fd75f](https://placehold.it/40x40/5fd75f/ffffff?text= ) | pale green          | #5FD75F |
| ![#5fd787](https://placehold.it/40x40/5fd787/ffffff?text= ) | pastel green        | #5FD787 |
| ![#5fd7af](https://placehold.it/40x40/5fd7af/ffffff?text= ) | downy               | #5FD7AF |
| ![#5fd7d7](https://placehold.it/40x40/5fd7d7/ffffff?text= ) | viking              | #5FD7D7 |
| ![#5fd7ff](https://placehold.it/40x40/5fd7ff/ffffff?text= ) | steel blue          | #5FD7FF |
| ![#5fff00](https://placehold.it/40x40/5fff00/ffffff?text= ) | chartreuse          | #5FFF00 |
| ![#5fff5f](https://placehold.it/40x40/5fff5f/ffffff?text= ) | screaming green     | #5FFF5F |
| ![#5fff87](https://placehold.it/40x40/5fff87/ffffff?text= ) | sea green 1         | #5FFF87 |
| ![#5fffaf](https://placehold.it/40x40/5fffaf/ffffff?text= ) | aquamarine 1        | #5FFFAF |
| ![#5fffd7](https://placehold.it/40x40/5fffd7/ffffff?text= ) | aquamarine 2        | #5FFFD7 |
| ![#5fffff](https://placehold.it/40x40/5fffff/ffffff?text= ) | aquamarine          | #5FFFFF |
| ![#870000](https://placehold.it/40x40/870000/ffffff?text= ) | dark red            | #870000 |
| ![#87005f](https://placehold.it/40x40/87005f/ffffff?text= ) | fresh eggplant      | #87005F |
| ![#870087](https://placehold.it/40x40/870087/ffffff?text= ) | dark magenta        | #870087 |
| ![#8700af](https://placehold.it/40x40/8700af/ffffff?text= ) | purple 2            | #8700AF |
| ![#8700d7](https://placehold.it/40x40/8700d7/ffffff?text= ) | electric violet     | #8700D7 |
| ![#8700ff](https://placehold.it/40x40/8700ff/ffffff?text= ) | purple 1            | #8700FF |
| ![#875f00](https://placehold.it/40x40/875f00/ffffff?text= ) | brown               | #875F00 |
| ![#875f5f](https://placehold.it/40x40/875f5f/ffffff?text= ) | copper rose         | #875F5F |
| ![#875f87](https://placehold.it/40x40/875f87/ffffff?text= ) | strike master       | #875F87 |
| ![#875faf](https://placehold.it/40x40/875faf/ffffff?text= ) | deluge              | #875FAF |
| ![#875fd7](https://placehold.it/40x40/875fd7/ffffff?text= ) | medium purple       | #875FD7 |
| ![#875fff](https://placehold.it/40x40/875fff/ffffff?text= ) | heliotrope          | #875FFF |
| ![#878700](https://placehold.it/40x40/878700/ffffff?text= ) | olive 1             | #878700 |
| ![#87875f](https://placehold.it/40x40/87875f/ffffff?text= ) | clay creek          | #87875F |
| ![#878787](https://placehold.it/40x40/878787/ffffff?text= ) | gray 1              | #878787 |
| ![#878787](https://placehold.it/40x40/878787/ffffff?text= ) | grey 1              | #878787 |
| ![#8787af](https://placehold.it/40x40/8787af/ffffff?text= ) | wild blue yonder    | #8787AF |
| ![#8787d7](https://placehold.it/40x40/8787d7/ffffff?text= ) | chetwode blue       | #8787D7 |
| ![#8787ff](https://placehold.it/40x40/8787ff/ffffff?text= ) | light slate blue    | #8787FF |
| ![#87af00](https://placehold.it/40x40/87af00/ffffff?text= ) | limeade 1           | #87AF00 |
| ![#87af5f](https://placehold.it/40x40/87af5f/ffffff?text= ) | chelsea cucumber    | #87AF5F |
| ![#87af87](https://placehold.it/40x40/87af87/ffffff?text= ) | bay leaf            | #87AF87 |
| ![#87afaf](https://placehold.it/40x40/87afaf/ffffff?text= ) | gulf stream         | #87AFAF |
| ![#87afd7](https://placehold.it/40x40/87afd7/ffffff?text= ) | polo blue           | #87AFD7 |
| ![#87afff](https://placehold.it/40x40/87afff/ffffff?text= ) | malibu 1            | #87AFFF |
| ![#87d700](https://placehold.it/40x40/87d700/ffffff?text= ) | pistachio           | #87D700 |
| ![#87d75f](https://placehold.it/40x40/87d75f/ffffff?text= ) | dark olive green    | #87D75F |
| ![#87d787](https://placehold.it/40x40/87d787/ffffff?text= ) | feijoa              | #87D787 |
| ![#87d7af](https://placehold.it/40x40/87d7af/ffffff?text= ) | vista blue          | #87D7AF |
| ![#87d7d7](https://placehold.it/40x40/87d7d7/ffffff?text= ) | bermuda             | #87D7D7 |
| ![#87d7ff](https://placehold.it/40x40/87d7ff/ffffff?text= ) | anakiwa             | #87D7FF |
| ![#87ff00](https://placehold.it/40x40/87ff00/ffffff?text= ) | chartreuse 1        | #87FF00 |
| ![#87ff5f](https://placehold.it/40x40/87ff5f/ffffff?text= ) | light green         | #87FF5F |
| ![#87ff87](https://placehold.it/40x40/87ff87/ffffff?text= ) | mint green          | #87FF87 |
| ![#87ffaf](https://placehold.it/40x40/87ffaf/ffffff?text= ) | pale green 1        | #87FFAF |
| ![#87ffd7](https://placehold.it/40x40/87ffd7/ffffff?text= ) | aqua marine         | #87FFD7 |
| ![#87ffff](https://placehold.it/40x40/87ffff/ffffff?text= ) | anakiwa 1           | #87FFFF |
| ![#af0000](https://placehold.it/40x40/af0000/ffffff?text= ) | bright red          | #AF0000 |
| ![#af005f](https://placehold.it/40x40/af005f/ffffff?text= ) | flirt               | #AF005F |
| ![#af0087](https://placehold.it/40x40/af0087/ffffff?text= ) | medium violet red   | #AF0087 |
| ![#af00af](https://placehold.it/40x40/af00af/ffffff?text= ) | magenta 1           | #AF00AF |
| ![#af00d7](https://placehold.it/40x40/af00d7/ffffff?text= ) | dark violet         | #AF00D7 |
| ![#af00ff](https://placehold.it/40x40/af00ff/ffffff?text= ) | purple 4            | #AF00FF |
| ![#af5f00](https://placehold.it/40x40/af5f00/ffffff?text= ) | rose of sharon      | #AF5F00 |
| ![#af5f5f](https://placehold.it/40x40/af5f5f/ffffff?text= ) | indian red          | #AF5F5F |
| ![#af5f87](https://placehold.it/40x40/af5f87/ffffff?text= ) | tapestry            | #AF5F87 |
| ![#af5faf](https://placehold.it/40x40/af5faf/ffffff?text= ) | fuchsia pink        | #AF5FAF |
| ![#af5fd7](https://placehold.it/40x40/af5fd7/ffffff?text= ) | medium purple 1     | #AF5FD7 |
| ![#af5fff](https://placehold.it/40x40/af5fff/ffffff?text= ) | heliotrope 1        | #AF5FFF |
| ![#af8700](https://placehold.it/40x40/af8700/ffffff?text= ) | pirate gold         | #AF8700 |
| ![#af875f](https://placehold.it/40x40/af875f/ffffff?text= ) | muesli              | #AF875F |
| ![#af8787](https://placehold.it/40x40/af8787/ffffff?text= ) | pharlap             | #AF8787 |
| ![#af87af](https://placehold.it/40x40/af87af/ffffff?text= ) | bouquet             | #AF87AF |
| ![#af87d7](https://placehold.it/40x40/af87d7/ffffff?text= ) | lavender            | #AF87D7 |
| ![#af87ff](https://placehold.it/40x40/af87ff/ffffff?text= ) | heliotrope 2        | #AF87FF |
| ![#afaf00](https://placehold.it/40x40/afaf00/ffffff?text= ) | gold 1              | #AFAF00 |
| ![#afaf5f](https://placehold.it/40x40/afaf5f/ffffff?text= ) | olive green         | #AFAF5F |
| ![#afaf87](https://placehold.it/40x40/afaf87/ffffff?text= ) | hillary             | #AFAF87 |
| ![#afafaf](https://placehold.it/40x40/afafaf/ffffff?text= ) | silver chalice      | #AFAFAF |
| ![#afafd7](https://placehold.it/40x40/afafd7/ffffff?text= ) | wistful             | #AFAFD7 |
| ![#afafff](https://placehold.it/40x40/afafff/ffffff?text= ) | melrose             | #AFAFFF |
| ![#afd700](https://placehold.it/40x40/afd700/ffffff?text= ) | rio grande          | #AFD700 |
| ![#afd75f](https://placehold.it/40x40/afd75f/ffffff?text= ) | conifer             | #AFD75F |
| ![#afd787](https://placehold.it/40x40/afd787/ffffff?text= ) | feijoa 1            | #AFD787 |
| ![#afd7af](https://placehold.it/40x40/afd7af/ffffff?text= ) | pixie green         | #AFD7AF |
| ![#afd7d7](https://placehold.it/40x40/afd7d7/ffffff?text= ) | jungle mist         | #AFD7D7 |
| ![#afd7ff](https://placehold.it/40x40/afd7ff/ffffff?text= ) | anakiwa 2           | #AFD7FF |
| ![#afff00](https://placehold.it/40x40/afff00/ffffff?text= ) | lime 1              | #AFFF00 |
| ![#afff5f](https://placehold.it/40x40/afff5f/ffffff?text= ) | green yellow        | #AFFF5F |
| ![#afff87](https://placehold.it/40x40/afff87/ffffff?text= ) | mint green 1        | #AFFF87 |
| ![#afffaf](https://placehold.it/40x40/afffaf/ffffff?text= ) | dark sea green      | #AFFFAF |
| ![#afffd7](https://placehold.it/40x40/afffd7/ffffff?text= ) | aero blue           | #AFFFD7 |
| ![#afffff](https://placehold.it/40x40/afffff/ffffff?text= ) | french pass         | #AFFFFF |
| ![#d70000](https://placehold.it/40x40/d70000/ffffff?text= ) | guardsman red       | #D70000 |
| ![#d7005f](https://placehold.it/40x40/d7005f/ffffff?text= ) | razzmatazz          | #D7005F |
| ![#d70087](https://placehold.it/40x40/d70087/ffffff?text= ) | hollywood cerise    | #D70087 |
| ![#d700af](https://placehold.it/40x40/d700af/ffffff?text= ) | hollywood cerise 1  | #D700AF |
| ![#d700d7](https://placehold.it/40x40/d700d7/ffffff?text= ) | purple pizzazz      | #D700D7 |
| ![#d700ff](https://placehold.it/40x40/d700ff/ffffff?text= ) | electric violet 1   | #D700FF |
| ![#d75f00](https://placehold.it/40x40/d75f00/ffffff?text= ) | tenn                | #D75F00 |
| ![#d75f5f](https://placehold.it/40x40/d75f5f/ffffff?text= ) | roman               | #D75F5F |
| ![#d75f87](https://placehold.it/40x40/d75f87/ffffff?text= ) | cranberry           | #D75F87 |
| ![#d75faf](https://placehold.it/40x40/d75faf/ffffff?text= ) | hopbush             | #D75FAF |
| ![#d75fd7](https://placehold.it/40x40/d75fd7/ffffff?text= ) | orchid              | #D75FD7 |
| ![#d75fff](https://placehold.it/40x40/d75fff/ffffff?text= ) | medium orchid       | #D75FFF |
| ![#d78700](https://placehold.it/40x40/d78700/ffffff?text= ) | mango tango         | #D78700 |
| ![#d7875f](https://placehold.it/40x40/d7875f/ffffff?text= ) | copperfield         | #D7875F |
| ![#d78787](https://placehold.it/40x40/d78787/ffffff?text= ) | pink                | #D78787 |
| ![#d787af](https://placehold.it/40x40/d787af/ffffff?text= ) | cancan              | #D787AF |
| ![#d787d7](https://placehold.it/40x40/d787d7/ffffff?text= ) | light orchid        | #D787D7 |
| ![#d787ff](https://placehold.it/40x40/d787ff/ffffff?text= ) | heliotrope 3        | #D787FF |
| ![#d7af00](https://placehold.it/40x40/d7af00/ffffff?text= ) | corn                | #D7AF00 |
| ![#d7af5f](https://placehold.it/40x40/d7af5f/ffffff?text= ) | tacha               | #D7AF5F |
| ![#d7af87](https://placehold.it/40x40/d7af87/ffffff?text= ) | tan                 | #D7AF87 |
| ![#d7afaf](https://placehold.it/40x40/d7afaf/ffffff?text= ) | clam shell          | #D7AFAF |
| ![#d7afd7](https://placehold.it/40x40/d7afd7/ffffff?text= ) | thistle             | #D7AFD7 |
| ![#d7afff](https://placehold.it/40x40/d7afff/ffffff?text= ) | mauve               | #D7AFFF |
| ![#d7d700](https://placehold.it/40x40/d7d700/ffffff?text= ) | corn 1              | #D7D700 |
| ![#d7d75f](https://placehold.it/40x40/d7d75f/ffffff?text= ) | khaki               | #D7D75F |
| ![#d7d787](https://placehold.it/40x40/d7d787/ffffff?text= ) | deco                | #D7D787 |
| ![#d7d7af](https://placehold.it/40x40/d7d7af/ffffff?text= ) | green mist          | #D7D7AF |
| ![#d7d7d7](https://placehold.it/40x40/d7d7d7/ffffff?text= ) | alto                | #D7D7D7 |
| ![#d7d7ff](https://placehold.it/40x40/d7d7ff/ffffff?text= ) | fog                 | #D7D7FF |
| ![#d7ff00](https://placehold.it/40x40/d7ff00/ffffff?text= ) | chartreuse yellow   | #D7FF00 |
| ![#d7ff5f](https://placehold.it/40x40/d7ff5f/ffffff?text= ) | canary              | #D7FF5F |
| ![#d7ff87](https://placehold.it/40x40/d7ff87/ffffff?text= ) | honeysuckle         | #D7FF87 |
| ![#d7ffaf](https://placehold.it/40x40/d7ffaf/ffffff?text= ) | reef                | #D7FFAF |
| ![#d7ffd7](https://placehold.it/40x40/d7ffd7/ffffff?text= ) | snowy mint          | #D7FFD7 |
| ![#d7ffff](https://placehold.it/40x40/d7ffff/ffffff?text= ) | oyster bay          | #D7FFFF |
| ![#ff005f](https://placehold.it/40x40/ff005f/ffffff?text= ) | rose                | #FF005F |
| ![#ff0087](https://placehold.it/40x40/ff0087/ffffff?text= ) | deep pink           | #FF0087 |
| ![#ff00af](https://placehold.it/40x40/ff00af/ffffff?text= ) | hollywood cerise 2  | #FF00AF |
| ![#ff00d7](https://placehold.it/40x40/ff00d7/ffffff?text= ) | purple pizzazz 1    | #FF00D7 |
| ![#ff00ff](https://placehold.it/40x40/ff00ff/ffffff?text= ) | magenta             | #FF00FF |
| ![#ff5f00](https://placehold.it/40x40/ff5f00/ffffff?text= ) | blaze orange        | #FF5F00 |
| ![#ff5f5f](https://placehold.it/40x40/ff5f5f/ffffff?text= ) | bitter sweet        | #FF5F5F |
| ![#ff5f87](https://placehold.it/40x40/ff5f87/ffffff?text= ) | wild watermelon     | #FF5F87 |
| ![#ff5faf](https://placehold.it/40x40/ff5faf/ffffff?text= ) | hotpink             | #FF5FAF |
| ![#ff5fd7](https://placehold.it/40x40/ff5fd7/ffffff?text= ) | hotpink 1           | #FF5FD7 |
| ![#ff5fff](https://placehold.it/40x40/ff5fff/ffffff?text= ) | pink flamingo       | #FF5FFF |
| ![#ff8700](https://placehold.it/40x40/ff8700/ffffff?text= ) | flush orange        | #FF8700 |
| ![#ff875f](https://placehold.it/40x40/ff875f/ffffff?text= ) | salmon              | #FF875F |
| ![#ff8787](https://placehold.it/40x40/ff8787/ffffff?text= ) | vivid tangerine     | #FF8787 |
| ![#ff87af](https://placehold.it/40x40/ff87af/ffffff?text= ) | pink salmon         | #FF87AF |
| ![#ff87d7](https://placehold.it/40x40/ff87d7/ffffff?text= ) | lavender rose       | #FF87D7 |
| ![#ff87ff](https://placehold.it/40x40/ff87ff/ffffff?text= ) | blush pink          | #FF87FF |
| ![#ffaf00](https://placehold.it/40x40/ffaf00/ffffff?text= ) | yellow sea          | #FFAF00 |
| ![#ffaf5f](https://placehold.it/40x40/ffaf5f/ffffff?text= ) | texas rose          | #FFAF5F |
| ![#ffaf87](https://placehold.it/40x40/ffaf87/ffffff?text= ) | hit pink            | #FFAF87 |
| ![#ffafaf](https://placehold.it/40x40/ffafaf/ffffff?text= ) | sundown             | #FFAFAF |
| ![#ffafd7](https://placehold.it/40x40/ffafd7/ffffff?text= ) | cotton candy        | #FFAFD7 |
| ![#ffafff](https://placehold.it/40x40/ffafff/ffffff?text= ) | lavender rose 1     | #FFAFFF |
| ![#ffd700](https://placehold.it/40x40/ffd700/ffffff?text= ) | gold                | #FFD700 |
| ![#ffd75f](https://placehold.it/40x40/ffd75f/ffffff?text= ) | dandelion           | #FFD75F |
| ![#ffd787](https://placehold.it/40x40/ffd787/ffffff?text= ) | grandis             | #FFD787 |
| ![#ffd7af](https://placehold.it/40x40/ffd7af/ffffff?text= ) | caramel             | #FFD7AF |
| ![#ffd7d7](https://placehold.it/40x40/ffd7d7/ffffff?text= ) | cosmos              | #FFD7D7 |
| ![#ffd7ff](https://placehold.it/40x40/ffd7ff/ffffff?text= ) | pink lace           | #FFD7FF |
| ![#ffff5f](https://placehold.it/40x40/ffff5f/ffffff?text= ) | laser lemon         | #FFFF5F |
| ![#ffff87](https://placehold.it/40x40/ffff87/ffffff?text= ) | dolly               | #FFFF87 |
| ![#ffffaf](https://placehold.it/40x40/ffffaf/ffffff?text= ) | portafino           | #FFFFAF |
| ![#ffffd7](https://placehold.it/40x40/ffffd7/ffffff?text= ) | cumulus             | #FFFFD7 |
| ![#080808](https://placehold.it/40x40/080808/ffffff?text= ) | cod gray            | #080808 |
| ![#121212](https://placehold.it/40x40/121212/ffffff?text= ) | cod gray 1          | #121212 |
| ![#1c1c1c](https://placehold.it/40x40/1c1c1c/ffffff?text= ) | cod gray 2          | #1C1C1C |
| ![#262626](https://placehold.it/40x40/262626/ffffff?text= ) | mine shaft          | #262626 |
| ![#303030](https://placehold.it/40x40/303030/ffffff?text= ) | mine shaft 1        | #303030 |
| ![#3a3a3a](https://placehold.it/40x40/3a3a3a/ffffff?text= ) | mine shaft 2        | #3A3A3A |
| ![#444444](https://placehold.it/40x40/444444/ffffff?text= ) | tundora             | #444444 |
| ![#4e4e4e](https://placehold.it/40x40/4e4e4e/ffffff?text= ) | tundora 1           | #4E4E4E |
| ![#585858](https://placehold.it/40x40/585858/ffffff?text= ) | scorpion 1          | #585858 |
| ![#626262](https://placehold.it/40x40/626262/ffffff?text= ) | dove gray           | #626262 |
| ![#6c6c6c](https://placehold.it/40x40/6c6c6c/ffffff?text= ) | dove gray 1         | #6C6C6C |
| ![#767676](https://placehold.it/40x40/767676/ffffff?text= ) | boulder             | #767676 |
| ![#8a8a8a](https://placehold.it/40x40/8a8a8a/ffffff?text= ) | gray 2              | #8A8A8A |
| ![#8a8a8a](https://placehold.it/40x40/8a8a8a/ffffff?text= ) | grey 2              | #8A8A8A |
| ![#949494](https://placehold.it/40x40/949494/ffffff?text= ) | dusty gray          | #949494 |
| ![#9e9e9e](https://placehold.it/40x40/9e9e9e/ffffff?text= ) | silver chalice 1    | #9E9E9E |
| ![#a8a8a8](https://placehold.it/40x40/a8a8a8/ffffff?text= ) | silver chalice 2    | #A8A8A8 |
| ![#b2b2b2](https://placehold.it/40x40/b2b2b2/ffffff?text= ) | silver chalice 3    | #B2B2B2 |
| ![#bcbcbc](https://placehold.it/40x40/bcbcbc/ffffff?text= ) | silver 1            | #BCBCBC |
| ![#c6c6c6](https://placehold.it/40x40/c6c6c6/ffffff?text= ) | silver 2            | #C6C6C6 |
| ![#d0d0d0](https://placehold.it/40x40/d0d0d0/ffffff?text= ) | alto 1              | #D0D0D0 |
| ![#dadada](https://placehold.it/40x40/dadada/ffffff?text= ) | alto 2              | #DADADA |
| ![#e4e4e4](https://placehold.it/40x40/e4e4e4/ffffff?text= ) | mercury             | #E4E4E4 |
| ![#eeeeee](https://placehold.it/40x40/eeeeee/ffffff?text= ) | gallery             | #EEEEEE |
