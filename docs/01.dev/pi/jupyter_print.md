# Jupyterの標準出力

Jupyterでは標準出力も画面に表示できます。

## print

```python
import sys

while True:
	sys.stdout.write("\rvalue = %d" % value)
	sys.stdout.flush()
    	value += 1
```


![](../img/dev/jupyter/jupyter009.png)

画面にScroll Barがでて、どんどん下の方に追加されていく。

## sys.stdout.write

```python
import sys

while True:
    sys.stdout.write("\rvalue = %d" % value)
    sys.stdout.flush()
    value += 1
```

同じ場所をどんどん更新していく。

![](../img/dev/jupyter/jupyter010.png)