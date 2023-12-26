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

> **Note**
> Separator can contain only one character.

### You can also paint your content

**Supported colors:**
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- gray / grey
- light red
- light green
- light yellow
- light blue
- light magenta
- light cyan

```python
    from termspark import TermSpark

    TermSpark().print_right('RIGHT', 'blue').spark()
    TermSpark().print_left('LEFT', 'light red').spark()
    TermSpark().print_center('CENTER', 'light_green').spark()
```

**Supported highlights:**
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- gray / grey
- light red
- light green
- light yellow
- light blue
- light magenta
- light cyan

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
> **Warning**
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
> **Warning**
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

> **Note**
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
