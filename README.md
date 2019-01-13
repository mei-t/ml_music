# ml_music
Compose music with machine learning.

## Training data
* music/liszt/liz_donjuan.mid
* music/liszt/liz_et1.mid
* ...

These are converted to "piano roll" array (time × 128 keys) as preprocessing.
![Piano roll](images/piano_roll.png)

## Architecture
```
tf.keras.Sequential([
    tf.keras.layers.Dense(...),
    tf.keras.layers.LSTM(...),
    tf.keras.layers.Dense(...),
])
```

## Genarated music example
Raw output.
![Genarated music example](images/genarated_music_example.png)
Discretizesed output. See piano_roll_to_pretty_midi in [music-playground.ipynb](music-playground.ipynb)
![Generated music example (discretized)](images/genarated_music_example_midi.png)

