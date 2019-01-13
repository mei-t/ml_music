# ml_music
compose music with machine learning

## Training data
* music/liszt/liz_donjuan.mid
* music/liszt/liz_et1.mid
* ...

These are converted to "piano roll" array (time × 128 keys) as preprocessing.

## Architecture
```
tf.keras.Sequential([
    tf.keras.layers.Dense(...),
    tf.keras.layers.LSTM(...),
    tf.keras.layers.Dense(...),
])
```

## Genarated music example

